import numpy as np
from sys import exit


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:

    try:
        np_height = np.array(height)
        np_weight = np.array(weight)
        return list(np_weight / (np_height ** 2))
    except ValueError:
        print("ValueError: eight and weight must be the same length")
        exit(1)
    except TypeError:
        print("TypeError: height and weight must be a list of int or float")
        exit(2)
    except ...:
        print("Error: an error occured")
        exit(4)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    np_bmi = np.array(bmi)
    try:
        return list(np_bmi > limit)
    except TypeError:
        print("BMI must be a list of int or float")
        exit(5)


def main():
    ...
    # test for eval
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    

if __name__ == "__main__":
    main()

