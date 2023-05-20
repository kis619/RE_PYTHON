import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import UnidentifiedImageError


def load_image(path):
    """
    Loads an image from a given path prints its dimension
    and returns an ndarray

    args:
        path: str - path to the image

    Returns:
        ndarray: the image as an ndarray
        None: if there is an error
    """

    if not isinstance(path, str):
        print("Path must be a string")
        return None

    plt.xlabel("width")
    plt.ylabel("height")

    try:
        animal_image = mpimg.imread(path)
    except FileNotFoundError:
        print("load_image: File not found")
        return None
    except UnidentifiedImageError:
        print("load_image: Unidentified image")
        return None

    print("The image shape is:", animal_image.shape)
    print(animal_image)
    return animal_image
