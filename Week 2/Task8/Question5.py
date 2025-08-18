store = {'Book': 10, 'Pen': 20, 'Bag': 5}
item_to_buy = input('Enter item you want to buy: ')
item_quantity = int(input('Enter quantity you want to buy: '))
store[item_to_buy] -= item_quantity
print(store)
