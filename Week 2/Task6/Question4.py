#Create a set of names
names = {"David", "Grace", "Mercy"}
#Prompt user for name
your_name = input('Enter your name here: ')
#Print message if user name is already in set
if your_name in names:
    print('Don\'t register twice')
#Add name to set
names.add(your_name)