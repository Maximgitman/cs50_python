import re


def main():
    print(convert(input("Hours: ")))


def convert(s):

    match = re.search(
        r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$",
        s,
    )
    if match:
        first_time = s.split(" ")[:2]
        second_time = s.split(" ")[3:]

        # + 12 h and change format to h:02
        if ":" in first_time[0]:
            split_first = first_time[0].split(":")
            m = split_first[1]
            if first_time[1] == "PM":
                if split_first[0] == "12":
                    h = 12
                else:
                    h = int(split_first[0]) + 12
            else:
                if split_first[0] == "12":
                    h = 0
                else:
                    h = int(split_first[0])
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
                    h = int(first_time[0])
            first_time[0] = f"{h:02}:{m}"

        # Second time
        if ":" in second_time[0]:
            split_second = second_time[0].split(":")
            m = split_second[1]
            if second_time[1] == "PM":
                if split_second[0] == "12":
                    h = 12
                else:
                    h = int(split_second[0]) + 12
            else:
                if split_second[0] == "12":
                    h = 0
                else:
                    h = int(split_second[0])
                h = int(split_second[0])
            second_time[0] = f"{h:02}:{m}"
        else:
            m = "00"
            if second_time[1] == "PM":
                if second_time[0] == "12":
                    h = 12
                else:
                    h = int(second_time[0]) + 12
            else:
                if second_time[0] == "12":
                    h = 0
                else:
                    h = int(second_time[0])
            second_time[0] = f"{h:02}:{m}"

        corrected_time = f"{first_time[0]} to {second_time[0]}"

        return corrected_time
    else:
        raise ValueError


if __name__ == "__main__":
    main()
