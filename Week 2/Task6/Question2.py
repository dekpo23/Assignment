#Question 2

#Enter names of people seperated by space
event_attendance = input('Enter names of people seperated by space here: ')
#Extract names from event_attendance and store in set event_set
event_set = set(event_attendance.split())
#sort the set
print(sorted(event_set, key = lambda x:x.lower()))