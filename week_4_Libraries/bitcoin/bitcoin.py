from sys import exit, argv
import requests


if len(argv) == 2:
    try:
        quantity_bitcoin = float(argv[1])
    except:
        print("Command-line argument is not a number")
        exit(1)
else:
    print("Missing command-line argument")
    exit(1)

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response_json = r.json()
    rate = response_json["bpi"]["USD"]["rate_float"]
    total = rate * quantity_bitcoin
    print(f"${total:,.4f}")

except requests.RequestException:
    print("RequestException")
    exit(1)
