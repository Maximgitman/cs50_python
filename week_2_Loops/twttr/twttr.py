input_twit = input("Input: ")

vowels = ["a", "e", "i", "o", "u"]

new_twitt = ""

for i in input_twit:
    if i.lower() in vowels:
        pass
    else:
        new_twitt += i

print(new_twitt)