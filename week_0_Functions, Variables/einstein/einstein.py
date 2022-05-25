def einstein(mass):
    # Constant for E = mc2
    c = 300000000

    # Count mc ** 2
    e = mass * (c** 2)

    return e

mass = int(input("m: "))
print("E:", einstein(mass))