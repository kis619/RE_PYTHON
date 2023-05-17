from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    King class
    Inherits from Baratheon and Lannister
    Attributes:
        first_name: a string representing the first name of the character
        is_alive: a boolean representing if the character is alive or not
        family_name: inherited from Baratheon
        eyes: inherited from Baratheon
        hairs: inherited from Baratheon
    Methods:
        die: set is_alive to False
        set_eyes: set eyes color
        set_hairs: set hairs color
        get_eyes: get eyes color
        get_hairs: get hairs color
    """

    def __init__(self, first_name):
        """
        Constructor of the class King
        that inherits from Baratheon and Lannister
        """
        super().__init__(first_name)

    def set_eyes(self, eyes):
        """Set eyes color"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set hairs color"""
        self.hairs = hairs

    def get_eyes(self):
        """Get eyes color"""
        return self.eyes

    def get_hairs(self):
        """Get hairs color"""
        return self.hairs
