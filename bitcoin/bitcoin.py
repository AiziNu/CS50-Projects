import requests
import sys


def main():
    #check if the number of btc is provided in coman line or not
    if len(sys.argv) !=2:
        sys.exit("Missing command line argument")

    #convert arg to float
    try:
        num_btc = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Number of bitcoin must be float")

    # fetch api
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Error: Unable to fetch a data")

    #conferting to json file
    try:
        data = response.json()
        btc_usd_price = data["bpi"]["USD"]["rate_float"]
    except (KeyError, TypeError, ValueError):
        sys.exit("Error: Unable to parse Bitcoin price.")

    total_cost = num_btc * btc_usd_price


    print(f"The current cost of {num_btc} Bitcoins is ${total_cost:,.4f} USD")

main()







