# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 23:26:10 2025

@author: Xuan
"""

balance = 320000
x = balance
annual_interest_rate = 0.2
updated_balance_each_month = balance
monthly_interest_rate = annual_interest_rate / 12.0
monthly_payment_lower_bound = balance / 12
y = (balance * (1 + monthly_interest_rate)**12) / 12
monthly_payment_upper_bound = y
minimum_monthly_payment = (monthly_payment_lower_bound + monthly_payment_upper_bound) / 2.0
epsilon = 0.001

while monthly_payment_upper_bound - monthly_payment_lower_bound >= epsilon:
    balance = x
    count = 0
    minimum_monthly_payment = (monthly_payment_lower_bound + monthly_payment_upper_bound) / 2.0
    monthly_unpaid_balance = 0
    updated_balance_each_month = 0
    while count < 12:
        count += 1
        monthly_interest_rate = annual_interest_rate / 12.0
        monthly_unpaid_balance = balance - minimum_monthly_payment
        updated_balance_each_month = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
        balance = updated_balance_each_month
        print(balance)
    if balance > 0:
        monthly_payment_lower_bound = minimum_monthly_payment
    else:
        monthly_payment_upper_bound = minimum_monthly_payment


print("Lowest Payment: " + str(round(minimum_monthly_payment,2)))