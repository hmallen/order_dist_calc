#!/usr/env python3

# Order distribution calculator

"""
1) Input center price (and distance) [or use market data]
2) Input trade amount
3) Input number of orders
4) Input exponential
"""

import gdax
import sys
import time

"""
center_price = float(input('Center Price: '))
trade_amount = float(input('Trade Amount: '))
order_number = float(input('Number of Orders: '))
order_exp = float(input('Price Exponential: '))
"""

while True:
    print()
    print('1: BTC-USD')
    print('2: LTC-USD')
    print('3: LTC-BTC')
    print('4: ETH-USD')
    print('5: ETH-BTC')
    user_product = int(input('Select Product:     '))

    if 0 < user_product < 6:
        break
    else:
        print('Invalid selection. Please try again.')

if user_product == 1:
    product = 'BTCUSD'
elif user_product == 2:
    product = 'LTCUSD'
elif user_product == 3:
    product = 'LTCBTC'
elif user_product == 4:
    product = 'ETHUSD'
elif user_product == 5:
    product = 'ETHBTC'
else:
    print('Unknown problem with product selection. Exiting.')
    sys.exit(1)

trade_amount = float(input('Trade Amount:      '))
order_number = float(input('Number of Orders:  '))
order_exp = float(input('Price Exponential: '))

public_client = gdax.PublicClient()


def user_menu(command):
    if command == 0:
        print('Stuff')
    elif command == 1:
        print('Things')
    elif command == 2:
        print('Junk')
    else:
        print('Error!')


def get_prices(product):
    # BTCUSD
    if product == 'BTCUSD':
        btcusd_bidask = public_client.get_product_order_book('BTC-USD', level=1)

        btcusd_bid = btcusd_bidask['bids'][0][0]
        btcusd_ask = btcusd_bidask['asks'][0][0]
    # LTCUSD
    elif product == 'LTCUSD':
        ltcusd_bidask = public_client.get_product_order_book('LTC-USD', level=1)

        ltcusd_bid = ltcusd_bidask['bids'][0][0]
        ltcusd_ask = ltcusd_bidask['asks'][0][0]

    # LTCBTC
    elif product == 'LTCBTC':
        ltcbtc_bidask = public_client.get_product_order_book('LTC-BTC', level=1)

        ltcbtc_bid = ltcbtc_bidask['bids'][0][0]
        ltcbtc_ask = ltcbtc_bidask['asks'][0][0]

    # ETHUSD
    elif product == 'ETHUSD':
        ethusd_bidask = public_client.get_product_order_book('ETH-USD', level=1)

        ethusd_bid = ethusd_bidask['bids'][0][0]
        ethusd_ask = ethusd_bidask['asks'][0][0]

    # ETHBTC
    elif product == 'ETHBTC':
        ethbtc_bidask = public_client.get_product_order_book('ETH-BTC', level=1)

        ethbtc_bid = ethbtc_bidask['bids'][0][0]
        ethbtc_ask = ethbtc_bidask['asks'][0][0]

    else:
        print('Invalid product selection.')


try:
    while True:
        time.sleep(5)
        
except:
    print('Exiting program.')
    sys.exit()
