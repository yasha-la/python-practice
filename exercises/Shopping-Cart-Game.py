# Shopping Cart Game

# Game description below in 'Introduces user' section

import random

# Creates variables
cart = []
budget = 100.0
prices = []
total = 0.0

# Introduces user
print('''
Shopping Cart Game

Each item will be priced randomly from 0-100$.
Goal: Try to buy as many items as you can without
spending more than your budget.

Budget: 100$
''')

# Allows user to pick items until they quit
while True:
    # User picks item
    item = input(f"Enter an item to buy ({len(cart)} items in cart, Q to quit): ")
    if item.lower() == "q":
        break
    else:
        # Adds item to shopping cart
        cart.append(item)

        # Assigns random price to item and adds to total
        price = round(random.uniform(0,100), 2)
        prices.append(price)
        total += price

print("\n----YOUR CART----")

# Lists items picked with each respective price
for item in cart:
    print(f"{prices[cart.index(item)]:6.2f}$ | {item} ")

# Prints final total
print(f"-----------------\nTOTAL SPENT: {total:.2f}$")

# Determines if user was successful or not and assigns a score
if total > budget:
    print("\nFailure!")
else:
    print(f"\nSuccess! Score: {len(cart):.2f} ")

