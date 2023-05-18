from sys import argv, exit

# the script takes an integer and prints if it is odd or even

# check if script receives more than 1 argument
if (len(argv) > 2):
    print("AssertionError: more than one argument is provided")
    exit()

# check if script received a argument
if (len(argv) < 2):
    # print("AssertionError: more than one argument is provided")
    exit()

# check if argument is an integer
try:
    num = int(argv[1])
except (ValueError, AssertionError):
    print("AssertionError: argument is not an integer")
    exit()

# dictionary type of numbers
type_number = {
    0: "Even",
    1: "Odd"
}

# print formated result
print(f"I'm {type_number[num % 2]}")
