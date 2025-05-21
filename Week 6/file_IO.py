# names = []

# for _ in range(3):
#     names.append(input("Whats ur name? "))

# for name in sorted(names):
#     print(name)


# name = input("Whats ur name? ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("names.txt", "r") as file:
#     # name = file.readlines()
#     for names in sorted(file):
#         print("Hello, ", names.rstrip())

with open("names.txt", "r") as file:
    name = file.readlines()

for names in sorted(name, reverse=True):
    print("Hello, ", names.rstrip())
