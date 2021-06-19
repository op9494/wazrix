from notifiaction import Send_notification_Android
from typing import List
from wazrix_data import get_coin,get_coin_list
import requests
import json
#Import python modules
import time
from query_DB import get_past_value,Update_row_in_table_NEWCOINDETAIL
 
#define a function for you want it be repeated

#Write the function you want to execute periodically

#create a while loop and place your function inside it and use time.sleep function
def checking_new_coin():
    new_coin_T_F=len(get_coin_list())
    past_value=get_past_value()
    print(f"newdata={new_coin_T_F} and past data={past_value}")
    if new_coin_T_F>past_value:
        Update_row_in_table_NEWCOINDETAIL(new_coin_T_F)
        Send_notification_Android("Some new coins has been added please check")
    else:
        print("No change in Market")
    
def get_coin_change(coin_name):
    print(get_coin(coin_name)['last'])
'''
    while True:
        #    
        time.sleep(1) #1 second
'''
#----------------------------------------------------------------
#To send the notification
#Send_notification_Android(<msg>)

#----------------------------------------------------------------
#get_coin(<coin_name>)

#get_coin_list() to display coins
#----------------------------------------------------------------

#----------------------------------------------------------------
'''
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
  
# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes
'''


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