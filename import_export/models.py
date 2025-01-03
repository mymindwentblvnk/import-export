import dataclasses


@dataclasses.dataclass
class ImportEntry:

    user_id: str
    first_name: str
    last_name: str

    def __dict__(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }
