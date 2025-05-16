#Creating main function

def main():
    # Taking input
    text = input("Enter a camel case string: ").strip()

    # Set of uppercase letters
    uppercase = {chr(i) for i in range(65, 91)}

    # Result string for snake case
    snake_case = ""

    # Loop through each character in the input string
    for char in text:
        if char in uppercase:
            snake_case += "_" + char.lower()
        else:
            snake_case += char

    print("Snake case:", snake_case)

main()
