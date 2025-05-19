import emoji

def main():
    str = input("Input: ")
    print(emoji.emojize(f"Output: {str}", language="alias"))

if __name__ == "__main__":
    main()
