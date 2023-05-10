import numpy as np
from load_image import load_image, crop_image
from matplotlib import pyplot as plt
import colored_traceback
colored_traceback.add_hook()


def rotate_image(image_array):
    """
    Rotates an image by 90 degrees clockwise

    args:
        image_array: ndarray - image as an ndarray

    Returns:
        ndarray: the rotated image as an ndarray
        None: if there is an error
    """
    if not isinstance(image_array, np.ndarray):
        print("Image must be a numpy array")
        return None

    new_arr = []
    new_row = []
    rows, cols = image_array.shape[:2]
    for i in range(cols):
        for j in range(rows):
            new_row.append(image_array[j][cols - i - 1])
        new_arr.append(new_row.copy()) 
        new_row.clear()
    new_arr = np.array(new_arr)
    print(new_arr.shape)
    print(new_arr)
    return new_arr


def main():
    """
    crops, paints gray and rotates an image
    
    """
    img = load_image("animal.jpeg")
    img = crop_image(img, 100, 100, 500)
    img = rotate_image(img)
    if img is not None:
        plt.imshow(img, cmap="gray")
        plt.show()


if __name__ == "__main__":
    main()
