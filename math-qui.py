import random
score = 0

while True:
   num1 = random.randint(1,10)
   num2 = random.randint(1,10)
   answer = num1 + num2
   guess = int(input("What is " + str(num1) + " + " + str(num2) + "? "))

   if guess == answer:
      print ("That's correct!!")
      score += 1
   else:
      print ("Sorry, that's wrong -- the correct answer is: ", answer)
      break

print ("Your total score is: ", score)

"""
In this lesson, we will create a Math Quiz that will exercise our skill with addition, subtraction and multiplication, and use that skill in a contest to see who can score the most points.  We will generate two random numbers and display a prompt asking the user to calculate the result.

The Basic Code

import random

num1 = random.randint(1,10)
num2 = random.randint(1,10)
answer = num1 + num2

guess = int(input("What is " + str(num1) + " + " + str(num2) + "? "))
if guess == answer:
   print ("That's correct!!")
else:
   print ("Sorry, that's wrong -- the correct answer is: ", answer)

Repeat this exercise using subtraction or multiplication, instead of addition, and note which "+" characters to change.

Now, let’s put that code into a loop that continues to prompt for different combinations of numbers, and we keep score until we get a wrong answer, and then we display the final summary and exit.  Add the code that is highlighted in red with yellow background.  Note the initialization and incrementation of the variable named score and pay close attention to the indentation, especially for the final summary. 

"""
