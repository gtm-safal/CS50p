# A Tip Calculator

#defining main function
def main():

    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#Creating new dollars_to_float function
def dollars_to_float(d):
    d = float(d.replace("$", ""))
    return d

#Creating new percent_t0_float function
def percent_to_float(p):
    p = float(p.replace("%", ""))
    p /= 100
    return p

#Calling main function
main()
