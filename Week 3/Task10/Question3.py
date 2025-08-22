#Task3: Simulate a football match ticket system**
#Store all seat numbers (1 to 50) in a set.
#Ask users to "book" a seat by entering the number.
#Remove booked seats from the set.
#Show remaining seats after each booking.

#Create a set to store seat numbers
tickets = set(range(1,51))
#Allows user to book as many seats as possible
try:
    while len(tickets) != 0:
        print('Available seats are: ', ' '.join([str(x) for x in list(tickets)]))
        seat = int(input('Enter seat number here(1-50): '))
        if seat in tickets:
            tickets.remove(seat)
        else:
            print('Seat has already been booked. Choose another seat')
            print('Available seats are: ', ' '.join([str(x) for x in list(tickets)]))
            tickets.remove(int(input('Enter seat number here: ')))
        choice = int(input('Enter 1 to book another ticket and 2 to stop booking: '))
        if choice == 2:
            break
        elif choice == 1:
            pass
        else:
            raise ValueError('Your option isn\'t included here')
except ValueError as e:
    print('Error: ', e)


