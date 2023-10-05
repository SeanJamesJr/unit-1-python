"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
chicken= 'yo'
for x in chicken :
 print(x)

#  using the x it prints the amount of characters in the list

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""

num= [1,2,3]
sum = 0
for x in num:
 sum +=x
 print(sum)
 
 #set the sum to zero then for the amount of items in num  then use + to equal sum to whats on the other side of the =

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
word= "sean likes food"
word =word.split(" ")
for x in word:
 print(x) 
 print(len(x))

# used word.split in order to make it a list then did the empty with a space so it identifies the seperated words then len breaks down the words and says how long it ia

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result


In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
black={
  'chicken' : 7,
  'collard greens' : 3

}
for x in  black :
 print(x)

 # It didnt print the amount of items in the dictionary, It isnt what i expected cause i tjought it was gonna print the amount to