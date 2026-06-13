# Madlibs
# > Madlibs is a simple word game where the user 
# creates a story by picking random words.

# Introduces user
print("\nWelcome to Madlibs user\n")

# User picks random words
noun1 = input("Enter a noun (place): ")
noun2 = input("Enter a noun (living being): ")
adj1 = input("Enter an adjective (emotion): ")
adj2 = input("Enter an adjective: ")
verb1 = input("Enter a verb: ")

# Prints story
print(f'''
Here is your story:

I went to a {noun1} one evening.
When I got there, I saw a {noun2}.
It made me very {adj1}.
The {noun2} was {adj2}, causing it to {verb1}.
I turned around and went back home.
''')