"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
i = 1
while i <= 10:
  print(i)
i += 1

# first i made a variable

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""

i = 1
while i >= 10:
  print(i)
  i -= 1

# similar to1 i did a variable with 10 then in while loop kept talking 1 away and also printing it

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""

product = 1
fact = int(input("pick a integer"))

while fact >1:
  product = fact * product
  fact -= 1 
  print('product')

  #
"""
# let them put the inetegr then while the integer(fact) is greater than 1 its is multiplied by the product(1) then prints the product

4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
c=''
while c != 'apples':
  c=input('guess the password')
  if c =='apples':
    print('congrats')
  else:
    print('try again')

# first i made a empty variable then a while loop to guess one word until they get it right

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
a='Start'
while a != 'Stop':
   value = input('give a number')
   value2= input("give me a second number")
   print(int(value)+int(value2))

#

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""


