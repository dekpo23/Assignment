#Create set of numbers from 1 to 50
numbers = set([i for i in range(1, 51)])
#Prompt user for a number
num = int(input('Choose the seat number you prefer: '))
#Remove the number from the set
numbers.remove(num)
#Display output
print(numbers)
