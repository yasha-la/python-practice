# Unit Temperature Converter (°C/°F)
# > Converts values from lb to kg or vice versa

# Creates initial variables
temp = ""
unit = ""

# Introduces user
print("\nUnit Temperature Converter (°C/°F)\n")

# Prompts user to pick a temperature until a valid choice is made
while type(temp) != float:
    temp = input("Enter temperature value: ")

    # Checks that input is convertible to float
    try:
        float(temp)
    except ValueError:
        print("Invalid value. Please try again.\n")
    else:
        temp = float(temp)

# Prompts user to pick a unit until a valid choice is made
while unit not in ("C","c","F","f"):
    unit = input("Enter units (c/f): ")

    # Checks for valid unit
    if unit not in ("C","c","F","f"):
        print("Invalid unit. Please try again.\n")

# Calculates answer
if unit in ("C","c"):
    unit = "°C"
    answer_temp = 1.8 * temp + 32
    answer_unit = "°F"
else:
    unit = "°F"
    answer_temp =(temp - 32) / 1.8
    answer_unit = "°C"

# Prints answer
print(f"\n{round(temp, 2)} {unit} = "
      f"{round(answer_temp, 2)} {answer_unit}\n")