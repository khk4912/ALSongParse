import random
from string import ascii_letters, digits
from typing import Dict

import requests
from bs4 import BeautifulSoup


class Utils:
    @staticmethod
    def post(url: str, data: bytes, headers: Dict[str, str]) -> BeautifulSoup:
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

    @staticmethod
    def create_enc() -> str:
        pool = ascii_letters + digits
        result = ""
        for _ in range(256):
            result += random.choice(pool)

        return result
