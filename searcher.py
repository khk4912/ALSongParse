import eyed3
import asyncio
import aiohttp
import aiofiles
from typing import Dict, Union
from utils import Utils


class Searcher:
    """ 가사 검색에 관련한 함수를 포함한 클래스입니다. """

    @classmethod
    async def search(cls, filename: str):
        """
        파일을 기반으로 자동으로 
        제목, 아티스트명, 길이를 얻어 검색하여 정보를 리턴하는 함수입니다.  

        mp3만 지원하며, I3U 태그가 있어야합니다.

        파라미터
            filename: 가사를 찾을 파일 이름(mp3)
        """
        info = await Utils.get_info(filename)
        xml = await Utils.search_xml(info)
        data = await Utils.post(xml)

        return data

    @classmethod
    async def search_with_info(cls, title: str, artist: str, length: int):
        """
        I3U 태그 기반으로 정보를 얻는 Searcher.search 함수와 다르게,  
        곡 제목과 아티스트 명, 길이를 받아 가사를 검색합니다.  

        I3U 태그가 없을 때 유용합니다.

        파라미터
            title: 검색할 노래 제목
            artist: 검색할 노래의 아티스트 이름
            length: 검색하는 노래의 밀리세컨트 초(int)
        """
        info = {"title": title, "artist": artist, "length": length}
        xml = await Utils.search_xml(info)
        data = await Utils.post(xml)
        return data

    @classmethod
    async def search_with_mp3(cls, fileename: str):
        """
        mp3 파일 자체의 해시로만 검색을 시도합니다.
        곡 제목, 아티스트 등 정보를 몰라도 검색할 수 있습니다.

        하지만, 찾을 확률은 다른 방법에 비해서 떨어집니다.

        파라미터
            filename: 가사를 찾을 파일 이름(mp3)
        """
        xml = await Utils.search_with_mp3_xml(fileename)
        data = await Utils.post(xml)
        return data


print(asyncio.run(Searcher.search_with_mp3("창모 - METEOR(메테오).mp3")))
