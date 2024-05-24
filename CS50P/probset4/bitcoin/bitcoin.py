import json
import requests
import sys

def main():
    money = get_coin()
    requested_coin(money)

# command-line argument for the request of number of Bitcoin user would like to purchase.
def get_coin():
    if len(sys.argv) == 2:
        try:
            if float(sys.argv[1]):
                return sys.argv[1]
        except ValueError:
            # error handling
            print("Command-line argument is not a number")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)

def requested_coin(givencoin):
    # function takes the amount entered by user and then multiplies by the price of Bitcoin in API to return price of Bitcoin.
    req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    usdata = req.json()
    usd = usdata["bpi"]["USD"]["rate_float"]
    rsdata = float(usd) * float(givencoin)
    # values converted to float instead of int for accurate multipication.
    print(givencoin)
    print(f"${rsdata:,.4f}")
# calling the main function where all of the programming jizz takes place.
if __name__ == "__main__":
    main()
