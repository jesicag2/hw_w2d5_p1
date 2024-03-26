#HW1_P1: The Calculator App

# Task 1: Create functions for each arithmetic operation.

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: Sorry can not divide by 0!"
    else:
        return x / y


# Task 2: Implement user input to receive numbers and an operation choice.

while True:
    problem = input("What mathematical operation would you like to complete? (addition/substraction/multilication/division) ")
    if problem in ("addition", "subtraction", "multiplication", "division"):
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        if problem == "addition":
            total = add(x, y)
        elif problem == "subtraction":
            total = sub(x, y)
        elif problem == "multiplication":
            total = multiplication(x, y)
        elif problem == "division":
            total = division(x, y)
        print(f"The {problem} is equal to: {total}")
        break
    else:
        print("Please enter a valid mathematical operation.")


# Task 3: Ensure your program can handle division by zero and other potential errors.

while True:
    problem = input("What mathematical operation would you like to complete? (addition/substraction/multilication/division) ")
    if problem in ("addition", "subtraction", "multiplication", "division"):
        while True:
            try:
                x = float(input("Enter the first number: "))
                y = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Opps, seems you have not inputed a valid number.")
        if problem == "addition":
            total = add(x, y)
        elif problem == "subtraction":
            total = sub(x, y)
        elif problem == "multiplication":
            total = multiplication(x, y)
        elif problem == "division":
            total = division(x, y)
        print(f"The {problem} is equal to: {total}")
        break
    else:
        print("Please enter a valid mathematical operation.")
