'''
TASK 1 Even or Odd
Determine if a number is even or odd.
'''
num=int (input("Enter any number"))
if num % 2 == 0:
    print(" That is an even number")
else:print(" tha is an odd number")

# let the put in the number than divide it by 2 because any even number can didvide by 2 and any odd number cant




'''
TASK 2 Positive, Negative, or Zero:
Determine if a number is positive, negative, or zero.

EXTRA CREDIT: Tell the user if they did not enter a valid number
'''
numb = int(input(" say any number you can think of"))
if numb > 0 :
    print(" thats a positive number")
elif numb>0 :
    print(" thats a negative number")
else:
    print(" the number is zero")
           
           # i used greater then less than and the equal then signs to tell if its positive negative or equal and printed out the result

'''
TASK 3: Largest of Three
Find and print the largest of three numbers.
'''
list = max(1,2,3,50)
print(list)

# max makes it print the biggest numbers
'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
'''
year = int(jnput("what year is it"))
if year % 4 == 0 :
 print("it is a leap year")
else:
 print("it is not a leap year")

# leap year is 4 years so divide the year by 4 and if theres no leftover its a leap year
'''
TASK 5: Vowel or Consonant:
Identify if a character is a vowel or consonant.

EXTRA CREDIT: Tell the user if they did not enter a valid letter
'''
input(" pick a letter in the alapbet to check if its a vowel or consonant")
vowel=('a','e','i','o','u')
if input == vowel:
 print('that is a vowel')
else: print("that is a consonant")

# made it identify if the word had a vowel in it by putting all the vowels in a list