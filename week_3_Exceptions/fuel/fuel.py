def main():
    fullness = get_fruction()
    if fullness <= 1:
        print("E")
    elif fullness >= 99:
        print("F")
    else:
        print(f"{fullness}%")


def get_fruction():
    while True:
        try:
            exist, trank = input("Fruction: ").split("/")
            percent = round(int(exist) / int(trank) * 100)
            if int(exist) > int(trank):
                continue
        except (ZeroDivisionError, ValueError):
            pass
        else:
            return percent


if __name__=="__main__":
    main()