#Print welcome message in pidgin
print('Welcome boss, how u dey na')

#Store ussd code in ussd variable
ussd = '*321*'

#Print message to prompt user to dial code
print(f'Please dial {ussd} to access our services.')

#Print menu
print('1. Check balance \n 2. Buy airtime \n 3. Buy  data \n 4. Speak to Customer Care rep')

#Prompt user to make choice
choice = int(input('Choose from options 1 - 4 above: '))

#Print confirmation message showing   user choice
print(f'You chose option {choice}')

#Prompt user for airtime/data amount
amount = float(input('Enter amount of airtime/ data here: '))

#Print final message
print(f'You bought airtime/data worth {amount}')