from dataclasses import dataclass


@dataclass
class Song:
    title: str
    artist: str
    album: str
    lyric_id: str

    @property
    def lyric(self) -> str:
        return "너는 해1갈"