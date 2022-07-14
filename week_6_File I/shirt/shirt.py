import PIL.Image
from PIL import Image, ImageOps
from sys import exit, argv

# Permitted extension for Image
permitted_extension = ["jpg", "png"]

# Check if there are fewer arguments than needed
if len(argv) < 3:
    print("Too few command-line arguments")
    exit(1)

# Check if there are more arguments than needed
elif len(argv) > 3:
    print("Too many command-line arguments")
    exit(1)

# Let's start
else:
    # Read file name from argument
    before = argv[1]
    after = argv[2]

    before_extension = before.split(".")[-1]
    after_extension = after.split(".")[-1]

    # Check if extension is in permitted
    if before_extension in permitted_extension and after_extension in permitted_extension:
        # Check if they have the same file extension
        if before_extension == after_extension:
            try:
                shirt = Image.open("shirt.png")
                img = Image.open(before)
                img = ImageOps.fit(img, size=shirt.size)
                img.paste(shirt, shirt)
                img.save(after)
            except FileNotFoundError:
                print("Input does not exist")
                exit(1)
        else:
            print("Input and output have different extensions")
            exit(1)
    else:
        print("Invalid input")
        exit(1)
