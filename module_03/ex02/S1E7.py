from S1E9 import Character


class Baratheon(Character):
    """
    Baratheon class
    Attributes:
        first_name: a string representing the first name of the character
        is_alive: a boolean representing if the character is alive or not
        family_name: a default string - Baratheon
        eyes: a default string - brown
        hairs: a default string - dark
    Methods:
        die: set is_alive to False
    """

    def __init__(self, first_name, is_alive=True):
        """
        Constructor of the class Baratheon that inherits from Character
        """
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        Set is_alive to False
        """
        self.is_alive = False

    def __repr__(self) -> str:
        """
        repr() function returns a printable representation of the given object
        """
        return f"Baratheon(first_name='{self.first_name}', " \
            f"is_alive={self.is_alive}, family_name='{self.family_name}', " \
            f"eyes='{self.eyes}', hairs='{self.hairs}')"

    def create_baratheon(first_name, is_alive):
        """
        Create a Baratheon
        """
        return Baratheon(first_name, is_alive)


class Lannister(Character):
    """
    Lanister class
    Attributes:
        first_name: a string representing the first name of the character
        is_alive: a boolean representing if the character is alive or not
        family_name: a default string - Lanister
        eyes: a default string - brown
        hairs: a default string - dark
    Methods:
        die: set is_alive to False
    """

    def __init__(self, first_name, is_alive=True):
        """
        Constructor of the class Lanister that inherits from Character
        """
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lanister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """
        Set is_alive to False
        """
        self.is_alive = False

    def __repr__(self) -> str:
        """
        repr() function returns a printable representation of the given object
        """
        return f"Lanister(first_name='{self.first_name}', " \
            f"is_alive={self.is_alive}, family_name='{self.family_name}', " \
            f"eyes='{self.eyes}', hairs='{self.hairs}')"

    def create_lannister(first_name, is_alive):
        """
        Create a Lannister
        """
        return Lannister(first_name, is_alive)
