import requests
import sys
import json

def main():
    if len(sys.argv)<2:
        sys.exit("Missing command-line argument ")
    try:
        coin = float(sys.argv[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        rate = o["bpi"]["USD"]["rate_float"]

    except requests.RequestException:
        sys.exit()

    print(f"${rate * coin:,}")

if __name__ == '__main__':
    main()
