#Prompt user for 3 names
names = input('Enter 3 names seperated by comma here: ')

#Create and display dictionary
names_set = set(names.split(','))
names_set = set(name.strip() for name in names_set)
names_dic = {name: len(name) for name in names_set}
print(names_dic)