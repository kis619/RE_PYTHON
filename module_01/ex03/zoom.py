from load_image import load_image
import matplotlib.pyplot as plt

import colored_traceback
colored_traceback.add_hook()


def zoom(path, x, y):
    """
    Zooms on a given image
    args:
        path: str - path to the image
        x: int - x coordinate
        y: int - y coordinate
    """

    if not isinstance(path, str):
        print("Path must be a string")
        return

    if not isinstance(x, int) or not isinstance(y, int):
        print("Coordinates must be integers")
        return None

    animal_image = load_image(path)
    if animal_image is None:
        print("No image found. Please double check the path")
        return None

    if x < 0 or y < 0:
        print("Coordinates must be positive")
        return None

    if x >= animal_image.shape[0] or y >= animal_image.shape[1]:
        print("Coordinates must be smaller than the image size")
        return None

    animal_image = animal_image[x:, y:, :1]
    print("The new image shape is:", animal_image.shape)
    print(animal_image)

    return animal_image


def main():
    """
    Main function
    Displays a zoomed image in grayscale
    """
    img = zoom("animal.jpeg", 100, 100)
    # img = zoom("noob-level.png", 100, 100)
    # img = zoom("normal-level.webp", 100, 100)
    plt.imshow(img, cmap="gray")  # should work
    plt.show()

    img = zoom("data/42AI.png", 100, 100)
    if img is not None:
        plt.imshow(img)  # error file not found
        plt.show()

    img = zoom("tests/tests00.py", 100, 100)
    if img is not None:
        plt.imshow(img)  # error unidentified image
        plt.show()

    img = zoom("animal.jpeg", 10000, 100000)
    if img is not None:
        # error coordinates must be smaller than the image size
        plt.imshow(img)
        plt.show()

    img = zoom("animal.jpeg", -100, 100)
    if img is not None:
        plt.imshow(img)  # error coordinates must be positive
        plt.show()


if __name__ == "__main__":
    main()
