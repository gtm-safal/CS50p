#A program to take input and output same input in lowercase

def main():

    #Taking input
    text = input("Enter the input: ").strip()

    #Obtaining lowercase of the input
    lwr_text = text.lower()

    #Showing output
    print(f"The lowercase of {text} is: {lwr_text}.")

main()
