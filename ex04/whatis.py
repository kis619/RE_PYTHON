from sys import argv, exit

# the script takes an integer and prints if it is odd or even

# check if script receive one argument
if (len(argv) != 2):
    print("AssertionError: more than one argument are provided")
    exit()

# check if argument is an integer
try:
    num = int(argv[1])
except:
    print("AssertionError: argument is not an integer")
    exit()

# dictionary type of numbers
type_number = {
    0: "Even",
    1: "Odd"
}

# print formated result
print(f"I'm {type_number[num % 2]}")
