import csv
from tabulate import tabulate
from sys import exit, argv

if len(argv) == 1:
    print("Too few command-line arguments")
    exit(1)
elif len(argv) > 2:
    print("Too many command-line arguments")
    exit(1)
else:
    file_name = argv[1]
    if file_name.split(".")[-1] == "csv":
        try:
            with open(file_name, "r") as f:
                file_content = csv.DictReader(f)
                print(tabulate(file_content, headers="keys", tablefmt="grid"))
        except FileNotFoundError as error:
            print(error)
            exit(1)
    else:
        print("Not a CSV file")
        exit(1)
