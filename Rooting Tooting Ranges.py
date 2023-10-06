"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
for x in range(1,11):
 print(x)
# used range to print the numbers 1-10 and used 1 to start from and 11 to subtract 1 from so it stops at 10
"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
for x in range(900, 1010 , 10):
 print(x)
 # used range to print numbers 900- 1000 used 900 to start from and 1010to subtract 10 from so it stops at 1000 and used 10 so it knows to count by 10s

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
for x in range(1, 109, 9):
 print(x)
#

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
sum=0
for x in range(1,11):
    sum += x
print(x)
# the range is used to add all the values together between 1and 10

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""


rows = 5
 
for i in range(rows):
     for j in range(i + 1):
         print('*', end=' ')
     print()

     # The output is a bunch of stars that after each output increases by 1
     # The i acts as * so that when it checks the * it adds 1 morwe after each output