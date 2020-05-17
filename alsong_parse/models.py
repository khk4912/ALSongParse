import aiofiles
from bs4 import BeautifulSoup
from .errors import BadStatusException, NoLyricException


class Lyric:
    """ XML을 파싱하여 나오는 가사 모델입니다. """

    def __init__(
        self,
        xml_data: str,
        is_mp3_search: bool = False,
        is_id_search: bool = False,
    ):
        self.xml_data = BeautifulSoup(xml_data, "lxml-xml")

        if is_mp3_search:
            status_id = self._xml_find(self.xml_data, "GetMurekaInfoResult")
            if status_id == "false":
                raise BadStatusException("정상이 아닌 StatusID를 받았습니다.")

        elif is_id_search:
            status_id = self._xml_find(self.xml_data, "GetLyricByID2Result")
            if status_id == "false":
                raise BadStatusException("정상이 아닌 StatusID를 받았습니다.")

        else:
            status_id = int(self._xml_find(self.xml_data, "strStatusID"))
            info_id = int(self._xml_find(self.xml_data, "strInfoID"))

            if status_id == 2:
                raise BadStatusException("정상이 아닌 StatusID를 받았습니다.")

            if info_id == 0:
                raise NoLyricException("정보를 찾지 못했습니다.")

        if is_id_search:
            self.title = self._xml_find(self.xml_data, "title")
            self.artist = self.xml_data(self.xml_data, "artist")
            pre_lyric = self._xml_find(self.xml_data, "lyric").split("<br>")
            self.lyrics = "\n".join(pre_lyric)
        else:
            self.title = self._xml_find(self.xml_data, "strTitle")
            self.artist = self._xml_find(self.xml_data, "strArtist")
            pre_lyric = self._xml_find(self.xml_data, "strLyric").split("<br>")
            self.lyrics = "\n".join(pre_lyric)

    def _xml_find(self, soup: BeautifulSoup, tag: str) -> str:
        """
        내부에서 XML 데이터를 처리할 때 사용합니다.
        값을 얻은 후 strip 한 값을 반환합니다.

        파라미터
            soup: BeautifulSoup
            tag: 찾을 태그
        """
        tg_tag = soup.find(tag)
        if tg_tag is None:
            return None
        return tg_tag.text.strip()

    def save_to_lrc(self, filename: str = None):
        """
        lrc 파일로 저장하는 함수입니다.
        
        파라미터
            filename: 저장할 파일 이름,
                      설정하지 않으면 자동으로 정합니다.
        """
        if filename is None:
            filename = "{} - {}.lrc".format(self.artist, self.title)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.lyrics)
