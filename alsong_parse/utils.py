import hashlib
import eyed3
import string
import random
import requests
from bs4 import BeautifulSoup
from typing import Union, Dict
from .envs import *
from .errors import InvaildID3, BadStatusException


class Utils:
    """ 필요한 메소드를 모아둔 클래스입니다. """

    @staticmethod
    def search_xml(info: dict) -> str:
        """
        Searcher.search 에서 POST 할 XML 데이터를 생성해 리턴합니다.  

        파라미터
            info: Utils.get_info 함수가 리턴하는 Dict
        """
        title = info["title"]
        artist = info["artist"]
        length = info["length"]
        enc_data = Utils.create_enc_data()
        xml = XML_TEMPLATE.format(
            title=title, artist=artist, ms_playtime=length, enc_data=enc_data
        )

        return xml.strip()

    @staticmethod
    def search_with_info_xml(info: dict) -> str:
        """
        Searcher.search_with_info 에서 POST 할 XML 데이터를 생성해 리턴합니다.
        
        파라미터
            info: TODO - 이거 작성하기
        """

        title = info["title"]
        artist = info["artist"]
        enc_data = Utils.create_enc_data()
        xml = XML_RESMBLE_TEMPLATE.format(
            title=title, artist=artist, enc_data=enc_data
        )
        return xml.strip()

    @staticmethod
    def search_with_mp3_xml(filename: str) -> str:
        """
        Searcher.search_with_mp3 에서 POST 할 XML 데이터를 생성해 리턴합니다.  

        파라미터
            filename: 검색할 mp3 파일의 이름
        """
        hashes = Utils.create_mp3_hash(filename)
        enc_data = Utils.create_enc_data()
        xml = XML_WITH_MP3_TEMPLATE.format(hash=hashes, enc_data=enc_data)
        return xml.strip()

    @staticmethod
    def search_with_id_xml(lyric_id: str) -> str:
        """
        lyric_id를 통해 POST 할 XML 데이터를 생성해 리턴합니다.

        파라미터
            lyric_id: 검색할 가사 id 
        """
        enc_data = Utils.create_enc_data()
        xml = XML_WITH_ID_TEMPLATE.format(enc_data=enc_data, lyric_id=lyric_id)

        return xml

    @staticmethod
    def create_mp3_hash(filename: str) -> str:
        """
        알송 검색시 사용하는 mp3 해시 값을 리턴합니다.  
        mp3 파일의 오디오 프레임을 1638400 바이트를 읽어 md5로 해시한 값을 리턴합니다.  

        파라미터
            filename: 해시값을 얻을 파일 이름(mp3)
        """
        hasher = hashlib.md5()
        with open(filename, "rb") as f:
            id3 = f.read(10)
            if id3[:3].decode() == "ID3":
                tag_int = [x for x in id3[-4:]]
                tag_size = (
                    tag_int[0] << 21
                    | tag_int[1] << 14
                    | tag_int[2] << 7
                    | tag_int[3]
                )  ## Read ID3
                f.read(tag_size)
                buf = f.read(163840)  ## Read 1638400 bytes from audioframes
            else:
                raise InvaildID3("ID3 버전이 지원되지 않습니다.")

        hasher.update(buf)
        return hasher.hexdigest()

    @staticmethod
    def get_info(filename: str) -> Dict[str, Union[str, int]]:
        """
        ID3 태그를 기반으로 mp3 파일에서 정보를 얻어오고,   
        파일이름, 제목, 아티스트, 길이(ms)를 포함한 dict를 리턴합니다.  

        파라미터
            filename: ID3 태그를 받아올 파일 이름
        """
        mp3 = eyed3.load(filename)
        title = mp3.tag.title
        artist = mp3.tag.artist
        length = int(mp3.info.time_secs) * 1000
        info = {
            "filename": filename,
            "title": title,
            "artist": artist,
            "length": length,
        }

        if None in info.values():
            raise InvaildID3("ID3 태그의 값 중 일부 값을 얻지 못했습니다.")

        return info

    @staticmethod
    def create_enc_data():
        pool = string.ascii_letters + string.digits
        result = ""
        for _ in range(256):
            result += random.choice(pool)

        return result

    @staticmethod
    def post(data: bytes, headers: dict = None) -> str:
        """ 
        내부에서 알송 서버로 값을 POST 할 때 사용됩니다.
        
        파라미터
            data: Utils.search_xml 또는
                  Utils.search_with_info_xml의 리턴 값
        """
        if headers is None:
            headers = {
                "Content-Type": "application/soap+xml",
                "User-Agent": "gSOAP/2.7",
            }

        r = requests.post(
            "http://lyrics.alsong.co.kr/alsongwebservice/service1.asmx",
            headers=headers,
            data=data.encode(),
        )
        if r.status_code != 200:
            raise BadStatusException(
                "HTTP Status {}를 받았습니다.".format(r.status_code)
            )
        return r.text
