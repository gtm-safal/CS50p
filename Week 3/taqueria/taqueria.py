# Main Function to run the ordering process
def main():

    # Menu with items and their prices
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0.00  # Initialize the total cost

    try:
        while True:
            # Prompt the user for an item
            item = input("Item: ").strip().title()

            if item in menu:
                total += menu[item]  # Add the price of the item to the total
                print(f"Total: ${total:.2f}")  # Print the total cost, formatted to two decimal places
            else:
                pass

    except EOFError:  # Handle end-of-file (Ctrl-D) error
        print(f"Total: ${total:.2f}")  # Final total after user inputs Ctrl-D

main()
