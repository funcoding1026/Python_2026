
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") 

# function without any parameters .
def message():
    print("Welcome to PYnative")

# call function using its name
message()

# function with parameters 
def course_func(name, course_name):
    print("Hello", name, "Welcome to PYnative")
    print("Your course name is", course_name)

# call function
course_func('John', 'Python')

# function with parameters and return value
def calculator(a, b):
    add = a + b
    substract = a - b
    product = a * b
    quotient = a / b

    return substract + add + product + quotient

# call function
# take return value in variable


print("Addition :", calculator(20, 5))
# Output Addition : 25
course_func('Ahmed', 'C++')

#-------------------------------------------------
print("Addition :", calculator(2, 15))
# Output Addition : 17

def OddEven(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

OddEven(10)
OddEven(15)
#----------------------------------------------------
def sum():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = a + b
    d= a - b
    e= a * b
    f= a / b if b != 0 else "Undefined"
    print("Sum of two numbers is:", c)
    print("Difference of two numbers is:", d)
    print("Product of two numbers is:", e)
    print("Quotient of two numbers is:", f)

for i in range(3):
    sum()
    #-----------------------------------------------------
    

from random import randint
print(randint(10, 20))

for i in range(5):
    print(randint(10, 20))

#-----------------------------------------------------

#in this program we demonstrate various types of functions in Python, including functions without parameters, functions with parameters, functions with return values, and functions that take input from the user.

def greet_user(name):
    print("Hello", name, "Welcome to PYnative")

greet_user("ahmed")
greet_user("tobias")

def greet_users(names):
    for name in names:
        print("Hello", name, "Welcome to PYnative")

greet_users(["ahmed", "tobias", "linus"])

def greet_users_with_message(names, message):
    for name in names:
        print("Hello", name, message)

greet_users_with_message(["ahmed", "tobias", "linus"], "Welcome to PYnative")

def greet_users_with_message_and_title(names, message, title):
    for name in names:
        print("Hello", title, name, message)

greet_users_with_message_and_title(["ahmed", "tobias", "linus"], "Welcome to PYnative", "Mr.")


def test_function():
    print("This is a test function")

test_function()



def another_test_function(n, start=1):
     for i in range(start, start + n):
         print(i);

another_test_function(5)


another_test_function(5, start=10)




