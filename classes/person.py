from abc import ABC, abstractclassmethod


class Person(ABC):
    def __init__(
        self,
        name: str,
        age: int,
        role: str,
        password: str,
    ):
        self.name = name
        self.age = age
        self.role = role
        self.password = password

    @abstractclassmethod
    def all_members(self):
        pass
