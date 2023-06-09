#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 20:28:05 2023

@author: chinmayakumarpalo
"""

import requests

def currency_converter(amount, from_currency, to_currency):
    api_key = "f695af22308991d811dd5a2db5209817"  

   
    response = requests.get(f"http://api.exchangeratesapi.io/v1/latest?base={from_currency}&symbols={to_currency}&access_key={api_key}")

    if response.status_code == 200:
        data = response.json()
        conversion_rate = data['rates'][to_currency]
        converted_amount = amount * conversion_rate
        return converted_amount
    else:
        print("Error fetching exchange rates.")
        return None


amount = 100
from_currency = 'USD'
to_currency = 'EUR'
converted_amount = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
