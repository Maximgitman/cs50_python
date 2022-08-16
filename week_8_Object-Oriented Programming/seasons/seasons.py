from datetime import date
import inflect
import sys
import re




def main():
    birth_data = input("Date of Birth: ")

    try:
        year, month, day = validating(birth_data)
    except:
        sys.exit("Invalid Date")

    formated = date(int(year), int(month), int(day))
    today = date.today()
    print(get_minutes(formated, today))


def get_minutes(birth_data, today):
    p = inflect.engine()
    day_difference = today - birth_data
    minutes = day_difference.days * 24 * 60
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"


def validating(date_text):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", date_text):
        year, month, day = date_text.split("-")
        return year, month, day


if __name__ == "__main__":
    main()
