#Collect student's info
name = input('Enter your name here: ')
age = int(input('Enter student\'s age here: '))
gender = input('Enter student\'s gender here: ')
courses = input('Enter your courses seperated by space here: ')

#Create dictionary
student_bio = {}
student_bio['Student Name'] = name
student_bio['age'] = age
student_bio['gender'] = gender
student_bio['courses'] = courses.split()

#Print Output
courses_fmt = ' '.join(student_bio['courses'])
print(f'name: {student_bio["Student Name"]:>44} \nage: {student_bio["age"]:>45} \ngender: {student_bio["gender"]:>42} \ncourses: {courses_fmt:>41}')

