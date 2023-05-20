def square(x):
    """
    return the square of a number x
    raise TypeError if x is not numeric
    """

    if not isinstance(x, (int, float)):
        raise TypeError('x must be numeric')
    return x * x


def pow(x):
    """
    return the power of a number x
    raise TypeError if x is not numeric
    """
    if not isinstance(x, (int, float)):
        raise TypeError('x must be numeric')
    return x ** x


def outer(x: int | float, function):
    count = 0
    def inner() -> float:
        nonlocal count, x
        x = function(x)
        count += 1
        return x
    return inner


class Dummy:
    def __init__(self, x=5):
        self.x = x

    def __call__(self):
        return self.x


def main():
    def addition(x, z=True):
        y = 2
        return x + y

    try:
        my_counter = outer(3, square)
    except TypeError as e:
        print(f"Type error: {e}")

    else:
        print(my_counter())
        print(my_counter())
        print(my_counter())
    print("---")
    try:
        another_counter = outer(1.5, pow)
    except TypeError as e:
        print(f"Type error: {e}")

    else:
        print(another_counter())
        print(another_counter())
        print(another_counter())
        print("---")
    try:
        third_counter = outer(2, addition)
        print(third_counter())
    except TypeError as e:
        print(f"Type error: {e}")

    try:
        fourth_counter = outer(2, 7)
        print(fourth_counter())
    except TypeError as e:
        print(f"Type error: {e}")

    try:
        inst = Dummy()
        fourth_counter = outer(2, inst)
        print(fourth_counter())
    except TypeError as e:
        print(f"Type error: {e}")

    try:
        fifth_counter = outer("2", pow)
        print(fifth_counter())
    except TypeError as e:
        print(f"Type error: {e}")


if __name__ == "__main__":
    main()
    # print(type(lambda: None))
