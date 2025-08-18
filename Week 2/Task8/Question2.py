#Enter candidate info 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))

#Citizenship
nationality = input('State your country: ')

#Institution
institution = input('Enter your higher institution: ')
nigerian_universities = [
    "University of Lagos",
    "University of Ibadan",
    "Obafemi Awolowo University",
    "Ahmadu Bello University",
    "University of Nigeria, Nsukka",
    "Covenant University",
    "Federal University of Technology, Akure",
    "University of Benin",
    "University of Ilorin",
    "University of Port Harcourt",
    "Ladoke Akintola University of Technology",
    "Bayero University Kano",
    "Nnamdi Azikiwe University",
    "University of Jos",
    "Federal University of Technology, Minna",
    "Federal University of Technology, Owerri",
    "Abubakar Tafawa Balewa University",
    "Olabisi Onabanjo University",
    "Adekunle Ajasin University",
    "Lagos State University",
    "Ambrose Alli University",
    "Delta State University",
    "University of Uyo",
    "Benue State University",
    "Ekiti State University",
    "Rivers State University",
    "Babcock University",
    "Afe Babalola University",
    "Pan-Atlantic University",
    "American University of Nigeria"
]
nigerian_universities_fmt = [x.lower() for x in nigerian_universities]

#Scholarship
scholarship = input('Do you have any other scholarship from oil and gas industries in Nigeria?(True or False) ')

#Academic Qualification
subjects = input('Enter subjects(including maths and English) seperated by commas: ')
grades = input('Enter grades for the subjects listed above seperated by commas: ')

subjects_list = [x.strip() for x in subjects.split(',')]
grades_list = [x.strip() for x in grades.split(',')]
grade_list_fmt = [x.upper() for x in grades_list]



performance_dic = {subject.lower(): grade.upper() for subject, grade in zip(tuple(subjects_list), tuple(grades_list))}
performance_bool = (performance_dic['english'] == 'A' or performance_dic['english'] == 'B') and (performance_dic['mathematics'] == 'A' or performance_dic['mathematics'] == 'B') and (grade_list_fmt.count('A') + grade_list_fmt.count('B')) >= 5

eligibility = (age < 18) and (score > 70) and (nationality.title() == 'Nigeria') and (institution.lower() in nigerian_universities_fmt) and (scholarship.lower() == 'false') and (performance_bool == True)
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")


