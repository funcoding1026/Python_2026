#1-this program will perform six operstions on two numbers and prit the rsults of each operation using choices and if else statements
#------------------------------------------------------------------------------------------------------------
'''a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
while True:
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        result = a + b
        print(f"The sum of {a} and {b} is: {result}")
    elif choice == '2':
        result = a - b
        print(f"The difference between {a} and {b} is: {result}")
    elif choice == '3':
        result = a * b
        print(f"The product of {a} and {b} is: {result}")
    elif choice == '4':
        if b != 0:
            result = a / b
            print(f"The quotient of {a} divided by {b} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == '5':
        if b != 0:
            result = a % b
            print(f"The modulus of {a} and {b} is: {result}")
        else:
            print("Error: Modulus by zero is not allowed.")
    elif choice == '6':
        result = a ** b
        print(f"{a} raised to the power of {b} is: {result}")
    else:
        print("Invalid choice. Please select a valid operation.")

    # Ask the user if they want to perform another operation
    again = input("Do you want to perform another operation? (Y/N): ").strip().upper()
    if again != 'Y':
        print("Exiting the program.")
        break'''


#---------------------------------------------------------------------------------------------
#3- program to check if a number is prime or not using a while loop
#---------------------------------------------------------------------------------------------
'''
while True:
    n = int(input("Enter a number to check if it is prime: "))
    if n <= 1:
        print(f"{n} is not a prime number.")
    else:
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is not a prime number.")
    
    # Ask the user if they want to check another number
    again = input("Do you want to check another number? (Y/N): ").strip().upper()
    if again != 'Y':
        print("Exiting the program.")
        break
#---------------------------------------------------------------------------------------------
#4- program to generate the Fibonacci sequence up to a specified number of terms
#---------------------------------------------------------------------------------------------
n = int(input("Enter the number of terms for the Fibonacci sequence: "))
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
          '''
#---------------------------------------------------------------------------------------------
#4- Calculator using functions and a loop plus Continuous User Input (The "Keep Asking" Loop)
#---------------------------------------------------------------------------------------------
'''
while True:
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    choice = input("Enter your choice (1-5): ")
    if choice in ['1', '2', '3', '4', '5']:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
    else:
        print("Invalid choice. Please select a valid operation.")
        continue

    def sum_values(x, y):
        return x + y

    def difference(x, y):
        return x - y

    def product(x, y):
        return x * y

    def quotient(x, y):
        if y != 0:
            return x / y
        return "Error: Division by zero is not allowed."

    def modulus(x, y):
        if y != 0:
            return x % y
        return "Error: Modulus by zero is not allowed."

    if choice == '1':
        print(f"The sum of {a} and {b} is: {sum_values(a, b)}")
    elif choice == '2':
        print(f"The difference between {a} and {b} is: {difference(a, b)}")
    elif choice == '3':
        print(f"The product of {a} and {b} is: {product(a, b)}")
    elif choice == '4':
        print(f"The quotient of {a} divided by {b} is: {quotient(a, b)}")
    elif choice == '5':
        print(f"The modulus of {a} and {b} is: {modulus(a, b)}")
    else:
        print("Invalid choice. Please select a valid operation.")

    again = input("Do you want to perform another operation? (Y/N): ").strip().upper()
    if again != 'Y':
        print("Exiting the program.")
        break
        '''
#---------------------------------------------------------------------------------------------
#5- Continuous User Input (The "Keep Asking" Loop)
#In Python, a while True loop creates an infinite loop, meaning the code inside it will run forever
#unless you intentionally stop it. To prevent the program from getting stuck, developers typically
# use a break statement to exit the loop when a specific condition is met
#---------------------------------------------------------------------------------------------
'''
while True:
    text = input("Enter text (or 'quit' to exit): ")
    if text.strip().lower() == "quit":
        print("Exiting the program.")
        break
    print(f"You entered: {text}")
    '''
#---------------------------------------------------------------------------------------------
#6- Basic Input Validation
#---------------------------------------------------------------------------------------------

""" while True:
    age_input = input("Please enter your age: ")
    
    if age_input.isdigit():
        age = int(age_input)
        print(f"Thank you! Your age is recorded as {age}.")
        break  # Only exits if the input is a valid number
    else:
        print("That is not a valid number. Try again.") """

#---------------------------------------------------------------------------------------------
#7- creating a simple counter using while True
#---------------------------------------------------------------------------------------------
'''
counter=1
while True:
    print(f'iteration nbre:{counter}')
    counter=counter+1
    if counter == 5 :
        print(f"you made it to the {counter}th iteration, Stopping the loop")
        break
    '''
#---------------------------------------------------------------------------------------------
#8- Difference between While True and standard While , this program is done by standard while
#---------------------------------------------------------------------------------------------
'''
temperature = 100
while temperature > 50:
    print(f"Temperature is {temperature}°C. Cooling down...")
    temperature -= 10
print(f"The water has cooled to {temperature}°C. Loop stopped.")
print("the end of the program")
'''
#---------------------------------------------------------------------------------------------
#9- Armstrong Number Check
#---------------------------------------------------------------------------------------------

""" while True :

        n=int(input("Enter a value to check if it is an Armstrong Nbre : "))
        # n=153
        p=str(n) # Convert to string to make it iterable
        s=0
        for i in p:
            digit=int(i) # Convert back to an integer to use it as a number
            s=s+digit**3 
        if s==n:
            
            print(f"{n} is equal to {s}, so {n} is an Armstrong nbre")
        else:
            print(f"{n} is not equal to {s}, so {n} is not an Armstrong nbre")

        print(s)
        print(len(p))


        text = input(" Enter 'quit' to exit or 'stay' to Continue : ")
        if text.strip().lower() == "quit":
            print("Exiting the program.")
            break
        elif text.strip().lower() == "stay":
             print("\n\n\n\n")
             print(f"Since you did not choose to quit the program,\n We are goig to run the program again for you \n......  ")
             
             continue
        else:
             print(f"Make sure you entered the right choice my friend .") """            
             


""" print("Number Pattern:")

# Outer loop for the number of rows
for i in range(1,      6):
    # Inner loop to print numbers in each row
    for j in range(1, i + 1):
        print(j, end=' ')
    # Move to the next line after each row is printed
    print("") """

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

e = np.array([1, 2, 3, 4, 5], ndmin=5)
f = np.array([1,2,3,4,5,6,7])


'''print(a)
print(type(a))
print(a.ndim)

print(b)
print(b[0])
print(b.ndim)
print(type(b))

print(b[0]+b[1])

print(c)
print("2nd element on 1st row of c:", c[0, 1])
print('5th element on 2nd row: ', c[1, 4])
print(type(c))
print(c.ndim)

print(d)    
print(type(d))
print(d.ndim)

print(e)
print(type(e))
print(e.ndim) '''

print('Last element from 2nd dim: ', f[1,-1]) 
print(f[1:5])










            


      

      



              
                     
        



           
    













    
      
      




    
   
