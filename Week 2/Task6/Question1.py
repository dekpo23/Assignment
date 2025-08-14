#Prompt user for fruits seperated by space
fruits = input('Enter 5 fruits seperated by space: ')

#Split the fruits by space
fruits_set = set(fruits.split())

#Display result
print(fruits_set)