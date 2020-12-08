from models.lyric import Lyric
from typing import List, Optional

from exceptions import NotFoundException
from models.song import Song
from template import (
    ENDPOINT_URL,
    GET_RESEMBLE_XML_COUNT,
    GET_RESEMBLE_XML_COUNT_HEADER,
    GET_RESEMBLE_XML_LIST,
    GET_RESEMBLE_XML_LIST_HEADER,
)
from utils import Utils


class Searcher:
    def __init__(self) -> None:
        pass

    def search(self, title: str, artist: Optional[str] = None) -> List[Song]:
        """
        Search lyrics with title & artist.

        Parameters
        ----------
        title : str
            Title of the song to search for.
        artist : Optional[str]
            Artist of the song to search for.

        Returns
        -------
        Lyrics
            Lyrics dataclass of the song searched.
        """
        count = self._get_resemble_count(title=title, artist=artist)

        if count == 0:
            raise NotFoundException("Can't find any lyric.")
        return self._get_resemble(title=title, artist=artist)

    def _get_resemble_count(
        self, title: str, artist: Optional[str] = None
    ) -> int:

        query = GET_RESEMBLE_XML_COUNT.format(title=title, artist=artist or "")
        soup = Utils.post(
            url=ENDPOINT_URL,
            data=query.encode(),
            headers=GET_RESEMBLE_XML_COUNT_HEADER,
        )

        count: str = soup.find("strResembleLyricCount").text
        return int(count)

    def _get_resemble(
        self, title: str, artist: Optional[str] = None
    ) -> List[Song]:
        query = GET_RESEMBLE_XML_LIST.format(
            title=title, artist=artist or "", enc_data=Utils.create_enc()
        )
        soup = Utils.post(
            url=ENDPOINT_URL,
            data=query.encode(),
            headers=GET_RESEMBLE_XML_LIST_HEADER,
        )
        results = soup.find_all("ST_SEARCHLYRIC_LIST")
        return [
            Song(
                title=x.find("title").text,
                artist=x.find("artist").text,
                lyric_id=x.find("lyricID").text,
                album=x.find("album").text,
            )
            for x in results
        ]


# s = Searcher()
# s.search("Jvcki On The Banshees")