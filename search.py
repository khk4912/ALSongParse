import random
import time
from string import ascii_letters, digits
from typing import Dict, List, Optional

import requests
from bs4 import BeautifulSoup

from exceptions import NotFoundException
from model import Song
from template import (
    ENDPOINT_URL,
    GET_RESEMBLE_XML_LIST,
    GET_RESEMBLE_XML_COUNT,
    GET_RESEMBLE_XML_COUNT_HEADER,
    GET_RESEMBLE_XML_LIST_HEADER,
)


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
        soup = self._post(
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
            title=title, artist=artist or "", enc_data=self._create_enc()
        )
        soup = self._post(
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

    def _post(
        self, url: str, data: bytes, headers: Dict[str, str]
    ) -> BeautifulSoup:
        """
        Custom post method.

        Parameters
        ----------
        url : str
            URL to post.
        data : bytes
            Data to post.
        headers : Dict[str, str]
            Headers to post.

        Returns
        -------
        BeautifulSoup
            BeautifulSoup parsed XML returned from URL.
        """
        r = requests.post(url, data=data, headers=headers)
        soup = BeautifulSoup(r.text, "lxml-xml")

        return soup

    def _create_enc(self) -> str:
        pool = ascii_letters + digits
        result = ""
        for _ in range(256):
            result += random.choice(pool)

        return result
