from sys import exit, argv

if len(argv) == 2:

    file_name = argv[1].strip()
    file_extension = file_name.split(".")[-1]

    if file_extension != "py":
        print("Not a Python file")
        exit(1)
    else:
        try:
            line_counter = 0
            with open(f"{file_name}") as f:
                for line in f:
                    row = line.lstrip()
                    if row.startswith("#") or len(row) == 0:
                        continue
                    else:
                        line_counter += 1
                print(line_counter)
        except FileNotFoundError:
            raise

elif len(argv) == 1:
    print("Too few command-line arguments")
    exit(1)

else:
    print("Too many command-line arguments ")
    exit(1)
