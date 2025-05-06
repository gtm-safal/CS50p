"""
To create a function to replace :) with 🙂 and :( with 🙁
"""

#Creating a function
def convert(data):
        data = data.replace (":)", "🙂").replace (":(", "🙁")
        return data

#Creating main function
def main():
    str_in = input ("Enter the string: ")
    #Calling convert function
    str_out = convert(str_in)
    print(f"The '{str_in}' is converted to '{str_out}'.")

#Calling main function
main()
