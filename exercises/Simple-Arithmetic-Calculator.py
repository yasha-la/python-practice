# Simple Arithmetic Calculator
# > Solves simple 2-value arithmetic problems.

# Creates variables
operator = ""
num1 = ""
num2 = ""

# Introduces user
print("\nSimple Arithmetic Calculator\n")

# Prompts user to pick an operator until a valid choice is made
while operator not in ("+","-","*","/"):
    operator = input("Enter operator (+, -, *, /): ")

    # Checks for valid operator
    if operator not in ("+","-","*","/"):
        print(f"{operator} is not a valid operator. Please try again.\n")

# Prompts user to pick 2 values until a valid choice is made
while type(num1) != float and type(num2) != float:
    num1 = input("Enter 1st number: ")
    num2 = input("Enter 2nd number: ")

    # Checks that input is convertible to float
    try:
        float(num1)
        float(num2)
    except ValueError:
        print("This is not a valid pair of values. Please try again.\n")
    else:
        num1 = float(num1)
        num2 = float(num2)

# Calculates and prints answer
if operator == "+":
    print(f"\n{round(num1, 3)} {operator} "
          f"{round(num2, 3)} = {round((num1 + num2), 3)}\n")
elif operator == "-":
    print(f"\n{round(num1, 3)} {operator} "
          f"{round(num2, 3)} = {round((num1 - num2), 3)}\n")
elif operator == "*":
    print(f"\n{round(num1, 3)} {operator} "
          f"{round(num2, 3)} = {round((num1 * num2), 3)}\n")
else:
    print(f"\n{round(num1, 3)} {operator} "
          f"{round(num2, 3)} = {round((num1 / num2), 3)}\n")
