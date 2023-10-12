# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".

def my_function(name): 
    print("Hello " + name)

my_function("chicken")

#  using the function to hold the value for name and input it

# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.


def sum_numbers(a,b):
    print (a + b)
   
sum_numbers(1,2)
# used the function to hold the values of a and b

# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.

def factorial(n):
    factor = 1
    if n<0:
        print("error")
    elif n== 0:
        print("the factorial of 0 is 1.")
    else:
        while n> 0 :
            factor *+ n 
            n-=1
    print(factor)
            
#

# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.

def is_even(num):
    if num %2 == 0:
        print('True')
    else:
        print('false')
    
is_even(5)
# used the  function to a hold a value

# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.

def calculate_area(length,width) :
  print (length * width )
  
calculate_area(2,5)
# use the function to hold the values of length and with then multiply them and print