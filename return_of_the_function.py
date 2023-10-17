"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def square(int):
  return  int**2
est=square(5)
print(est)

# use return int**2 to returnn as a square
"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def aor(length, width) :
   return length * width
taco =  aor(6,7)
print(taco)

# use retun to multiply length and with and use taco to hold  the info
"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

def temp(a): 
    # Creates function
    return (a * (9/5)) + 32 
# returns value, multiples a by (9/5), and adds 32
print(temp(1),"°C") 
# Calls function

"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
def avgNumber(a): 
    # Creates function
    total = sum(a) 
    # Retrieves total of sum of list
    avg = total / len(a) 
    # Retieves avg by dividing total by length of avg
    return avg 
# Returns avg value
    return total / len(a) 
# Returns and retieves avg by dividing total by length of avg
