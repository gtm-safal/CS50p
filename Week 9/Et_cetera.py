# def meow(n: int) -> str:
#     return "meow\n" * n

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")

# import argparse

# phase = argparse.ArgumentParser(description = 'Meow like a cat')
# phase.add_argument("-n", default = 1, type = int)
# phase.add_argument("-m", default = 1, type = int)
# args = phase.parse_args()

# for _ in range(args.n*args.m):
#     print("meow")

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]

# print(total(*coins), "Knuts")

import cowsay
import pyttsx3

engine = pyttsx3.init()

this = input("What's this? ")
cowsay.cow(this)

engine. say(this)

engine. runAndWait()
