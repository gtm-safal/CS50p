import sys
import csv

#Creating main function
def main():
    #Checking for files names
    if len(sys.argv) <3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) >3:
        sys.exit("Too many command-line arguments")
    in_file = sys.argv[1]
    out_file = sys.argv[2]

    try:
        with open(in_file) as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                data.append(row) #reading data from first file and saving in a dict


    except FileNotFoundError:
        sys.exit(f"Could not read {in_file}.")

    with open(out_file, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"]) #writing in second file
            writer.writeheader()

            for names in data:
                last, first = names["name"].split(",") #Splitting full name into first anf last as given condtn
                writer.writerow({"first": first.strip(), "last": last.strip(), "house": names["house"]})

if __name__ == "__main__":
    main()
