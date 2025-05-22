import validators

def main():
    mail = input("What's your mail address? ").strip()
    result = validators.email(mail)
    if result is True:
        print("Valid")

    else:
        print("Invalid")


if __name__ == "__main__":
    main()
