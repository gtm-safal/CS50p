# names = {
#     "safal": "ilam",
#     "dahal": "jhapa",
#     "ghimire": "KTM",
#     "karna":"Biratnagar",
#     "thapa":"Sudurpaschim",
#     "limbu":"Itahari"
#     }

# with open("students.csv", "a") as file:
#     for name in names:
#         file.write(f"{name},{names[name]}\n")

# students =[]
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student ={ "name" : name, "house" : house}
#         students.append(student)

# # def get_name(student):
# #     return student["name"]

# for student in sorted(students, key=lambda student: student["name"]): #key = get_name):
#     print(f"{student['name']} is in {student['house']}")


# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name" :row["name"], "home" :row["home"]})

# for student in sorted(students, key=lambda student:student["name"]):
#     print(f"{student['name']} is from {student['home']}")


import csv

name = input("Whats ur name ? ")
home = input("wheres ur name? ")

with open("students.csv", "a") as file :
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

