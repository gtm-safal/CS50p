#A program to take mass of an object as mass and calculate enery possesed in Joules

#Creating main function
def main():
    m = int( input("Mass of body in kg: "))
    c = 3 * 10 **8
    E = m * c**2
    print(f"Energy is: {E} J.")

#Calling main function
main()
