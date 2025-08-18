age = int(input('Enter your age here: '))
utme_score = int(input('Enter your utme score: '))
olevel = input('Do you have 5 credits in your olevel: ')
postutme = input('Did you paticipate in post utme?(True or False) ')
dept_cut_off = float(input('Enter departmental cut off here: '))

final_admission = (age >= 16) and (utme_score >= 200) and (olevel.lower() == 'true') and (postutme.lower() == 'true') and (dept_cut_off >= 200)
print(f'Admitted: {final_admission}')