#Creating main function
def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        try:

            date = input("Date: ").strip()

            if "/" in date:
                parts = date.split("/")
                if len(parts) != 3:
                    raise ValueError
                month, day, year = map(int, parts)

            else:
                if "," in date:
                    date = date.replace(",", "")
                    parts = date.split()
                    if len(parts) != 3:
                        raise ValueError
                else:
                    raise KeyError

                month = parts[0]
                day = int(parts[1])
                year = int(parts[2])

                if month in months:
                    month = months.index(month) + 1
                else:
                    raise ValueError

            if not (1 <= month <= 12) or not (1 <= day <= 31):
                raise ValueError

            # Print the date in YYYY-MM-DD format
            print(f"{year}-{month:02}-{day:02}")
            break

        except ValueError:
            continue
        except KeyError:
            break
main()
