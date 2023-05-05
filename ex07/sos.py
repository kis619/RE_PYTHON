from sys import argv, exit

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"
}


def alnum_to_morse(text: str) -> str:
    """
    Args:
        text (string): text to convert to morse

    Returns:
        text (string): text converted to morse with spaces between each char
    """
    return " ".join([NESTED_MORSE.get(ch.upper()) for ch in text])


def validate_input(text: str) -> bool:
    """
        checks if the string contains only alphanumeric characters and spaces
    """
    for ch in argv[1]:
        if ch.upper() not in NESTED_MORSE:
            return False
    return True


def main():
    """
    Programme to convert a string to morse code
    """
    argc = len(argv)

    if argc != 2 or not validate_input(argv[1]):
        print("AssertionError: the arguments are bad")
        exit()

    print(alnum_to_morse(argv[1]))


if __name__ == "__main__":
    main()
