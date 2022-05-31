def main():
    time = input("What time is it? ")
    current_time = convert(time)

    if 7.0 <= current_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= current_time <= 13.0:
        print("lunch time")
    if 18.0 <= current_time <= 19.0:
        print("dinner time")
    else:
        pass


def convert(time):
    h, m = time.split(":")
    time = round(int(h) + (int(m) / 60), 1)
    return time

if __name__ == "__main__":
    main()