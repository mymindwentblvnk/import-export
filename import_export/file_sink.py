import json
from typing import List

from import_export.models import ImportEntry


class FileSink:
    def __init__(self, path: str):
        self.path = path

    def save_file(self, entries: List[ImportEntry]):
        pass


class JsonlFileSink(FileSink):

    def save_file(self, entries: List[ImportEntry]):
        data = [e.__dict__() for e in entries]
        with open(self.path, "w", encoding="utf-8") as out_file:
            json.dump(data, out_file, ensure_ascii=False, indent=4)
