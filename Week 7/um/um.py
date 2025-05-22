import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\bum\b", s.lower())
    if matches:
        return len(matches)

if __name__ == "__main__":
    main()
