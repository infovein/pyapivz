#!/usr/bin/python3

import requests
import pprint

def main():
    mylookup = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AMZN&interval=5min&apikey=IJCWJ9MMJ3YV4AH2"
    stockdata = requests.get(mylookup)
    #print(stockdata.json()) #print all data
    decodestockdata = stockdata.json()
    lastrefresh = stockdata.json()["Meta Data"]["3. Last Refreshed"]
    
    pprint.pprint(decodestockdata["Time Series (5min)"][lastrefresh])


main()
