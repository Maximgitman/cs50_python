import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(
        r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$",
        s,
    ):
        first_time = s.split(" ")[:2]
        second_time = s.split(" ")[3:]

        # + 12 h and change format to h:02
        if ":" in first_time[0]:
            split_first = first_time[0].split(":")
            m = split_first[1]
            if first_time[1] == "PM":
                if first_time[0] == "12":
                    h = 12
                else:
                    h = int(split_first[0]) + 12
            else:
                if first_time[0] == "12":
                    h = 0
                else:
                    h = int(split_first[0]) + 12
            first_time[0] = f"{h:02}:{m}"
        else:
            m = "00"
            if first_time[1] == "PM":
                if first_time[0] == "12":
                    h = 12
                else:
                    h = int(first_time[0]) + 12
            else:
                if first_time[0] == "12":
                    h = 0
                else:
                    h = int(first_time[0]) + 12
            first_time[0] = f"{h:02}:{m}"

        # Second time
        if ":" in second_time[0]:
            split_second = second_time[0].split(":")
            m = split_second[1]
            if second_time[1] == "PM":
                h = int(split_second[0]) + 12
            else:
                h = int(split_second[0])
            second_time[0] = f"{h:02}:{m}"
        else:
            m = "00"
            if second_time[1] == "PM":
                h = int(second_time[0]) + 12
            else:
                h = int(second_time[0])

            second_time[0] = f"{h:02}:{m}"

        corrected_time = f"{first_time[0]} to {second_time[0]}"

        return corrected_time


"""
1. Check if 12 for second time

:( working.py converts "12 AM to 12 PM" to "00:00 to 12:00"
    expected "00:00 to 12:00...", not "12:00 to 24:00..."
:( working.py converts "12:00 AM to 12:00 PM" to "00:00 to 12:00"
    expected "00:00 to 12:00...", not "12:00 to 24:00..."
:( working.py raises ValueError when given "8:60 AM to 4:60 PM"
    expected "ValueError", not "None\n"
:( working.py raises ValueError when given "9AM to 5PM"
    expected "ValueError", not "None\n"
:( working.py raises ValueError when given "09:00 to 17:00"
    expected "ValueError", not "None\n"
:( working.py raises ValueError when given "9 AM - 5 PM"
    expected "ValueError", not "None\n"
:( working.py raises ValueError when given "10:7 AM - 5:1 PM"
    expected "ValueError", not "None\n"
:( correct working.py passes all test_working checks
    expected exit code 0, not 5
"""

if __name__ == "__main__":
    main()
