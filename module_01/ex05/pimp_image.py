import numpy as np
from matplotlib import pyplot as plt
from load_image import load_image


def get_max_val(array):
    """
    description: gets the max value of an array element
    args: array (np.array): array
    throws: ValueError if the array dtype is not numeric
    """
    if np.issubdtype(array.dtype, np.integer):
        max_val = np.iinfo(array.dtype).max
    elif np.issubdtype(array.dtype, np.floating):
        max_val = np.finfo(array.dtype).max
    else:
        raise ValueError("Array dtype must be numeric.")
    return max_val


def ft_invert(array) -> np.array:
    """receives an image and inverts it

    args:
        array (np.array): image

    returns:
        np.array: inverted image
    """

    if len(array.shape) != 3 or array.shape[2] < 3:
        print("ft_grey: image format is not supported")
        return None

    # added this for png images because they be havng float values
    array = array.astype(np.uint8)
    max_val = get_max_val(array)
    inverted_image = max_val - array

    return inverted_image


def ft_red(array) -> np.array:
    """receives an image and makes it red

    Args:
        array (np.array): image

    Returns:
        np.array: red image
    """

    if len(array.shape) != 3 or array.shape[2] < 3:
        print("ft_grey: image format is not supported")
        return None

    red = array.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    return red


def ft_green(array) -> np.array:
    """receives an image and makes it green

    Args:
        array (np.array): image

    Returns:
        np.array: green image
    """

    if len(array.shape) != 3 or array.shape[2] < 3:
        print("ft_grey: image format is not supported")
        return None

    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    return green


def ft_blue(array) -> np.array:
    """receives an image and makes it blue

    Args:
        array (np.array): image

    Returns:
        np.array: blue image
    """

    if len(array.shape) != 3 or array.shape[2] < 3:
        print("ft_grey: image format is not supported")
        return None

    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    return blue


def ft_grey(array) -> np.array:
    """
    receives an image and makes it grey
    returns:
        np.array: grey image
        none: if the image format is not supported
    """
    if len(array.shape) != 3 or array.shape[2] < 3:
        print("ft_grey: image format is not supported")
        return None

    # computing the grayscale values of each pixel
    # eaach pixel from the array is represented by 3 values (RGB)
    # r is multiplied by 0.21 g by 0.72 and b by 0.07
    # then we add them up
    # shape of the original array is (height, width, 3)
    # shape of the gray_vals array is (height, width)
    gray_vals = np.dot(array[..., :3], [0.21, 0.72, 0.07])

    # Set the RGB values of each pixel to the grayscale intensity value
    # gray_vals[..., None] has shape (height, width, 1)
    gray_arr = array.copy()
    gray_arr[..., :3] = gray_vals[..., None]
    # same as:
    # gray_arr = array.copy()
    # gray_arr[..., 0] = gray_vals
    # gray_arr[..., 1] = gray_vals
    # gray_arr[..., 2] = gray_vals

    return gray_arr


def main():
    image = load_image("landscape.jpg")
    # image = load_image("noob-level.png")
    # image = load_image("normal-level.webp")
    pimped_image = ft_invert(image)
    # pimped_image = ft_red(image)
    # pimped_image = ft_green(image)
    # pimped_image = ft_blue(image)
    # pimped_image = ft_grey(image)
    if pimped_image is None:
        return
    plt.imshow(pimped_image)
    plt.show()


if __name__ == "__main__":
    main()
