from random import randint

def main():
    while True :
        try:
            level = int(input("Level : "))
            if (level <=  0):
                continue

            break
        except ValueError:
            continue
    num = randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if (guess <= 0):
                continue
            if(guess < num):
                print("Too Small!")
                raise ValueError
            elif( guess> num):
                print("Too large!")
                raise ValueError
            else:
                print("Just right!")
            break

        except ValueError:
            continue

if __name__ == '__main__':
    main()
