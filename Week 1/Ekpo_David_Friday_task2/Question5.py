#Prompt user for market name and store it in market_name variable
market_name = input('Enter name of market: ')

#Prompt user for number of traders and store it in no_of_traders variable
no_of_traders = int(input('Enter number of traders: '))

#Prompt user for daily revenue and store it in daily_revenue variable
daily_revenue = float(input('Enter daily revenue in naira: '))

#Print the report using the information above
print(f'The number of traders at {market_name} is currently {no_of_traders}, all of which contributes to {daily_revenue:,} in daily revenue')