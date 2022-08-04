from validator_collection import checkers


def main():
    email = input("What's your email address? ")
    is_email_address = checkers.is_email(email)

    # Print VAlid if it is email
    if is_email_address:
        print("Valid")
    # Print Invalid otherwise
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
