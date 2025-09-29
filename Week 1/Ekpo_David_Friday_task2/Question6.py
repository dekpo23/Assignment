#Create title and set it to title variable
title = 'July 2025 Electric Bill'

#Prompt user for full name and set it to name variable
name = input('Enter your full name here: ')

#Prompt user for units consumed and set it to Units_Con variable
Units_Con = int(input('Enter units consumed here: '))

#Prompt user for cost per unit and set it to Cost_per_unit variable
Cost_per_unit = float(input('Enter cost per unit here: '))

#Calculate total
total = Units_Con * Cost_per_unit

#Print well formatted receipt using f strings
print(f' {title:^60} \n Name: {name:>54} \n Units Consumed(kWh): {Units_Con:>39} \n Cost per Unit: {Cost_per_unit:>45} \n Total Charges: {total:>45}')