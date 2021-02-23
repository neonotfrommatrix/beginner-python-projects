def consecSum(num):
 count = 0          #This is the sum that will be returned by the method
 i = 0              #This is the index that will increase for the numbers below the num input
 while i <= num:    #We check for i as the numbers below num and num
   count += i       #We increase the sum by i
   i += 1           #We increase i for the next enumeration
 return count       #We return count
print("The sum of all positive numbers up to 8 is " + str(consecSum(8)))  #We print out the returned value. We could also start off without a defined function and then introduce it afterwards to reinforce learning how to define functions

def reverseSum(num):
 count = 0
 i = num
 while i >= 1:
   count += i
   i -= 1
 return count
print("The sum of all positive numbers up to 5 is " + str(reverseSum(5))) #Functionally the same as the above, except the while loop acts in reverse

def forConsecSum(num):
 count = 0
 for i in range(num + 1):
   count += i     
 return count      
print("The sum of all positive numbers up to 13 is " + str(forConsecSum(13))) #Functionally the same as the top, except with a for loop

def forReverseSum(num):
 count = num
 total = 0
 for i in range(num + 1):
   total += count
   count -= 1   
 return total      
print("The sum of all positive numbers up to 4 is " + str(forReverseSum(4))) #Functionally the same as the second from the top,except with a for loop





"""
Lesson Plan:
We review the operators += and -= and how they can be used to modify the existing values of variables
Relate the above operators to var = var (+-) num
Review while loops and how they can be used for when a condition is met (especially with numeric variables using <=, >=, <, and >
Go over the main problem with adding consecutive numbers up to the specified number (ex: The input is 4, so we add 1 + 2 + 3 + 4 which equals 10 so we return 10)
Ask them to combine while, the += and -= assignment operators to return the consecutive number sum given an input number (give the hint of there being two variables, with one being tested for in the while loop)
Also point them in the direction that we have to increase the same variable by 1 inside the loop
Get them to turn this into a function
Repeat for the reverse consecutive sum that moves the opposite way through the while loop
Reintroduce the for loop (the students should already know about it) and have them rewrite the problem two ways (normal and reverse) using for loops


"""
