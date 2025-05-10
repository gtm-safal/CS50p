#creating main function

def main ():

    #Taking input
    curr_time = input ("What time is it now? ")

    #calling function
    data = convert(curr_time)

    #checking conditions
    if 7 <= data <= 8 :
        print("breakfast time")

    elif 12 <= data <= 13 :
        print("Lunch time")

    elif 18 <= data <=19:
        print("Dinner time")

#Defining convert function
def convert(time):

    first, last = time.split(':')
    last = float(last) / 60
    return ( float(first) + last)

if __name__ == "__main__":
    main()
