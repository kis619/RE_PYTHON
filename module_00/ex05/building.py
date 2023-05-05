from sys import argv, exit


def main():
    """
       A program which pompts for a string and displays its character makeup
    """

    # get number of args
    argc = len(argv)

    # declare a variable to hold the input string
    input_text = ""

    # end programme if more than one arg was provided
    if (argc > 2):
        print("AssertionError: more than one argument are provided")
        exit()

    # assign input string if a single arg was provided
    if (argc == 2):
        input_text = argv[1]

    # prompt the user for input if they did not provide a string
    while (input_text == ""):
        try:
            input_text = input("What is the text to count? ")
        except EOFError:
            exit()

    chars_count = calculate_characters_count(input_text)
    display_char_count(chars_count)


def calculate_characters_count(text: str) -> dict:
    """
        Iterates over a string
        Creates a dict with pairs: char_type: count
        Returns the dict
    """

    chars_count = {
        "upper letters": 0,
        "lower letters": 0,
        "punctuation marks": 0,
        "spaces": 0,
        "digits": 0,
    }

    for ch in text:
        if ch.isupper():
            chars_count["upper letters"] += 1
        elif ch.islower():
            chars_count["lower letters"] += 1
        elif ch in r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""":
            chars_count["punctuation marks"] += 1
        elif ch.isdigit():
            chars_count["digits"] += 1
        elif ch.isspace():
            chars_count["spaces"] += 1

    return chars_count


def display_char_count(char_count: dict) -> None:
    """
        Args:
            char_count (dict): {type of char: count}

        Displays the sums of:
        - upper-case characters
        - lower-case characters
        - punctuation characters
        - spaces
        - digits

        Displays the count for each category as well
    """
    # print total sum of chars
    print(f"""The text contains {sum(char_count.values())} characters:""")

    # print separate categories
    [print(f"{val} {key}") for key, val in char_count.items()]


if __name__ == "__main__":
    main()
