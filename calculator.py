# define the functions needed: add, sub, mul, div
# print options to the user
# ask for values
# call the function
# while loop to continue the function until the user wants to exit

def add(a, b):
    answer = a + b
    print(f"{a} + {b}  =  {answer}")


def sub(a, b):
    answer = a - b
    print(f" {a} - {b} = {answer}")


def mul(a, b):
    answer = a * b
    print(f"{a} * {b} = {answer}")


def div(a, b):
    answer = a / b
    print(f"{a} / {b} = {answer} ")


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("multiplication")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        div(a, b)

    elif choice == "E" or choice == "E":
        print("program ended")
        quit()
