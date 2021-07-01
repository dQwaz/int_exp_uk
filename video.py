from typing import Sequence


class Video:
    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        self._title = video_title
        self._video_id = video_id
        self._tags = tuple(video_tags)

    # Dunder method to convert the memory address of the object to string
    def __str__(self):
        return f"{self._title, self._video_id, self._tags}".format(self=self)

    @property
    def title(self) -> str:
        return self._title

    @property
    def video_id(self) -> str:
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        return self._tags
