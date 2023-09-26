print("Welcome to the Calculatinator-inator 9000!")

first=input("Enter the first number")
second=input("Enter the first number")

# added the inputs first and second so that the code is numbers to use for functions

print(" Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponential")
print("7. Remainder")

# say the functions and give them numbers so that the user knows what to input

Choice=input("Enter choice")

# choice is ehat the user uses to pick what function they want to do


if Choice == 1 :
 print( first + second)
elif  Choice == 2 :
 print( first - second)
elif Choice == 3 :
 print ( first * second)
elif Choice == 4 :
  print(first / second ) 
elif Choice == 5 :
 print(first// second)
elif Choice == 6 :
 print(first ** second)
elif Choice == 7 :
  print( first % second) 
else:
 print("Error, This is not a option pick from the Options avaliable")
 #it gives the if a choice based on what the user wants to do