from load_image import load_image
import matplotlib.pyplot as plt


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
        return

    animal_image = load_image(path)
    if animal_image is None:
        print("No image found. Please double check the path")
        return

    if x < 0 or y < 0:
        print("Coordinates must be positive")
        return

    if x >= animal_image.shape[0] or y >= animal_image.shape[1]:
        print("Coordinates must be smaller than the image size")
        return

    animal_image = animal_image[x:, y:]
    print("The new image shape is:", animal_image.shape)
    print(animal_image)
    plt.imshow(animal_image)
    plt.show()


def main():
    zoom("animal.jpeg", 100, 100)  # should work
    zoom("data/42AI.png", 100, 100)  # error file not found
    zoom("tests/tests00.py", 100, 100)  # error unidentified image
    zoom("animal.jpeg", "100", 100)  # error coordinates must be integers
    zoom("animal.jpeg", -100, 100)  # error coordinates must be positive


if __name__ == "__main__":
    main()
