# n=0
# while ( n<3):
#     print("meow1")
#     n+=1

# for i in range (3):#function
#     print("meow")

#print ("meow\n" *3, end = "")

# students = [ 'ram', 'shyam', 'hari']
# for i in students:
#     print(i)

# teachers = {
#     'name' : 'Ram',
#     'sub' : 'comp',
#     'time' : 'half',
# }
# print(teachers['name'])
# for i in teachers:
#     print(i, teachers[i], sep = ': ')


# workers = [
#     {'name':'ram', 'age':'41', 'sal':'5k'},
#     {'name':'shyam', 'age':'40', 'sal':'4.5k'},
#     {'name':'hari', 'age':'39', 'sal':'4k'},
#     {'name':'puttish', 'age':'38', 'sal':'3.5k'}

# ]
# for workers in workers:
#     print(workers['name'], workers['age'], workers['sal'], sep=',')

def main():
    print_square(3)




def print_square(size):
    for i in range(size):
        # for j in range(size):
        #     print("# ", end="")
        print_row(size)
        # print()

def print_row(row):
    print("# " * row)


main()
