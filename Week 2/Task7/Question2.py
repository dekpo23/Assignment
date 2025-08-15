#Create list to store items
items = ['books', 'pen', 'charger']

#Collect prics
price1 = float(input('Enter price for item 1: '))
price2 = float(input('Enter price for item 2: '))
price3 = float(input('Enter price for item 3: '))

#Create dictionary to store items and their prices
dic = {}
dic[items[0]] = price1
dic[items[1]] = price2
dic[items[2]] = price3

#Display items and their output
print(list(dic.keys()))
print(list(dic.values()))

#Update an item price
change_item = input('Enter item which price you want to update: ')
change_price = float(input('Enter updated price here: '))
print(change_item in dic.keys())

dic.update({change_item: change_price})
print(dic)
