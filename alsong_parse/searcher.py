import eyed3
from typing import Dict, Union
from bs4 import BeautifulSoup
from .errors import NoLyricException
from .utils import Utils
from .models import Lyric


class Searcher:
    """ 가사 검색에 관련한 함수를 포함한 클래스입니다. """

    def search(self, filename: str):
        """
        파일을 기반으로 자동으로 
        제목, 아티스트명, 길이를 얻어 검색하여 정보를 리턴하는 함수입니다.  

        mp3만 지원하며, I3U 태그가 있어야합니다.

        파라미터
            filename: 가사를 찾을 파일 이름(mp3)
        """
        info = Utils.get_info(filename)
        xml = Utils.search_xml(info)
        data = Utils.post(xml)

        return Lyric(data)

    def search_with_info(
        self, title: str, artist: str, max_result: int = 1
    ) -> list:
        """
        I3U 태그 기반으로 정보를 얻는 Searcher.search 함수와 다르게,  
        곡 제목과 아티스트 명, 길이를 받아 가사를 검색합니다.  

        I3U 태그가 없을 때, 더 넓은 범위의 가사를 검색할 때 유용합니다.


        파라미터
            title: 검색할 노래 제목
            artist: 검색할 노래의 아티스트 이름
            length: 검색하는 노래의 밀리세컨트 초(int)
        """
        info = {"title": title, "artist": artist}
        headers = {
            "SOAPAction": "ALSongWebServer/GetResembleLyricList2",
            "Content-Type": "application/soap+xml",
            "User-Agent": "gSOAP/2.7",
        }
        xml = Utils.search_with_info_xml(info)
        xml_data = Utils.post(xml, headers)

        xml_data = BeautifulSoup(xml_data, "lxml-xml")
        searchlyric_list = xml_data.find_all("ST_SEARCHLYRIC_LIST")

        if searchlyric_list == []:
            raise NoLyricException("가사를 찾을 수 없습니다.")

        total_searchlyric = len(searchlyric_list)

        if max_result > total_searchlyric:
            max_result = total_searchlyric

        pre_result = [
            searchlyric_list[x].find("lyricID").text for x in range(max_result)
        ]

        headers = {
            "SOAPAction": "ALSongWebServer/GetLyricByID2",
            "Content-Type": "application/soap+xml",
            "User-Agent": "gSOAP/2.7",
        }
        result = []
        for i in pre_result:
            pre_xml = Utils.search_with_id_xml(i)
            data = Utils.post(pre_xml, headers=headers)
            result.append(Lyric(data, is_id_search=True))
        return result

    def search_with_mp3(self, fileename: str):
        """
        mp3 파일 자체의 해시로만 검색을 시도합니다.
        곡 제목, 아티스트 등 정보를 몰라도 검색할 수 있습니다.

        하지만, 찾을 확률은 다른 방법에 비해서 떨어집니다.

        파라미터
            filename: 가사를 찾을 파일 이름(mp3)
        """
        xml = Utils.search_with_mp3_xml(fileename)
        data = Utils.post(xml)
        return Lyric(data, is_mp3_search=True)
