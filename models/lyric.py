from typing import Optional
from dataclasses import dataclass
from template import (
    ENDPOINT_URL,
    GET_LYRIC_BY_ID_HEADER,
    GET_LYRIC_BY_ID_TEMPLATE,
)
from utils import Utils


@dataclass
class Lyric:
    lyric_id: str

    @property
    def text(self) -> str:
        if not hasattr(self, "_text"):
            self._text = self._get_lyric_by_id(lyric_id=self.lyric_id)

        assert self._text is not None
        return self._text

    def _get_lyric_by_id(self, lyric_id: str) -> str:
        query = GET_LYRIC_BY_ID_TEMPLATE.format(
            enc_data=Utils.create_enc(), lyric_id=lyric_id
        )
        soup = Utils.post(
            url=ENDPOINT_URL,
            data=query.encode(),
            headers=GET_LYRIC_BY_ID_HEADER,
        )
        lyric: str = soup.find("lyric").text
        sp_lyric = lyric.split("\r\n")

        return "\n".join(sp_lyric)

    def save_to_lrc(self, file_name: str) -> None:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(self.text)
