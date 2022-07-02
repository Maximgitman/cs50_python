from sys import exit, argv
from textwrap import indent
import requests
import json


if len(argv) == 2:
    try:
        quantity_bitcoin = float(argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        exit(1)
else:
    print("Missing command-line argument")
    exit(1)

try:
    request = requests.get(url="https://api.coindesk.com/v1/bpi/currentprice.json")
    json_req = request.json()
    rate = json_req["bpi"]["USD"]["rate_float"]
    bit_in_usd = rate * quantity_bitcoin
    print(f"${bit_in_usd:,.4f}")

except requests.RequestException:
    print("RequestException")
    exit(1)