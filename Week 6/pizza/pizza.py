import sys
import csv
from tabulate import tabulate

#Creating main function
def main():

    #Checking command-line argument
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a csv file")

    try:
        with open(filename, "r") as files:
            reader = csv.DictReader(files) #opening the file and reading data in it in reader file
            table =[row for row in reader] #storing data fromm file in a list

            print(tabulate(table, headers = "keys", tablefmt = "grid")) #printing in table form

    except FileNotFoundError:
        sys.exit("File does not exist.")


if __name__ == "__main__":
    main()
