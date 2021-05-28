from typing import List
import requests
import json  
def get_coin(coin_name):
    coins_list=get_live_data()
    return coins_list[coin_name]

def get_live_data():
    print("Getting live data please wait...")
    response= requests.get("https://api.wazirx.com/api/v2/tickers")
    price_data=response.json()
    inr_coins=slicing_inr_data(price_data)
    return inr_coins

def slicing_inr_data(json_data):
    currency="inr"
    count=0
    count1=0
    coin_data={}
    for i in json_data:
        count+=1
        if(i[-3:]==currency):
            key=json_data[i]['base_unit']
            coin_data[key]=json_data[i]
            count1+=1
    return coin_data

def get_coin_list():
    coins_list=get_live_data()#getting inr whole values
    list=[]
    for i in coins_list: #slicing coins
        list.append(i)
    return list
'''
base_unit: ticker code of base market
quote_unit: ticker code of quote asset
low: 24 hrs lowest price of base asset
high: 24 hrs highest price of base asset
last: Last traded price in current market
open: Market Open price 24hrs ago
volume: Last 24hrs traded volume
sell: Top ask order price
buy: Top bid order price
name: Display text of market
at: Timestamp when ticker information is fetched
'''