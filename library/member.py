from library.user import User


class Member(User):
    def __init__(self, uID: int, name: str, group: int):
        super().__init__(uID, name, group)

    def scan(self) -> bool:
        pass

    def __str__(self):
        return f"Member ID {self._id}\n Member name {self._name}:\n    -This member currently has {len(self._books)} books borrowed"
