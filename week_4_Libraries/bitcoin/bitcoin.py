from selectors import EpollSelector
from sys import argv, exit
import requests

if len(argv) == 1:
    print("Missing command-line argument")
elif type(argv[2]) == str:
    print("Command-line argument is not a number")
else:
    quantity_bitcoin = argv[2]
