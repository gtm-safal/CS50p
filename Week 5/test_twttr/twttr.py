def main():
    str = input("Input: ").strip()#Taking input
    print(shorten(str))


def shorten(word):
    result =""
    #checking conditions
    for char in word:
        if char.lower() not in 'aeiou':
            result += char

    return result

if __name__ == "__main__":
    main()
