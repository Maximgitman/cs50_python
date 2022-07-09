def main():
    plate = input("Plate: ").upper()
    validation = is_valid(plate)
    if validation == True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()
    not_allowed = ",. #$%^&*()_+=-/\|"
    if len(s) > 6 or len(s) < 2 or s[0].isdigit() or s[1].isdigit() or any(x in not_allowed for x in s):
        return False

    else:
        if s.isalpha():
            return True
        else:
            if s[-1].isalpha():
                return False
            else:
                for d in range(len(s)):
                    if s[d].isdigit():
                        if int(s[d]) == 0:
                            return False
                        elif any(x.isalpha() for x in s[d:]):
                            return False
                        else:
                            return True

     
if __name__=="__main__":
    main()