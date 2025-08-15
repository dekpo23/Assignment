
#Collect Basic Info
name = input('Enter student\'s name here: ')
age = int(input('Enter student\'s age here: '))
gender = input('Enter student\'s gender here: ')
class_ = input('Enter student\'s class here: ')

#Collect scores for subjects
subjects = ('maths', 'eng', 'bio', 'chem', 'phy')

scores = tuple(float(input(f'Enter score for {subject}: ')) for subject in subjects)

#Guardian info
Guardian_name = input('Enter guardian name here: ')
Guardian_phone_num = input('Enter guardian phone number here: ')

#hobbies
hobbies = set(input('Enter hobbies seperated by commas: ').split(','))
hobbies = tuple(hobby.strip() for hobby in hobbies)

class_profile = {'Basic Info': {'Name': name.title(), 'Age': age, 'class': class_, 'Gender': gender}, 'Performance': {subject: score for subject, score in zip(subjects, scores)}, 'Guardian info': {'Guardian name': Guardian_name.title(), 'Guardian Phone number': Guardian_phone_num}, 'Hobbies': list(hobbies)}

#Derived Data
class_profile["Performance"]["Average"] = sum(scores) / len(scores)
class_profile["Basic Info"]["Initials"] = "".join([n[0] for n in name.split()])
class_profile["Hobbies Count"] = len(hobbies)

#Output
title = 'Student Profile'
title2 = 'Student\'s Performance'
title3 = 'Guardian Information'
title4 = 'Hobbies'


print('\n')
print(f'{title:^50}')
print(f"Name: {class_profile['Basic Info']['Name']:>44}")
print(f"Age: {class_profile['Basic Info']['Age']:>45}")
print(f"Gender: {class_profile['Basic Info']['Gender']:>42}")

print('\n')
print(f'{title2:^50}')
print(class_profile["Performance"])

print('\n')
print(f'{title3:^50}')
print(class_profile["Guardian info"])

print('\n')
print(f'{title4:^50}')
print(class_profile["Hobbies"])
print(f"\nTotal Hobbies:\t{class_profile['Hobbies Count']}")
print(f"Average Score:\t{class_profile['Performance']['Average']:.2f}")
