#Task2: Super Market Price List
food_list = ['beans', 'rice', 'yam', 'garri']
#create dictionary
food_dic = {}
#Loop through list of foods
for food in food_list:
    food_dic[food] = float(input(f'Enter price of {food} here: '))
#Display dictionary items
print(food_dic.keys())
print(food_dic.values())
#Collect user input
food = input('Choose food whose price you want to update: ')
#Update dictionary
new_price = float(input('Enter new price here: '))
food_dic.update({food: new_price})
print(food_dic)