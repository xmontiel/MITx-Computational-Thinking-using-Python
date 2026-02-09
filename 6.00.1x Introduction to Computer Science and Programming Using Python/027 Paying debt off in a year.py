# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 21:54:10 2025

@author: Xuan
"""

balance = 4773
x = balance
annual_interest_rate = 0.2
minimum_monthly_payment = -10
updated_balance_each_month = balance

while updated_balance_each_month > 0:
    balance = x
    count = 0
    minimum_monthly_payment += 10
    monthly_interest_rate = 0
    monthly_unpaid_balance = 0
    updated_balance_each_month = 0
    while count < 12:
        count += 1
        monthly_interest_rate = annual_interest_rate / 12.0
        monthly_unpaid_balance = round(balance,2) - round(minimum_monthly_payment,2)
        updated_balance_each_month = round(monthly_unpaid_balance,2) + monthly_interest_rate * round(monthly_unpaid_balance,2)
        balance = round(updated_balance_each_month,2)


print("Lowest Payment: " + str(minimum_monthly_payment))