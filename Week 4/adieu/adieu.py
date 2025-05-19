import inflect

p = inflect.engine()  # Initialize the inflect engine

names = []

def main():


    try:
        while True:
            name = input("Name :")
            if name:
                names.append(name)
    except EOFError:
        pass

    # Join method to format the names
    names_str = p.join(names)  # This will join the names with commas and 'and' before the last name
    print(f"Adieu, adieu, to {names_str}")

if __name__ == '__main__':
    main()
