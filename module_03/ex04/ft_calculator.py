class calculator:

    @staticmethod
    def dotproduct(a, b):
        """
        Dot product is the sum of the products
        of the corresponding entries of the two sequences of numbers
        """
        print(f"Dot product is: {sum([x * y for x, y, in zip(a, b)])}")

    @staticmethod
    def add_vec(a, b):
        """
        Add Vector is the sum of the corresponding entries
        of the two sequences of numbers
        """
        print(f"Add Vector is : {[float(x + y) for x, y in zip(a, b)]}")

    @staticmethod
    def sous_vec(a, b):
        """
        Sous Vector is the sum of the corresponding entries
        of the two sequences of numbers
        """
        print(f"Sous Vector is: {[float(x - y) for x, y in zip(a, b)]}")
