def main():

    x = int(input(" x = "))
    if is_even(x):
        print("Its even")
    else:
        print("Its odd")

def is_even(n):

    # return True if n % 2 == 0 else False
    return n % 2 == 0
main()

