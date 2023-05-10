import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Prints shape of array, slices it and prints new shape

    Args:
        family (list): list of elements
        start (int): start index to be included
        end (int): end index not to be included

    Raises:
        TypeError: if the 1st argument is not a list
        TypeError: if the indexes are not integers

    Side effects:
        prints the shape of the array before and after slicing

    Returns:
        list: the sliced list
    """

    if isinstance(family, list) is False:
        print("family argument is not a list")
        raise TypeError("family argument is not a list")

    if (isinstance(start, int) is False) or (isinstance(end, int) is False):
        print("start and end arguments must be integers")
        raise TypeError("start and end arguments must be integers")

    try:
        np.shape(family)
    except ValueError:
        raise ValueError("list elements must have the same size")

    print(f"My shape is: {np.shape(family)}")
    sliced = family[start:end]
    print(f"My new shape is: {np.shape(sliced)}")
    return sliced
