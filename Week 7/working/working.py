import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) TO ([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$", s.upper())
    if not matches:
        raise ValueError

    startHour = int(matches.group(1))
    startMin = int(matches.group(2) or 0)
    startTime = matches.group(3)

    endHour = int(matches.group(4))
    endMin = int(matches.group(5) or 0)
    endTime = matches.group(6)

    if not 0 <= startMin < 60 or not 0 <= endMin < 60:
        raise ValueError

    if startTime == 'PM':
        if startHour != 12:
            startHour += 12
    else:
         if startHour == 12:
            startHour = 0

    if endTime == 'PM':
        if endHour != 12:
            endHour += 12
    else:
        if endHour == 12:
            endHour = o


    return f"{startHour:02}:{startMin:02} to {endHour:02}:{endMin:02}"




if __name__ == "__main__":
    main()
