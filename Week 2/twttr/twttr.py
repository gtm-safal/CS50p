#Creating main function
def main():

    txt = input("Input: ").strip()#Taking input

    #checking conditions
    for text in txt:
        if text.lower() in ['a', 'e', 'i', 'o', 'u']:
            txt = txt.replace(text, '')

    #Printing output
    print(f"Output: {txt}")


#Calling main function
main()
