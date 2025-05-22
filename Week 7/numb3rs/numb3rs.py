import re
import sys


def main():
    ip=input("IPv4 Address: ")
    if validate(ip):
        print("True")
        sys.exit(0)
    else:
        print("False")
        sys.exit(1)


def validate(ip):

    if match := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        matches =  match.groups()
        if all(0 <= int(dats) <=254 for dats in matches):
            return True
        else:
            return False


    else:
        return False



if __name__ == "__main__":
    main()
