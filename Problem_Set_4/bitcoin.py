import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit("Incorrect Command line arguments!")
else:
    try:
        coin = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            
        ## Print JSON file in a readable format
        #print(json.dumps(response.json(),indent= 2))

        #Convert request in JSON format
        o = response.json()
        #Dictionaries one in another
        ratef = o['bpi']['USD']["rate_float"]

        print(f"${ratef * coin:,}")
    except ValueError:
        sys.exit("Command line argument is not a number")
    except requests.RequestException():
        sys.exit("There was an ambiguous exception that occurred while handling your request.")
    