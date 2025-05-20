import sys
def main():
    while True:
        fract = input("Fraction: ")
        try:
            percent = convert(fract)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    num, den = fraction.split("/")
    num, den = int(num), int(den)
    if den == 0:
        raise ZeroDivisionError
    if num > den :
        raise ValueError

    return round(num / den * 100)

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <=1 :
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
