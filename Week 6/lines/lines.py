import sys

#Creating main function
def main():

    #Checking gor command-line argument
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a python file")

    print(count_lines(filename))

def count_lines(filename):
    try:
        with open(filename, "r") as files:
            lines = files.readlines()
            code_lines = []

            for line in lines:
                if line.strip() and not line.strip().startswith("#"): # .strip() for removing whitespaces and another condition is to check comments
                    code_lines.append(line)

            return len(code_lines)

    except FileNotFoundError:
        sys.exit("Error: File does not exist.")


if __name__ == "__main__":
    main()
