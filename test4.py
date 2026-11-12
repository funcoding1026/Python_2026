def arithmetic(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    multiply = num1 * num2
    division = num1 / num2
    # return four values
    return add, sub, multiply, division

# read four return values in four variables
a, b, c, d = arithmetic(10, 2)

print("Addition: ", a)
print("Subtraction: ", b)
print("Multiplication: ", c)
print("Division: ", d)

def addition(num1, num2):
    # Implementation of addition function in comming release
    # Pass statement 
    pass

addition(10, 2)

global_lang = 'DataScience'

def var_scope_test():
    local_lang = 'Python'
    print(local_lang)

var_scope_test()
# Output 'Python'

# outside of function
print(global_lang)
# Output 'DataScience'

def demo(name,age):
    print("Name:", name)
    print("Age:", age)

demo("Alice", 25)

def student(name,age,grade,school):
      print("student details:",name,age,grade,school)
student("ahmed",12,89,"icc")

def user_input4():
    y = float(input(" Input First Nbre :  "))
    z = float(input(" Input Second Nbre :  "))
    return y, z


def arithmetic(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    multiply = num1 * num2
    division =int(num1 / num2)
    # return four values
    return add, sub, multiply, division

# read four return values in four variables
y, z = user_input4()
a, b, c, d = arithmetic(num1=y, num2=z)

print("Addition: ", a)
print("Subtraction: ", b)
print("Multiplication: ", c)
print("Division: ", d)
















