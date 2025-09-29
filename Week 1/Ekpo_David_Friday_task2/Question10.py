#Prompt user name of school and store in variable school_name
school_name = input('Enter your school name here: ')

#Add " fees breakdown" to school name
school_name += ' fees breakdown'

#Prompt user for tuition fee and store in tuition_fee variable
tuition_fee = float(input('Enter your tuition fee here: '))

#Prompt user for hostel fee and store in hostel_fee variable
hostel_fee = float(input('Enter your hostel fee here: '))

#Prompt user for feeding fee and store in feeding_fee variable
feeding_fee = float(input('Enter your feeding fee here: '))

#Calculate total school fees
total = tuition_fee + hostel_fee + feeding_fee

#Print well formatted receipt using f strings
print(f' {school_name:^80} \n Tuition fee: {tuition_fee:>67} \n Hostel fee: {hostel_fee:>68} \n Feeding fee: {feeding_fee:>67} \n Total: {total:>73}')
