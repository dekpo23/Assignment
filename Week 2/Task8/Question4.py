student = {}
student['name'] = input('Enter name here: ')
student['age'] = int(input('Enter age here: '))
student['scores'] = [70, 85, 90]
score = (sum(student['scores'])/len(student['scores'])) >= 50
student['passed'] = score
student['is_teen'] = student['age'] in range(13,20)

title = "Student Record"
print(f'{title:^50}')
print(f'Name: {student['name']:>44}')
print(f'Age: {student['age']:>45}')
print(f'Scores: {str(student['scores']):>42}')
print(f'Passed: {student['passed']:>42}')
print(f'Teenager: {student['is_teen']:>40}')