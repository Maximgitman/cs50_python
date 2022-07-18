import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"<iframe(.)*><\/iframe>", s):
        if url_matches := re.search(
            r"(http)(s)*:\/\/(www\.)*youtube\.com\/embed\/([a-z_A-Z_0-9]+)", s
        ):
            splited_url = url_matches.group(4)
            return f"https://youtu.be/{splited_url} "
    else:
        return None


if __name__ == "__main__":
    main()
