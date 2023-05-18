import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate random id
    Returns: random id as string"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass()
class Student:
    """Student class
    Attributes:
        name: student name
        surname: student surname
        login: student login
        id: student id
        active: student active status
    Methods:
        __post_init__: generate login and id after init
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Generate login init"""
        self.login = (self.name[0] + self.surname[:4]).lower()


def main():
    std = Student(name='Huanita', surname='Suarez')
    print(std)


if __name__ == "__main__":
    main()
