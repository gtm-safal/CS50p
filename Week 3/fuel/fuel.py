#Creating main function
def main():

    #using infinite loop unless error is not found
    while True:
        fract = input("Fraction: ")#Taking input
        try:
            num, den = fract.split("/")
            num = int(num)
            den = int(den)
            if(num / den >1):#Checking so than denominator is always equal or greater then numerator
                continue
            check(num, den)
            break

        except (ValueError, ZeroDivisionError) :
            pass

def check(a, b):
    per = round(a / b *100) #Rounding up to nearest int

    #checking conditions and printing as per instruction
    if(per >= 99):
        print("F")
    elif(per<=1):
        print("E")
    else:
        print(f"{per}%")

main()
