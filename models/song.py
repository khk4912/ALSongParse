from models.lyric import Lyric
from dataclasses import dataclass


class Song:
    def __init__(
        self, title: str, artist: str, album: str, lyric_id: str
    ) -> None:
        self.title = title
        self.artist = artist
        self.album = album
        self.lyric_id = lyric_id
        self.lyric = Lyric(lyric_id=lyric_id)

    def __repr__(self):
        return f"{self.__class__.__qualname__}({', '.join([f'{x}={y}' for x, y in self.__dict__.items()])})"
