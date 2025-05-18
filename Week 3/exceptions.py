def get_int(prompt):

    while True:
        try:
            return int(input(prompt))

        except ValueError:
            pass

        # else:
        #     break / return x


def main():
    x = get_int("What's x ?\n")
    print(f"x is {x}")


main()
