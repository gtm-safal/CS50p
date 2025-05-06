# lecture 0
# print("Hello world")

# Ask for users name
name = input("What's your name? ")

# Say hello to user
print("Hello,", name)
print(f"Hello, {name}.")


# Normally Python's print function ends with \n but we can change it.
print("hello")
print("world")

print("hello", end="")
print("world")
# we can use this for seperation between parameters as well by using sep=""


# to print " in display
print('Hello "World"')
print("hello \"World\"")


name = name.strip()
# To remove unwanted whitespaces from the input in both sides

name = name.capitalize()
# To uppercase the first letter in of first word

name = name.title()
# To uppercase first letter of all words

print(f"Hello, {name}.")

name = name.strip().title()
# To remove whitespace and capatialize the data

print(f"Hello, {name}.")

# IN-SHORT
caste = input("What's your caste? ").strip().title()
print(f"Hello, {caste}.")

# split user's name into first and last name
first, last = name.split(" ")
print(f"Hello, {first}.")
print(f"Hello, mr. {last}.")

x = float(input(" x = "))
y = float(input(" y = "))
z = round(x + y, 3)  # Rounding up to 3 digits
# print(f"{z:.3f}")    Rounding up to 3 digits
print(f"{z:,}")  # To use comma as seperator on as hundreds, thousands...
