import re

# email = input("Email? ").strip()

# if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|edu)$", email, re.IGNORECASE):
#     print("valid")
# else:
#     print("Invalid")

# name = input("Name? ")

# if matches := re.search("^(.+), ?(.+)$", name):
#     name = matches.groups(2) + " " + matches.groups(1)

# print(f"Hello, {name}")


url = input("URL: ").strip()
matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)" ,  url, re.IGNORECASE)
if matches:

    print(matches.group(1))
me = 'SaFal Gautam'
print(me)
