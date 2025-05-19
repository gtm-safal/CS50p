# from random import choice
# print(choice(['Heads', 'Tails']))


# import random
# print(random.choice(['Heads', 'Tails']))
# print(random.randint(0, 100))
# cards = ['A', 'J', 'Q', 'K']
# random.shuffle(cards)
# for i in cards:
#     print (i, end = "\n")


# import statistics
# a = random.randint(0,100)
# b = random.randint(0,120)
# print(f"mean of {a} and {b} is {statistics.mean([a, b])}" )


# import sys

# if len(sys.argv) < 2:
#     sys.exit("Few arguments")
# print("hello my name is ", end="")

# for arg in sys.argv[1:]:
#     print(arg, end="\t")


# import cowsay
# import sys

# if len(sys.argv) ==2:
#     cowsay.cow("hi " +sys.argv[1])


import requests
import sys
import json

if len(sys.argv)!= 2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
o = response.json()
for result in o["results"]:
    print(result["trackName"])
# print(json.dumps(response.json(), indent =2))
