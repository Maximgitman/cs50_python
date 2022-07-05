def main():
    input_twit = input("Input: ")
    print(shorten(input_twit))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    new_twitt = ""

    for i in word:
        if i.lower() in vowels:
            pass
        else:
            new_twitt += i
    return new_twitt


if __name__ == "__main__":
    main()
