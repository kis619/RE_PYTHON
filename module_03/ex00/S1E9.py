from abc import ABC, abstractclassmethod


class Character(ABC):
    """
    Character class
    Attributes:
        first_name: a string representing the first name of the character
        is_alive: a boolean representing if the character is alive or not
    Methods:
        die: abstract method
    """

    def __init__(self, first_name, is_alive=True):
        """
        Constructor of the class Character
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractclassmethod
    def die(self):
        """abstract method"""
        pass


class Stark(Character):
    """
    Stark class
    Attributes:
        first_name: a string representing the first name of the character
        is_alive: a boolean representing if the character is alive or not
    Methods:
        die: set is_alive to False
    """

    def __init__(self, first_name, is_alive=True):
        """
        Constructor of the class Stark that inherits from Character
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Set is_alive to False
        """
        self.is_alive = False


def main():
    ...


if __name__ == '__main__':
    main()
