from ft_filter import ft_filter
from sys import argv, exit


def main():

    # getting number or argc
    argc = len(argv)

    # checking if exactly two arguments
    if (argc != 3):
        print("AssertionError: the arguments are bad")
        exit()

    # quit if second arg cannot be an integer
    try:
        min_len = int(argv[argc - 1]) + 1
    except (...):
        print("AssertionError: the arguments are bad")
        exit()

    # list of filtered words which contain only alphanum chars
    words = (list(ft_filter(lambda word: word.isalnum(), argv[1].split())))

    # print only words bigger than the given len
    print([word for word in words if len(word) >= min_len])


if __name__ == "__main__":
    main()
