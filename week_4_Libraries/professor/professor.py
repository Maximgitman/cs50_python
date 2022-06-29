from distutils.log import error
import random


def main():
    n = get_level()
    score = 0

    for i in range(10):
        error = 0
        first, second = generate_integer(n)
        try:
            assignment = int(input(f"{first} + {second} = "))
        except ValueError:
            pass

        if assignment == (first + second):
            score += 1

        while assignment != (first + second) and error < 3:
            if assignment == (first + second):
                score += 1
            elif assignment != (first + second):
                error += 1
                print("EEE")
                if error == 3:
                    score -= 1
                    print(f"{first} + {second} = {first + second}")
                else:
                    try:
                        assignment = int(input(f"{first} + {second} = "))
                    except ValueError:
                        pass
    print("Score:", score)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except ValueError:
            pass


def generate_integer(level):
    start = 10 ** (level - 1)
    end = (10**level) - 1

    if level == 1:
        first_number = random.randint(start-1, end)
        second_number = random.randint(start-1, end)
    else:
        first_number = random.randint(start, end)
        second_number = random.randint(start, end)

    return first_number, second_number


if __name__ == "__main__":
    main()
