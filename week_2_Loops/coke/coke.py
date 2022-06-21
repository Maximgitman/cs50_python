amount = 50

allowed_currency = [25, 10, 5]

while amount > 0:
    print(f"Amount Due: {amount}")
    insert_coin = int(input("Insert Coin: "))
    if insert_coin in allowed_currency:
        amount -= insert_coin
    if amount == 0:
        print(f"Change Owed: {amount}")
    elif amount < 0:
        debt = insert_coin - (amount + insert_coin)
        print(f"Change Owed: {debt}")
