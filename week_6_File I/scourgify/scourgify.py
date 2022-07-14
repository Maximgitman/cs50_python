import csv
from sys import exit, argv
from tabulate import tabulate


if len(argv) == 3:
    before = argv[1]
    after = argv[2]

    try:
        all_dict = []
        with open(before, "r") as f:
            content = csv.DictReader(f)
            for row in content:
                row_dict = {}
                last, first = [x.strip() for x in row["name"].split(",")]
                house = row["house"]
                row_dict["first"] = first
                row_dict["last"] = last
                row_dict["house"] = house
                all_dict.append(row_dict)

        with open(after, "w") as f:
            writer = csv.DictWriter(f, fieldnames=all_dict[0].keys())
            writer.writeheader()
            for row in all_dict:
                writer.writerow(row)

    except FileNotFoundError as error:
        print(error)
        exit(1)

elif len(argv) <= 2:
    print("Too few command-line arguments")
    exit(1)

else:
    print("Too many command-line arguments")
    exit(1)
