import sys
from pyfiglet import Figlet
figlet = Figlet()

#Creating main function
def main():

    if len(sys.argv) == 1:
        user_input = input("Input: ")
        print(figlet.renderText(user_input))

    # Checking `-f` or `--font`
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        try:
            figlet.setFont(font=sys.argv[2])  # Set font
            user_input = input("Input: ")
            print(figlet.renderText(user_input))
        except:
            print("Error: Invalid font name.")
            sys.exit(1)

    # Exit immediately
    else:
        print("Invalid usage")
        sys.exit(1)

if __name__ == "__main__":
    main()
