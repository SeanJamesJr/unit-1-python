try:
    age = int(input('Enter your age: '))
except:
  print("cant conver to integer")

faveNum = int(input('What is your favorite number: '))

if age <= 21:
 print('You are not allowed to enter, you are too young.')
else:
 print('Welcome, you are old enough.')
try:
 print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
except:  
 print(' unable to divide by 0')