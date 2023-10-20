"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class Person():
    def __init__ (self, name, age): 
     self.name = name
     self.age = age
    # makes person class and defines _innit__ with the attributes name and age

    def hello (self): # defines hello and gives the attriutes and prints name and age
        print(self.name)
        print(self.age)

Sean = Person(str("Sean"), 16)
Sean.hello()

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
class Animal(): # makes class for animal and define speak
   def speak(self) :
    print()

class Dog(Animal): # makes dog class and sets it to animal and defineds speak and gives it woof to print
   def speak(self):
      print("woof")

speak = Dog()
speak.speak()

class Cat(Animal): # makes cat class and sets it to animal and defineds speak and gives it meow to print
   def speak(self):
      print("meow")
      speak = Cat()
      speak.speak()

"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""


class BankAccount:# define banckaccount class
   def __innit__(self,balance,owner):
      self.b = balance #initialize balance
      self.o = owner# initialize owner

def balances(self):
      print( f" {self.o}'s Bank Account Balance: {self.b}") # shows starting balance
def withdraw( self,subtract):
   self.b = self.b - subtract #math function to subtract amount from original balance
   print(f" Your new balance is {self.b}")
def depoist (self,depoist):
   self.b = self.b +depoist # add anount to new balance
   print(f"your new balance is { self.b}")


