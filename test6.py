# Python Loops Exercises: 40+ Coding Problems with Solutions
#https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/
# ----------Exercise01-----------------------
""" 
def my_function(a,b,c):
      i=a
      while i<=c:
            i+=b
            print(i)
my_function(0,2,20)
my_function(10,10,500) """
#------------Exercise02-----------------------
""" for i in range(-10,0):
      print(i) """
#------------Exercixe03-------------------------
""" 
for i in range(0,5):
      print(i)
else:
      print('Done!') """
#----Exercises04-Calculate sum of all numbers from 1 to N---------------------
""" 
n=int(input("what is you number :"))
s=0
for i in range(n+1):
      s+=i
print(s) """
#----------Exercises05--Print multiplication table of a given number--------------------------------
""" 
def Multiplication(n, j):
    for i in range(1, j + 1):
        M = n * i
        print(f"{n} X {i} = {M}")

def user_input():
    x = int(input("what table multiplication you wanna perform ?? "))
    y = int(input("what is the limit of your table ?? "))
    return x,y
    
while True:
    x, y = user_input()
    Multiplication(x, y)
    print("Processing data...")

    # Validation loop for the Y/N prompt
    while True:
        choice = input("Run again? (Y/N): ").strip().upper()
        if choice in ('Y', 'N'):
            break # Valid choice, break out of validation loop
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        
    # Act on the valid choice
    if choice == 'N':
        print("Exiting program.")
        break
    
    print("Starting next round...\n")  """
#----------------Exercise6:------------------------------------------
""" 
def myfunction(x,y):
      for i in range(1,x+1):
            c=pow(i,y)
            print(f"current nbre is : {i} and the cube is {c} ")
while True:
    myfunction(int(input("How many times u will run the program for ")),int(input("Enter the Exponent ")))

    
    print("Processing data...")

    # Validation loop for the Y/N prompt
    while True:
        choice = input("Run again? (Y/N): ").strip().upper()
        if choice in ('Y', 'N'):
            break # Valid choice, break out of validation loop
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        
    # Act on the valid choice
    if choice == 'N':
        print("Exiting program.")
        break
    
    print("Starting next round...\n")  """
#------------------Exercise7--------------------------------------------
""" 
def get_valid_integer(prompt):
    while True:
        try:
            # Try to convert the input to an integer
            user_input = int(input(prompt))
            return user_input  # Exit the loop and return the valid number
        except ValueError:
            # Run this if the conversion fails
            print("Invalid input! Please enter a whole number.")



age = get_valid_integer("Enter your age (integer): ")
print(f"Age successfully saved as: {age} (Type: {type(age).__name__})")

def get_valid_float(prompt):
    while True:
        try:
            # Try to convert the input to a float (decimal)
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input! Please enter a valid decimal or number.")


price = get_valid_float("Enter the item price (decimal): ")
print(f"Price successfully saved as: ${price:.2f} (Type: {type(price).__name__})")

def get_letters_only(prompt):
    while True:
        user_input = input(prompt).strip()  # .strip() removes accidental spaces at the start/end
        
        # .isalpha() checks if the string contains ONLY letters
        if user_input.isalpha():
            return user_input
        else:
            print("Invalid input! Please enter letters only (no numbers or symbols).")

first_name=get_letters_only("Enter you first name")
print(f"you entered this name: {first_name} ")

def get_none_blank_string(prompt):
    while True:
        user_input = input(prompt).strip()  # .strip() removes accidental spaces at the start/end
        
        if user_input!="":
            return user_input
        else:
            print("Invalid input! this field cannnot left blank")

Address = get_none_blank_string("Enter your Address :")
print(f"Here is your Address: {Address}") """
#-----------------Exercise 8--------------------------------------------------
""" 
numbers = [12, 75, 150, 180, 105, 525, 50]

print(f"This lIST Contain {len(numbers)} elements")
print("here is the result for the 1st method")
for i in range(len(numbers))  :
    if numbers[i] > 500:
        break
    if numbers[i] > 150:
        continue
    if numbers[i] % 5 == 0:
        print(numbers[i])
print("here is the result for the second method")
for j in numbers:
    if j > 500:
        break
    if j > 150:
        continue
    if j % 5 == 0:
        print(j) """
#----------------------Exercise9--------------------------------------------------
""" list1 = [10, 20, 10, 30, 10, 20, 10, 30, 10, 40, 50]
target=20
count=0
for i in list1:
      if i==target:
            count+=1
      else:
            continue
print(f"{count}  is how many {target}'s we have on the list")
print("done") """
#-----------------------------------Exercise10----------------------------------------
""" my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(1,len(my_list),2):
      print(my_list[i],end=" ") """
