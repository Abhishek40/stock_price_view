import json
import boto3

def lambda_handler(event, context):
    client = boto3.resource("dynamodb")
    sns = boto3.client('sns')
    table = client.Table("stock_price_list")
    stock_list = table.scan()['Items']
    for stock in stock_list:
        if stock['Stock'] == 'AMZN':
            stock_price = stock['Price']
            print(stock_price)
            
            sns_response = sns.publish(
                TargetArn = "arn:aws:sns:eu-central-1:266186731626:public-ip",
                Message = json.dumps({'default': stock_price}),
                MessageStructure = 'json'
                )
    #print(stock_list)