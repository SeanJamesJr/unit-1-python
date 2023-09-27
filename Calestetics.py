'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

integer=int(input(' enter a number'))

if integer > 10 and integer %2 == 0 :
    print("True")
else:
    print('false')

    # to check if the ineteger is greater than 10 i used the greater then sign and to see if it 
    # was even i divided it by 2 and made it so if there was no remainder it was even

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
status= input(" are you a student")
integer=int(input(' enter age'))
if age > 18 or status == yes:
 print(" Price is 10$")
else:  
   print("Price is 20$")

# made it so if the age is > then 18 or the status  for student is yes the price would print 10$ and if anything else it was 20$

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

list = ['watermelon','orange','watermelon','apple']
fruitname=input("enter fruit name")
if fruitname in list:
 print("Yes, that fruit is in the list." )
else:
 print('"No, that fruit is not in the list."')

# made the user eneter a fruit and if it wasnt in the list it would print  "Yes, that fruit is in the list." and if not No, that fruit is not in the list."

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

