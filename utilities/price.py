import json
import os
import pprint
from requests import Request,Session
from dotenv import load_dotenv

load_dotenv()
symbol = ''
convert =''
def getPrice(symbol,convert):
    url ='https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    parameters = {
        'symbol' : symbol,
        'convert' : convert
    }

    headers = {
        'Accepts' : 'application/json',
        'X-CMC_PRO_API_KEY' : os.environ['KEY']
    }

    session = Session()
    session.headers.update(headers)

    response =session.get(url , params=parameters)
    price = json.loads(response.text)['data'][symbol][0]['quote'][convert]['price']
    pprint.pprint(price)

    return price



# BTC bitcoin 
# ETH ethereum
# USDT tether 
# USDC usd coin 
# BNB bnb 
# AVAX avalanche
# SOL solano
# LUNA terra
# XRP xrp
# ADA cardano 
# LTC litecoin
# DOT Polkadot
# BUSD Binance USD 
# MATIC polygon
# LINK chainlink
# UNI uniswap
# MANA Decentraland
# TRX tron
# HBAR hedera
# XLM stellar
# AXS Axie Infinity

# USD United State Dollar
# AUB Australian Dollar
# CAD Canadian Dollar
# CNY Chinese Yuan
# EUR EURO
# INR Indian Rupee
# JPY Japanese Yen
# SGD Singapore Dollar