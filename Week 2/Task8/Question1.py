num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number"))


print(f'{num1} == {num2} : {num1 == num2}')
print(f'{num1} != {num2} : {num1 != num2}')
print(f'{num1} > {num2} : {num1 > num2}')

"""
1. The first output checks for equality between numbers, it returns true if 
both numbers are equal and false if otherwise.

2. The second checks if both inputted variables are not equal, it returns true
if the not equal condition is met and false if otherwise.

3. The third checks if the number on the left if greater than the one on the 
right.
"""

"""
USE CASES

1. It can be used by hospitals check if a patient is overweight.
2. It can be used by loan sharks or banks to check if a customer 
has paid up a loan.
3. It can be used to check if a business makes profit or loss.
"""

#Code
#Obtain payment info
loan_amount = float(input('Enter amount loaned to customer: '))
payment = float(input('Enter amount payed back by customer: '))
interest_rate = float(input('Enter interest rate(in decimal): '))

#Calculate the amount to be payed
Amount_to_be_payed = (1 + interest_rate) * loan_amount

#Check if payment is complete
print(f'Payment Complete: {payment == Amount_to_be_payed}')
