#Prompt user for distance and store in distance variable
distance = float(input('Enter the distance in km: '))

#Prompt user for fare per km
fare = float(input('Enter transport fare per km: '))

#Calculate the total fare and store in total variable
total = distance * fare

#Display formatted total fare
print(f'Total fare is {total:,.2f}')