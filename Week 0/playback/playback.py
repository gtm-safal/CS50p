#A code to replace space ' ' with dots '...'

#creating main function
def main():

    #Taking input
    text = input ("Enter any text : ").strip()

    #Replacing space
    mod_text = text.replace(" ", "...")

    #Output the modified text
    print(f"The modified output of '{text}' is : {mod_text}")

#Calling main function
main()
