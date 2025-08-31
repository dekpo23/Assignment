

# Simple Calculator Program

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract second number from first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide first number by second
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Function to obtain remainder of first number after dividing by second number
def mod(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Division by zero"

# Function to handle exponentials
def exp(a, b):
    return a ** b

def square_root(a):
    return a ** 0.5

#Function for error handling, input validation and result display
def main():
    while True:
        try:
            # Display operation options to the user
            print("Select operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Modulus")
            print("6. Exponential")
            print("7. Square Root")
            print("8. Exit")

            # Take input from the user for operation choice
            choice = int(input("Enter choice (1/2/3/4/5/6/7/8): "))

            
            if choice in range(1,7):
                # Get two numbers as input from the user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                # Perform calculation based on user's choice
                if choice == 1:
                    print("Result:", add(num1, num2))
                elif choice == 2:
                    print("Result:", subtract(num1, num2))
                elif choice == 3:
                    print("Result:", multiply(num1, num2))
                elif choice == 4:
                    print("Result:", divide(num1, num2))
                elif choice == 5:
                    print("Result:", mod(num1, num2))
                elif choice == 6:
                    print("Result:", exp(num1, num2))
            
            elif choice == 7:
                num1 = float(input("Enter number: "))
                print("Result:", square_root(num1))

            elif choice == 8:
                print('Shutting program down')
                break

            else:
                print('Enter valid input please ')

           
        except ValueError as e:
            print("Error: ", e)    

main()