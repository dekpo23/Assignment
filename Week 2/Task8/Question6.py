#Collect student info
age = int(input('Enter your age here: '))
utme_score = int(input('Enter your utme score: '))
olevel = input('Do you have 5 credits in your olevel: ')
postutme = input('Did you paticipate in post utme?(True or False) ')
dept_score = float(input('Enter cumulative score after post utme here: '))
dept_cut_off = float(input('Enter departmental cut off here: '))

#Check admission status
final_admission = (age >= 16) and (utme_score >= 200) and (olevel.lower() == 'true') and (postutme.lower() == 'true') and (dept_score >= dept_cut_off)

#Print final message
print(f'Admitted: {final_admission}')