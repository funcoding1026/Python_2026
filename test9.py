


# this program will define an enpty vehicle class and demonstrate its usage.
class vehicle:
    def __init__(self,wheels=0,doors=0,color=""):
        self.wheels = wheels
        self.doors = doors
        self.color = color

    def display_info(self):
        print(f"Wheels: {self.wheels}, Doors: {self.doors}, Color: {self.color}")

# Example usage of the vehicle class
my_vehicle = vehicle(4,4,"red")
my_vehicle.display_info()

# Another example usage of the vehicle class
another_vehicle = vehicle()
another_vehicle.wheels = 2
another_vehicle.doors = 1
another_vehicle.color = "blue"
another_vehicle.display_info()

# Yet another example usage of the vehicle class
yet_another_vehicle = vehicle()
yet_another_vehicle.wheels = 6
yet_another_vehicle.doors = 2
yet_another_vehicle.color = "green"
yet_another_vehicle.display_info()

# One more example usage of the vehicle class
one_more_vehicle = vehicle()
one_more_vehicle.wheels = 3
one_more_vehicle.doors = 3
one_more_vehicle.color = "yellow"
one_more_vehicle.display_info()

# Last example usage of the vehicle class
last_vehicle = vehicle()
last_vehicle.wheels = 5
last_vehicle.doors = 5
last_vehicle.color = "purple"
last_vehicle.display_info()

# End of the program

#this new program will allow us to to add, substract , multiply and divid numbers using a simple calculator class
class calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

# Example usage of the calculator class
calc = calculator()
print(calc.add(5, 3))
print(calc.subtract(5, 3))
print(calc.multiply(5, 3))
print(calc.divide(5, 3))
print(calc.divide(5, 0))

# End of the calculator program

class person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Example usage of the person class
my_person = person("John Doe", 30)
my_person.display_info()

# Another example usage of the person class
another_person = person()
another_person.name = "Jane Smith"
another_person.age = 25
another_person.display_info()

# Yet another example usage of the person class
yet_another_person = person()
yet_another_person.name = "Alice Johnson"
yet_another_person.age = 28
yet_another_person.display_info()

# One more example usage of the person class
one_more_person = person()
one_more_person.name = "Bob Brown"
one_more_person.age = 35
one_more_person.display_info()

# Last example usage of the person class
last_person = person()
last_person.name = "Eve Davis"
last_person.age = 32
last_person.display_info()

# End of the person program

class animals:
    def __init__(self, name="", species=""):
        self.name = name
        self.species = species

    def display_info(self):
        print(f"Name: {self.name}, Species: {self.species}")

# Example usage of the animals class
my_animal = animals("Lion", "Carnivore")
my_animal.display_info()

# Another example usage of the animals class
another_animal = animals()
another_animal.name = "Elephant"
another_animal.species = "Herbivore"
another_animal.display_info()

# Yet another example usage of the animals class
yet_another_animal = animals()
yet_another_animal.name = "Tiger"
yet_another_animal.species = "Carnivore"
yet_another_animal.display_info()

# One more example usage of the animals class
one_more_animal = animals()
one_more_animal.name = "Giraffe"
one_more_animal.species = "Herbivore"
one_more_animal.display_info()

# Last example usage of the animals class
last_animal = animals()
last_animal.name = "Zebra"
last_animal.species = "Herbivore"
last_animal.display_info()

# End of the animals program

#compare two nbres using class
class compare_numbers:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def compare(self):
        if self.a > self.b:
            return f"{self.a} is greater than {self.b}"
        elif self.a < self.b:
            return f"{self.a} is less than {self.b}"
        else:
            return f"{self.a} is equal to {self.b}"

# Example usage of the compare_numbers class
comparison = compare_numbers(5, 10)
print(comparison.compare())

# Another example usage of the compare_numbers class
comparison2 = compare_numbers(15, 15)
print(comparison2.compare())

# Yet another example usage of the compare_numbers class
comparison3 = compare_numbers(20, 10)
print(comparison3.compare())

# One more example usage of the compare_numbers class
comparison4 = compare_numbers(0, 0)
print(comparison4.compare())

# Last example usage of the compare_numbers class
comparison5 = compare_numbers(-5, 5)
print(comparison5.compare())

# End of the compare_numbers program

# here is another class that calculate factorial
class factorial:
    def __init__(self, n=0):
        self.n = n

    def calculate(self):
        result = 1
        for i in range(1, self.n + 1):
            result *= i
        return result

# Example usage of the factorial class
fact = factorial(5)
print(fact.calculate())

# Another example usage of the factorial class
fact2 = factorial(0)
print(fact2.calculate())

# Yet another example usage of the factorial class
fact3 = factorial(10)
print(fact3.calculate())

# One more example usage of the factorial class
fact4 = factorial(3)
print(fact4.calculate())

# Last example usage of the factorial class
fact5 = factorial(7)
print(fact5.calculate())

# End of the factorial program

#program to calculate the sum of the first n natural numbers using a class
class sum_natural_numbers:
    def __init__(self, n=0):
        self.n = n

    def calculate(self):
        result = 0
        for i in range(1, self.n + 1):
            result += i
        return result

# Example usage of the sum_natural_numbers class
sum1 = sum_natural_numbers(5)
print(sum1.calculate())

# Another example usage of the sum_natural_numbers class
sum2 = sum_natural_numbers(0)
print(sum2.calculate())

# Yet another example usage of the sum_natural_numbers class
sum3 = sum_natural_numbers(10)
print(sum3.calculate())

# One more example usage of the sum_natural_numbers class
sum4 = sum_natural_numbers(3)
print(sum4.calculate())

# Last example usage of the sum_natural_numbers class
sum5 = sum_natural_numbers(7)
print(sum5.calculate())

# End of the sum_natural_numbers program

class person:
    def __init__(self,name,age,city,country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}, Country: {self.country}")

p1=person("Linus", 30, "Oslo", "Norway")
print(p1.name, p1.age, p1.city, p1.country)

# Another example usage of the person class
p2=person("Alice", 25, "Paris", "France")
print(p2.name, p2.age, p2.city, p2.country)

# Yet another example usage of the person class
p3=person("Bob", 40, "New York", "USA")
print(p3.name, p3.age, p3.city, p3.country)

# One more example usage of the person class
p4=person("Charlie", 35, "London", "UK")
print(p4.name, p4.age, p4.city, p4.country)

# Last example usage of the person class
p5=person("Diana", 28, "Tokyo", "Japan")
print(p5.name, p5.age, p5.city, p5.country)

# End of the person program


