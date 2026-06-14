# Unit Circle Countdown Timer
# > Countdown timer that converts each time point into radians,
# > as if the unit circle were a clock. It also gives the
# > principle angle for each time point for reference.

# Imports modules
import time
from fractions import Fraction

# Creates time variables
m = ""
s = ""

# Introduces user
print('''
Unit Circle Countdown Timer

This timer will convert the time point into radians, as if the
unit circle were a clock. For each time point, the principle angle
(the equivalent angle w/in one full rotation) will also be listed
in degrees (°).
''')

# Prompts user to pick a # of minutes until a valid choice is made
while type(m) != int:
    m = input("(xx):xx | Enter minutes (int, [0, 59]): ")

    # Checks that input is convertible to int
    try:
        x = int(m)
    except ValueError:
        print(f"{m} is not an integer w/in [0, 59]. Please try again.\n")
    else:
        # Checks that 0 < input < 59
        if int(m) < 0 or int(m) > 59:
            print(f"{m} is not an integer w/in [0, 59]. Please try again.\n")
        else:
            m = int(m)

# Prompts user to pick a # of seconds until a valid choice is made
while type(s) != int:
    s = input(f"{m:02}:(xx) | Enter seconds (integer, [0, 59]): ")

    # Checks that input is convertible to int
    try:
        int(s)
    except ValueError:
        print(f"{s} is not an integer w/in [0, 59]. Please try again.\n")
    else:
        # Checks that 0 < input < 59
        if int(s) < 0 or int(s) > 59:
            print(f"{s} is not an integer w/in [0, 59]. Please try again.\n")
        else:
            s = (m * 60) + int(s)
            print("")

# Creates variables corresponding to unit circle
position = Fraction(s, 30)
coord = (float(position) * 180) % 360

# Counts down to 0 from given time
for x in range(s, -1, -1):
    m = x // 60
    s = x % 60

    # Prints and calculates new values
    if position == 1:
        print(f"       π | {coord:03.0f}° | {m:02}:{s:02}")

        position = position - Fraction(1, 30)
        coord = (float(position) * 180) % 360
        time.sleep(1)
    else:
        print(f"{position:7}π | {coord:03.0f}° | {m:02}:{s:02}") 

        position = position - Fraction(1, 30)
        coord = (float(position) * 180) % 360
        time.sleep(1)

# Timer finished
print("\nTimes up!\n")
