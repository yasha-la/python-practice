# Compound Interest Calculator
# > Calculates interest accrued given a principle,
#   interest rate, and time

# Creates variables
principle = ""
interest = ""
time = ""

# Introduces user
print("\nCompound Interest Calculator\n")

# Prompts user to pick a principle value until a valid choice
# (number >= 0) is made
while not type(principle) == float:
    principle = input("Enter principle value ($): ")

    # Checks that input is convertible to float
    try:
        float(principle)
    except ValueError:
        print(f"{principle} is not a valid value. Please try again.\n")
    else:
        principle = float(principle)

        # Tests if input < 0
        if principle < 0:
            print("Principle cannot be < 0. Please try again.\n")
            principle = ""

# Prompts user to pick an interest rate until a valid choice
# (number >= 0) is made
while not type(interest) == float:
    interest = input("Enter interest rate (%): ")

    # Checks that input is convertible to float
    try:
        float(interest)
    except ValueError:
        print(f"{interest} is not a valid value. Please try again.\n")
    else:
        interest = float(interest)

        # Tests if input < 0
        if interest < 0:
            print("Interest rate cannot be < 0. Please try again.\n")
            interest = ""

# Prompts user to pick a time until a valid choice
# (number >= 0) is made
while not type(time) == float:
    time = input("Enter time (yr/s): ")

    # Checks that input is convertible to float
    try:
        float(time)
    except ValueError:
        print(f"{time} is not a valid value. Please try again.\n")
    else:
        time = float(time)

        # Tests if input < 0
        if time < 0:
            print("Time cannot be < 0. Please try again.\n")
            time = ""

# Calculates and prints total balance
total = principle * pow((1 + interest / 100), time)
print (f"\nBalance after {time} yr/s: {total:.2f}$\n")


    
