from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.ndarray | None:
    if not isinstance(path, str):
        print("Path must be a string")
        return None

    try:
        img = Image.open(path)
    except FileNotFoundError:
        print(f"File at path {path} not found")
        return None
    except UnidentifiedImageError:
        print("Unidentified image")
        return None

    format = img.format
    print("Image format:", format)
    format_to_pixel_array_funcitons = {
        "PNG": lambda img: np.array(img.convert('RGBA')),
        "JPEG": lambda img: np.array(img),
    }
    if format not in format_to_pixel_array_funcitons:
        print("Unsupported file format")
        img.close()
        return None
    pixel_array = format_to_pixel_array_funcitons[format](img)
    img.close()
    print("The shape of the image is:", pixel_array.shape)
    return pixel_array
