grocery = {}

while True:
    try:
        item = input().upper()  
        if item in grocery.keys():
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        print()  
        for key, value in sorted(grocery.items()):
            print(value, key)
        break