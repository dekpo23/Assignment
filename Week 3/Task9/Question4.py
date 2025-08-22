#Task4: Student Record

#Create dictionary
student = {}
#Create items list
items_list = ['Name', 'Age', 'Scores']
#Collect user inputs
name = input('Enter name here ')
age = int(input('Enter your age here '))

#Collect scores
student['scores'] = [65, 70 ,85]
#Check if student passed
if sum(student['scores']) / len(student['scores']) >= 50:
    print('Passed')
else:
    print('Failed')