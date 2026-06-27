# Fruit Stand

# Program that allows user to 'purchase' what they want to
# off of the menu below

# Creates menu
menu = {"apple": 0.20,
        "orange":0.25,
        "banana": 0.30,
        "mango": 0.45,
        "watermelon": 1.00,
        "kiwi": 0.25}

# Creates cart and total variable
cart = {}
total = 0

# Introduces user and prints menu
print("\nFruit Stand\n\n--------MENU--------")
for key, value in menu.items():
    print(f"{key}: {value:.2f}$")
print("--------------------")

# Prompts user to pick which items and how many
while True:
    pick = input(f"\n{len(cart)} item/s in cart. Select an item (f to finish): ").lower()

    if pick == "f":
        break
    elif menu.get(pick) == None:
        print("That is not on the menu. Please try again.")
    else:
        quantity = input(f"How many {pick}s?: ")

        # Checks if quantity is an integer
        try: 
            quantity = int(quantity)
        except ValueError:
            print(f"{quantity} is not a valid quantity. Please try again.")
        else:
            cart.update({pick: quantity})
            total += menu.get(pick) * quantity

# Prints cart and total
print("\n----YOUR CART----")

for key, value in cart.items():
    print(f"{key} ({value})")

print(f"-----------------\nTotal: {total:.2f}$\n")
        