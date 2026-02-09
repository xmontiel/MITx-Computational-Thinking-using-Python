# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 21:06:21 2025

@author: Xuan
"""

def annual_balance(balance,annual_interest_rate,monthly_payment_rate):
    
    count = 0
    
    while count < 12:
        count += 1
        monthly_interest_rate = annual_interest_rate / 12.0
        minimum_monthly_payment = monthly_payment_rate * round(balance,2)
        monthly_unpaid_balance = round(balance,2) - round(minimum_monthly_payment,2)
        updated_balance_each_month = round(monthly_unpaid_balance,2) + monthly_interest_rate * round(monthly_unpaid_balance,2)
        balance = round(updated_balance_each_month,2)
        print("Month " + str(count) + " Remaining balance: " + str(balance))
    return balance
    
print(annual_balance(42,0.2,0.04))


