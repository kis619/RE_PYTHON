class calculator:

    def __init__(self, data):
        """Constructor
        Atributtes: data (list)
        """
        self.data = data

    def __add__(self, other) -> None:
        """Addition of a number to each element of the list"""
        self.data = [x + other for x in self.data]
        print(self.data)

    def __sub__(self, other) -> None:
        """Subtraction of a number to each element of the list"""
        self.data = [x - other for x in self.data]
        print(self.data)

    def __mul__(self, other) -> None:
        """Multiplication of a number to each element of the list"""
        self.data = [x * other for x in self.data]
        print(self.data)

    def __truediv__(self, other) -> None:
        """Division of a number to each element of the list"""
        try:
            self.data = [x / other for x in self.data]
        except ZeroDivisionError:
            print("ZeroDivisionError: division by zero")
        else:
            print(self.data)
