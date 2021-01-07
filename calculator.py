# This function adds two numbers
def add(num1, num2):
    return num1 + num2


# This function subtracts two numbers
def subtract(num1, num2):
    return num1 - num2


# This function divide two numbers
def divide(num1, num2):
    return num1 / num2


# This function multiplies two numbers
def multiply(num1, num2):
    return num1 * num2


def calculator():
    num1 = 0.0
    num2 = 0.0
    operation = ""
    while True:
        print("Welcome to Debbie's Calculator")
        print("\n")
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("Please enter a valid number.")

        print("""
        \nEnter the desired operator:
        0 - Add
        1 - Subtract
        2 - Divide
        3 - Multiply
        """)
        operation = input(">")
        if operation == "0":
            print(f"{num1} + {num2} = {add(num1, num2)}")
            break
        elif operation == "1":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
            break
        elif operation == "2":
            print(f"{num1} / {num2} = {divide(num1, num2)}")
            break
        elif operation == "3":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
            break
        else:
            print("Not a valid entry. Please type again!")


calculator()

