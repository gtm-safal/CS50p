#Creating main function
def main():

    plate = input("Plate: ").strip() #Taking input

    #Calling function to check
    if is_valid(plate):
        print("Valid")

    else :
        print("Invalid")

#Creating function to valiadate
def is_valid(s):

    #Checking conditions
    if not 2 <= len(s) <=6:
        return False
    if not s[0:2].isalpha():
        return False
    if not s.isalnum():
        return False

    number_found = False
    for i in range(len(s)):
        if s[i].isdigit():
            if not number_found and s[i]=='0':
                return False
            number_found = True
        elif number_found:
            return False
    return True


if __name__ == "__main__":
    main()