#-------------------Exercise11-----------------------------------------------------
"""
word='Python'
new_word=''
for i in word:
      print(i,end="    ")
      print()
      new_word=i+new_word
print(f"Original word:{word}")
print(f"reversed word:{new_word}")

print(len(word))
pos=word.index("h")
print(pos) """
#-------------------Exercise12-----------------------------------------------------
""" 
print("Hello World".isalpha())
print("pyt1hon".isalpha())

Given_Input = "Count vowels and consonants in a sentence"
vowels="aoiue"
c=0
v=0
for i in Given_Input:
      if i.isalpha():
            if i in vowels:
                  v+=1
            else:
                  c+=1
      else:
            continue
                 
      

print(f"nbre of vowels in this string is : {v}")
print(f"nbre of Consonants in this string is : {c}") """
#-------------------Exercise13-----------------------------------------------------'
""" 
given_input=1542154
counter=1
while given_input>10:
      given_input//=10
      counter+=1

print(counter)
 """
#-------------------Exercise14-15-----------------------------------------------------
#this program will take a number and print the largest and smallest digit in that number,
#  as well as the reversed string of the digits.
""" 
given_input=15421845
digits = str(given_input)
reversed_string=""
largest_digit = digits[0]
smallest_digit = digits[0]

for i in range(len(digits)):
      print(digits[i], end=" ")
      reversed_string = digits[i] + reversed_string

for i in range(1, len(digits)):
      if digits[i] > largest_digit:
            largest_digit = digits[i]
      elif digits[i] < smallest_digit:
            smallest_digit = digits[i]

print(f"Largest digit in the number is : {largest_digit}")
print(f"Smallest digit in the number is : {smallest_digit}")
print(f"Reversed string: {reversed_string}")
 """
#--------------------------Exercise 16--------------------------------------------------------
#8- Difference between While True and standard While , this program is done by standard while
#---------------------------------------------------------------------------------------------

""" 
given_input=int(input("Enter a number to check if it is a palindrome: "))
num_str = str(given_input)
reversed_str = num_str[::-1]

print(f"Original number: {num_str}")
print(f"Reversed number: {reversed_str}")

if num_str == reversed_str:
    print(f"{given_input} is a palindrome.")
else:
    print(f"{given_input} is not a palindrome.") """

#---------------------------Exercise 17------------------------------------------------------------------
#2-this program will calculate the factorial of a nbre using a while loop
#---------------------------------------------------------------------------------------------
""" 
while True:
    n=int(input("Enter a number to calculate its factorial: "))
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print(f"The factorial of {n} is: {factorial}")

# Ask the user if they want to check another number
    again = input("Do you want to check another number? (Y/N): ").strip().upper()
    if again != 'Y':
        print("Exiting the program.")
        break
 """

#---------------------------Exercise 18------------------------------------------------------------------
# This program will check if a nbre is Armstrong
#---------------------------------------------------------------------------------------------

""" 
while True :

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
#---------------------------Exercise 20------------------------------------------------------------------
#Print right-angled triangle Number Pattern using a Loop
#--------------------------------------------------------------------------------------------------------
""" 
print("Number Pattern:")

# Outer loop for the number of rows
for i in range(1, 6):
    # Inner loop to print numbers in each row
    for j in range(1, i + 1):
        print(j, end=' ')
    # Move to the next line after each row is printed
    print("") """

#---------------------------Exercise 21------------------------------------------------------------------
#Arithmetic Product and Conditional Logic
#--------------------------------------------------------------------------------------------------------
""" 
a=int(input("eneter a nbre1: "))
b=int(input("eneter a nbre2: "))
if a*b <= 1000:
      print(f"product of the two nbres is less than 1000 so result =  {a*b}")
else:
      print(f"the product  of the two nbres is greater than 1000 so result =  {a+b}") """

#---------------------------Exercise 22------------------------------------------------------------------
#Arithmetic Product and Conditional Logic
#--------------------------------------------------------------------------------------------------------


""" print("Number Pattern:")
rows=6


for i in range(rows+1):
    
    for j in range(1,i):
        print(j, end=' ')
    
    print("") """


#---------------------------Exercise 22------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------------------------

""" list=[1,2,3,4]
list1=[]
for i in list:
      for j in len(list):
            
        list1[j]=list[i]+list[i+1]

print(list1) """

#---------------------------Exercise 22------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------------------------


    













