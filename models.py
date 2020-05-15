from bs4 import BeautifulSoup
from errors import CoolDownException, NoLyricException


class Lyric:
    """ XML을 파싱하여 나오는 가사 모델입니다. """

    def __init__(self, xml_data, is_mp3_search: bool = False):
        self.xml_data = BeautifulSoup(xml_data, "lxml-xml")
        if is_mp3_search:
            self.status_id = self._xml_find(
                self.xml_data, "GetMurekaInfoResult"
            )
            if self.status_id == "false":
                raise NoLyricException("정보를 찾지 못했습니다.")
        else:
            self.status_id = int(self._xml_find(self.xml_data, "strStatusID"))
            info_id = int(self._xml_find(self.xml_data, "strInfoID"))

            if self.status_id == 2:
                raise CoolDownException(
                    "너무 많은 전송으로 서버에서 정보를 받지 못했습니다. 잠시 후 재시도 하세요."
                )

            if info_id == 0:
                raise NoLyricException("정보를 찾지 못했습니다.")

        self.title = self._xml_find(self.xml_data, "strTitle")
        self.artist = self._xml_find(self.xml_data, "strAlbum")
        self.count_good = self._xml_find(self.xml_data, "strCountGood")
        self.count_bad = self._xml_find(self.xml_data, "strCountBad")
        pre_lyric = self._xml_find(self.xml_data, "strLyric").split("<br>")
        self.lyric = "\n".join(pre_lyric)

    def __str__(self):
        TEMPLATE = """
{title} - {artist}
-----
{lyric}
        """.format(
            title=self.title, artist=self.artist, lyric=self.lyric
        )
        return TEMPLATE

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
        if filename is None:
            filename = self.title + ".lrc"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.lyric)
