from signal import raise_signal
from unittest import result


def main():
    fruction = input("Fraction: ")
    percantage = convert(fruction)
    actual_gauge = gauge(percantage)
    print(actual_gauge)


def convert(fraction):
    while True:
        try:
            exist, trank = fraction.split("/")
            int_exist = int(exist)
            int_trank = int(trank)
            result = int_exist / int_trank

            if result <= 1:
                percent = int(result * 100)
                return percent
            else:
                fraction = input("Fraction: ")
                pass
        except (ZeroDivisionError, ValueError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
