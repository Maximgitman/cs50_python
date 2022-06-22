months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

while True:
    users_date = input("Date: ").strip()
    try:
        if "/" in users_date:
            date = users_date.split("/")
            if 1 < int(date[0]) <= 12  and 1 <= int(date[1]) <= 31:
                year = date[-1]
                month = f"{int(date[0]):02}"
                day = f"{int(date[1]):02}"
                print(f"{year}-{month}-{day}")
                break
        else:
            date = users_date.split()
            if date[0] in months and "," in date[1]:
                splited_day = int(date[1].split(",")[0])
                if 1 <= splited_day <= 31:
                    year = date[-1]
                    month = f"{months.index(date[0])+1:02}"
                    splited_date = date[1].split(",")
                    day = f"{splited_day:02}"
                    print(f"{year}-{month}-{day}")
                    break
    except ValueError:
        pass
