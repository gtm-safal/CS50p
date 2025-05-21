import sys
from PIL import Image, ImageOps

#Creating main function
def main():
    #Checking for files names
    if len(sys.argv) <3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) >3:
        sys.exit("Too many command-line arguments")

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    if not in_file.split(".")[-1].lower() == out_file.split(".")[-1].lower(): #Extensions should be same
        sys.exit("Input and Output have different extensions")

    ext = (".jpg", ".jpeg", ".png")
    if not in_file.endswith(ext): #Should have given extensions
        sys.exit("Invalid Input")


    try:
        with Image.open(in_file) as image:
            shirt = Image.open("shirt.png")
            resized_image = ImageOps.fit(image, shirt.size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
            resized_image.paste(shirt, (0,0), mask = shirt)
            resized_image.save(out_file)

    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
