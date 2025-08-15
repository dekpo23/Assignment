#Store days of a week and prompt user for inputs
days_of_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
day1 = input('Enter first day of the week where you perform an activity: ')
day2 = input('Enter second day of the week where you perform an activity: ')
day3 = input('Enter third day of the week where you perform an activity: ')

#Prompt user for 3 activities
activity1 = input('Enter first activity: ')
activity2 = input('Enter second activity: ')
activity3 = input('Enter third activity: ')

#Create and display dictionary
active_days_tuple = (day1, day2, day3)
activities = (activity1, activity2, activity3)
print({day: activity for day, activity in zip(active_days_tuple, activities)})


