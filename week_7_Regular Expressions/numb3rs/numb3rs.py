import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        splited_ip = ip.split(".")
        for n in splited_ip:
            if int(n) < 0 or int(n) > 255:
                return False
        return True
    else:

        return False


if __name__ == "__main__":
    main()
