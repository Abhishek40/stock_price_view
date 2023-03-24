import requests
import time
import boto3
import os

stock_name = "AAPL"
api_key = "88b3e97efb4e46adb0a89d4295a8ec11"
db_client = boto3.resource('dynamodb')
table_name = 'stock_price_list'
def get_stock_price(stock_symbol, api):
    table = db_client.Table('stock_price_list')
    url = f"https://api.twelvedata.com/time_series?apikey={api}&interval=5min&symbol={stock_symbol}&format=JSON&outputsize=1"
    res = requests.get(url).json()
    stock_sym = res['meta']['symbol']
    price = res['values'][0]['open']
    time = res['values'][0]['datetime']
    print(stock_sym)
    print(price)
    print(time)
    response = table.put_item(
        Item={
            'Stock':stock_sym,
            'Price' : price,
            'Time' : time,
        }
    )
    print(response)

get_stock_price(stock_name,api_key)