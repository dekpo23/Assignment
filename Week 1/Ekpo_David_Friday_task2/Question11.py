#Prompt user for amount in naira
amount = float(input('Enter Amount in Naira: '))

#Prompt user for usd to naira rate
usd_rate = float(input('Exchange rate to USD: '))

#Prompt user for gbp to naira rate
pounds_rate = float(input('Exchange rate to Pounds:'))

#Create title
title = 'Nigerian Currency Converter'

#Print currency converter table
print(f' {title:^60} \n Amount($): {amount/usd_rate:>49,.2f} \n Amount(£): {amount/pounds_rate:>49,.2f}')