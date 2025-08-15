#Create a tuple for names and phone numbers
names = ('David', 'Ekpo', 'Friday')
phone_nos = ('915556', '081699', '905067')

#Create a dctionary
info = {name: num for name, num in zip(names, phone_nos)}

#prompt user  for new name and get the phone number
user_name = input('Enter a name: ')
print(info.get(user_name))