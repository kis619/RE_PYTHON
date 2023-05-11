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

    plt.title("Cute Racoon")
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


def crop_image(img_array, x, y, size):
    """
    Zooms on a given image
    args:
        img_array: ndarray - image as an ndarray
        x: int - x coordinate
        y: int - y coordinate
    """

    if not isinstance(x, int) or not isinstance(y, int):
        print("crop_image: Coordinates must be integers")
        return None

    if x < 0 or y < 0 or size < 0:
        print("crop_image: Coordinates must be positive")
        return None

    if x >= img_array.shape[0] or y >= img_array.shape[1]:
        print("crop_image: Coordinates must be smaller than the image size")
        return None

    if x + size >= img_array.shape[0] or y + size >= img_array.shape[1]:
        print("crop_image: the starting point",
              "+ size should not exceed the image")
        return None

    img_array = img_array[x:, y:, :1]
    print("The new image shape is:", img_array.shape)
    print(img_array)

    return img_array
