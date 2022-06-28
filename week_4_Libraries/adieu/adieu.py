adieu = "Adieu, adieu, to "
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except (EOFError, KeyboardInterrupt):
        print()
        break

if len(names) == 1:
    print(adieu + names[0])
elif len(names) == 2:
    print(adieu + names[0] + " and " + names[1])
else:
    for n in range(len(names) - 1):
        if n == 0:
            adieu += names[n]
        else:
            adieu += ", " + names[n]
    print(adieu + ", and " + names[-1])
