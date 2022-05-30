def main():
    # Greeting from a bank
    greeting = input("Greeting: ").strip()

    # Getting input greeting
    if greeting[:5].lower() == "hello":
        print("$0")
    elif greeting[0].lower() == "h":
        print("$20")
    else:
        print("$100")
    

main()