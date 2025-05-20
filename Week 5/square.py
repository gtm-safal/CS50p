def main():
    n = float(input("?"))
    sq = square(n)
    print(f"{round(sq, 2)}")

def square(n):
    return n*n
if __name__ == "__main__":
    main()
