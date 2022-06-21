# 1. “All vanity plates must start with at least two letters.”
# 2. “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# 3. “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; 
# AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# 4. “No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
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