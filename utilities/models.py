from django.db import models

# Create your models here.
CHOICES_CRYP1 = [
    ('BTC', 'Bitcoin (BTC)'),
    ('ETH', 'Ethereum (ETH)'),
    ('USDT', 'Tether (USDT)'),
    ('USDC', 'USD Coin (USDC)'),
    ('BNB', 'BNB (BNB)'),
    ('AVAX', 'Avalanche (AVAX)'),
    ('SOL', 'Solano (SOL)'),
    ('LUNA', 'Terra (LUNA)'),
    ('XRP', 'XRP (XRP)'),
    ('ADA', 'Cardano (ADA)'),
    ('LTC', 'Litecoin (LTC)'),
    ('DOT', 'Polkadot (DOT)'),
    ('BUSD', 'Binance USD (BUSD)'),
    ('MATIC', 'Polygon (Matic)'),
    ('LINK', 'ChainLink (Link)'),
    ('UNI', 'Uniswap (UNI)'),
    ('MANA', 'Decentraland (MANA)'),
    ('TRX', 'Tron (TRX)'),
    ('HBAR', 'Hedera(HBAR)'),
    ('XLM', 'Stellar'),
    ('AXS', 'Axie Infinity (AXS)')
]

CHOICES_CRYP2 = [
    ('BTC', 'Bitcoin (BTC)'),
    ('ETH', 'Ethereum (ETH)'),
    ('USDT', 'Tether (USDT)'),
    ('USDC', 'USD Coin (USDC)'),
    ('BNB', 'BNB (BNB)'),
    ('AVAX', 'Avalanche (AVAX)'),
    ('SOL', 'Solano (SOL)'),
    ('LUNA', 'Terra (LUNA)'),
    ('XRP', 'XRP (XRP)'),
    ('ADA', 'Cardano (ADA)'),
    ('LTC', 'Litecoin (LTC)'),
    ('DOT', 'Polkadot (DOT)'),
    ('BUSD', 'Binance USD (BUSD)'),
    ('MATIC', 'Polygon (Matic)'),
    ('LINK', 'ChainLink (Link)'),
    ('UNI', 'Uniswap (UNI)'),
    ('MANA', 'Decentraland (MANA)'),
    ('TRX', 'Tron (TRX)'),
    ('HBAR', 'Hedera(HBAR)'),
    ('XLM', 'Stellar'),
    ('AXS', 'Axie Infinity (AXS)'),
    ('USD', 'US Dollars (USD)'),
    ('AUB', 'Australian Dollar (AUD)'),
    ('CAD', 'Canadian Dollar (CAD)'),
    ('CNY', 'Chinese Yuan (CNY)'),
    ('EUR', 'European Euro (EURO)'),
    ('INR', 'Indian Rupee (INR)'),
    ('JPY', 'Japanese Yen (JPY)'),
    ('SGD', 'Singapore Dollar (SGD)')
]

CHOICES = [
    ('ETH', 'Ethereum (ETH)'),
    ('MATIC', 'Polygon (Matic)'),
    ('UNI', 'Uniswap (UNI)'),
    ('LINK', 'ChainLink (Link)'),
    ('USDT', 'Tether (USDT)'),
    ('BNB', 'BNB (BNB)'),
    ('USDC', 'USD Coin (USDC)'),
    ('TRX', 'Tron (TRX)'),
]

class Post(models.Model):
    Quantity = models.IntegerField()
    ConvertFrom = models.CharField(max_length=20, choices=CHOICES_CRYP1, default='BTC')
    ConvertTo = models.CharField(max_length=20, choices=CHOICES_CRYP2, default='USD')

class balance(models.Model):
    Address = models.CharField(max_length=50)
    Coin = models.CharField(max_length=20, choices=CHOICES, default='BTC')

    
# USD United State Dollar
# AUB Australian Dollar
# CAD Canadian Dollar
# CNY Chinese Yuan
# EUR EURO
# INR Indian Rupee
# JPY Japanese Yen
# SGD Singapore Dollar

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