from datetime import date, datetime
import inflect
import sys


class Minutes:
    today = date.today()
    p = inflect.engine()

    @classmethod
    def get_minutes(cls, birth_data):
        day_difference = cls.today - birth_data
        minutes = day_difference.days * 24 * 60
        words = cls.p.number_to_words(minutes)
        return f"{words.capitalize()} minutes"

def main():
    birth_data = validate(date.fromisoformat(input("Date of Birth: ")))

    print(Minutes().get_minutes(birth_data))


def validate(date_text):
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
        except ValueError:
            sys.exit("Incorrect data format, should be YYYY-MM-DD")


if __name__ == "__main__":
    main()

    
    """
    :( Input of "1999-01-01" yields "Five hundred twenty-five thousand, six hundred minutes" when today is 2000-01-01
    expected "Five hundred t...", not "Twelve million..."
    :( Input of "2001-01-01" yields "One million, fifty-one thousand, two hundred minutes" when today is 2003-01-01
        expected "One million, f...", not "Eleven million..."
    :( Input of "1995-01-01" yields "Two million, six hundred twenty-nine thousand, four hundred forty minutes" when today is 2000-01-1
        expected "Two million, s...", not "Fourteen milli..."
    :( Input of "2020-06-01" yields "Six million, ninety-two thousand, six hundred forty minutes" when today is 2032-01-01
        expected "Six million, n...", not "One million, o..."
    :( Input of "1998-06-20" yields "Eight hundred six thousand, four hundred minutes" when today is 2000-01-01
        expected "Eight hundred ...", not "Twelve million..."
    """