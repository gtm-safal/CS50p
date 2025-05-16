#Creating main function

def main():

    rem = 50
    while(rem > 0):
        #Getting input
        coin = int(input("Insert Coin: "))

        if coin in [5, 10, 25] : #Checking condition
            rem -= coin

            if rem > 0:
                print(f"Amount Due: {rem}")
                
            else :
                change_owe = abs(rem)
                print(f"Change Owed: {change_owe}")

        else:
            print("Amount Due: 50")
            break

#Calling main function
main()
