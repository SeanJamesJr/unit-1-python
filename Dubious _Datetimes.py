
from datetime import date, time, datetime


"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
print(datetime.now())

# date time uses now to print the current time then u set x to it and print x

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
from datetime import date, time, datetime

now = datetime.now()

year = now.strftime('%Y')
print('year:', year)

month = now.strftime('%m')
print('month:', month)

day = now.strftime('%d')
print('day:', day)
# use date time again then use str time to convert the time into a string

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
str_d1 = '2023/10/12'
str_d2 = '2023/12/12'

d1= datetime.strptime(str_d1, '%Y/%m/%d')
d2= datetime.strptime(str_d2, '%Y/%m/%d')
delta = d2 - d1
print(f'differnce is (delta.days) days ')
# use strd1 and str_d2 and make them strings then subtract d2 -d1 and print the result

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""