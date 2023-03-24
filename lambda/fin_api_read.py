import requests
import time
import json
# import os
# import boto3

# ddb = boto3.resource('dynamodb')
# table_name = os.environ('TABLE_NAME')
# table = ddb.Table(table_name)
stock_name = "MSFT"
api_key = "88b3e97efb4e46adb0a89d4295a8ec11"
    
def get_stock_price(stock_symbol, api):
        url = f"https://api.twelvedata.com/price?symbol={stock_symbol}&apikey={api}"
        res = requests.get(url).json()
        #print(res)
        return res
def lambda_handler(res, context):

    get_stock_price(stock_name,api_key)
    #return event.res
    return res