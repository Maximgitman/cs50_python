from pyfiglet import Figlet
from sys import exit, argv
import random


flags = ["-f", "--font"]
f = Figlet()
fonts = f.getFonts()

if len(argv) == 3 and argv[1] in flags and argv[2] in fonts:
    text = input("Input: ")
    f.setFont(font=argv[2])
    print("Output:\n", f.renderText(text))

elif len(argv) == 1:
    text = input("Input: ")
    f.setFont(font=random.choice(fonts))
    print("Output:\n", f.renderText(text))

else:
    exit("Invalid usage")
