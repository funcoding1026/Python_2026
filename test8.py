text = input("Enter a string: ")
reversed_text = text[::-1]
c=len(text)//2

if text:
      
      result1=text[0]+text[c]+text[-1]
      result2=text[c-1]+text[c]+text[c+1]


print(result1)
print(result2)


print("Reversed string:", reversed_text)


y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")


#this program will calculate the sum of two nbres 

def sum(a,b):
   return a+b
print(sum(3,4))

def substract(a,b):
   return a-b
print(substract(3, 4))

def product(a, b):
   return a * b


from abc import ABC, abstractmethod


class b(ABC):
   @abstractmethod
   def add(self, a, b):
       return a + b

   @abstractmethod
   def is_even(self, value):
       return value % 2 == 0

# This is an abstract base class with two abstract methods: add and is_even.

   






