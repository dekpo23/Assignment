#Task3: Online Store Cart Calculation**
#Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).
#Start with an empty cart total (cart_total = 0).

#Define variables
items_list = ['Book', 'Pen', 'Bag', 'Shoes', 'Pencil']
item_prices = [200, 100, 5000, 4000, 50]
cart_total = 0

#Use for loop to obtain final price
for i in item_prices:
    cart_total += i
