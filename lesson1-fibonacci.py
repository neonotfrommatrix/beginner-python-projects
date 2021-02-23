# Use an input, if/else, a while loop, and three variables to output each term up to the nth term
# Make into a function

def FibFunc(n):
 n1 = 1
 n2 = 1
 count = 0
 if n <= 0:
   print("Enter a Positive Number")
 elif n == 1:
   print("Fibonacci sequence upto", n, ":")
 else:
   print("Fibonacci sequence upto",n,":")
   while count < n:
     print("Count"+  str(count+1) + ": " + str(n1))
     tempN = n1 + n2
     n1 = n2
     n2 = tempN
     count += 1

n = 10
n = int(input("How many terms? "))
FibFunc(n)
