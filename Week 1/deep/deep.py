#Creating main function
def main():

    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip()

    correct_answer = ['42', 'forty-two', 'forty two']
    if answer.lower() in correct_answer :
        print("Yes")

    else:
        print("No")

#Calling main function
main()
