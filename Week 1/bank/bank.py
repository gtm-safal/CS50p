#Creating main function

def main():

    greeting = input("Greeting: ").strip().lower()

    #Checking conditions

    if greeting.startswith('hello'):
        print("$0")

    elif greeting.startswith('h'):
        print("$20")

    else:
        print("$100")

#Calling main function

main()

