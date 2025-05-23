import sys
import inflect
import datetime



class Date:

    def __init__(self, datee):

        try:
            year, month, day = datee.split('-')
            self.year = int(year)
            self.month = int(month)
            self.day = int(day)
            self.date = datetime.datetime(self.year, self.month, self.day)

        except ValueError:
            sys.exit("Invalid date")

    def __str__(self):
        return f"{self.year}/{self.month:02}/{self.day:02}"

    def __sub__(self, datee):

        if self.date < datee.date:
            sys.exit("Invalid date")

        delta = self.date - datee.date
        return delta.days*1440

def main():
    datee = input("Date of Birth: ")
    dobDate = Date(datee)
    today = Date(str(date.today()))

    minDiff = today - dobDate

    print(inflect.engine().number_to_words(minDiff, andword="").capitalize(), "minutes")


if __name__ == "__main__":
    main()
