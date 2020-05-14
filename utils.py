import aiofiles
import hashlib
import eyed3
import aiohttp
from bs4 import BeautifulSoup
from typing import Union, Dict
from envs import XML_TEMPLATE, XML_WITH_MP3_TEMPLATE
from errors import InvaildID3


class Utils:
    """ 필요한 메소드를 모아둔 클래스입니다. """

    @classmethod
    async def search_xml(cls, info: dict) -> str:
        """
        Searcher.search 에서 POST 할 XML 데이터를 생성해 리턴합니다.  

        파라미터
            info: Utils.get_info 함수가 리턴하는 Dict
        """
        title = info["title"]
        artist = info["artist"]
        length = info["length"]
        xml = XML_TEMPLATE.format(
            title=title, artist=artist, ms_playtime=length
        )

        return xml.strip()

    @classmethod
    async def search_with_mp3_xml(cls, filename: str) -> str:
        """
        Searcher.search_with_mp3 에서 POST 할 XML 데이터를 생성해 리턴합니다.  

        파라미터
            title: 검색할 노래의 제목
            artist: 검색할 노래의 아티스트
        """
        xml = XML_WITH_MP3_TEMPLATE.format(
            hash=await cls.create_mp3_hash(filename)
        )
        return xml.strip()

    @classmethod
    async def create_mp3_hash(cls, filename: str) -> str:
        """
        알송 검색시 사용하는 mp3 해시 값을 리턴합니다.  
        mp3 파일을 1638400 바이트를 읽어 md5로 해시한 값을 반환합니다.  

        파라미터
            filename: 해시값을 얻을 파일 이름(mp3)
        """
        hasher = hashlib.md5()
        async with aiofiles.open(filename, "rb") as f:
            id3 = await f.read(10)
            if id3[:3].decode() == "ID3":
                tag_int = [x for x in id3[-4:]]
                tag_size = (
                    tag_int[0] << 21
                    | tag_int[1] << 14
                    | tag_int[2] << 7
                    | tag_int[3]
                )  ##
                await f.read(tag_size)
                buf = await f.read(163840)
            else:
                raise InvaildID3("ID3 버전이 지원되지 않습니다.")

        hasher.update(buf)
        print(hasher.hexdigest())
        return hasher.hexdigest()

    @classmethod
    async def get_info(cls, filename: str) -> Dict[str, Union[str, int]]:
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

        return {
            "filename": filename,
            "title": title,
            "artist": artist,
            "length": length,
        }

    @classmethod
    async def post(cls, data: bytes) -> str:
        """ 
        내부에서 알송 서버로 값을 POST 할 때 사용됩니다.
        
        파라미터
            data: Utils.search_xml 또는
                  Utils.search_with_info_xml의 리턴 값
        """
        headers = {"Content-Type": "application/soap+xml"}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(
                "http://lyrics.alsong.co.kr/alsongwebservice/service1.asmx",
                data=data,
            ) as r:
                return await r.text()
