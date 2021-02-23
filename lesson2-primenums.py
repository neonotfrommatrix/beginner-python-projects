for i in range (1, 100):           # main loop with index ("i") going from 2 to 100 (skip 1)
   prime_flag = True               # 1=TRUE, 0=FALSE; assume it's prime unless proven otherwise
   for divisor in range(2, i-1):   # scroll through all possible divisors from 2 to i-1
      if i % divisor == 0:         # if "i" is exactly divisible by some smaller divisor 
         prime_flag = False        # then it is NOT prime, so set the prime_flag to 0 and
         break                     # break out of the loop if that the number is not prime
   if prime_flag:                  # if the prime_flag is still true...
      print(i)                     # then print the value of "i" as a prime number
      
      """
      
      LESSON PLAN
      
1. What is a "prime number" (a number that is only divisible by 1 and itself), and illustrate the first 10 (or so) examples manually on a white board;  see how far they can go toward 100, and show that it’s a lot of work; a computer can do the job much faster and more accurately than humans (if we write the code properly to make that happen)
2. An "algorithm" is a scientific method for solving a problem; we use code to implement the logic of the algorithm; in this case dividing the original number by all numbers less than the original number, and if there is a zero remainder (meaning it is evenly divisible), then the original number is NOT PRIME.  In this case, we use the “modulo” operator (%) to determine if a number is evenly divisible by another number.
4. Review the syntax rules for FOR loops, including the RANGE function, the trailing colon, and proper indentation of the lines that follow, and how the index goes from the starting value up to BUT EXCLUDING the ending number, so to go from 1 to 100, the RANGE function must include (1, 101)
5. Instead of just printing the value of i, print a more descriptive line, such as “7 is a Prime Number” (review the syntax rules for a PRINT statement with a mixture of values and text strings), so the final two lines become:

   if prime_flag:
      print(i, "is a Prime Number")

6. Review the syntax rules for an IF statement, including "==" for comparing two values, the trailing colon, and proper indentation of the lines that follow
7. Discuss how using a variable as a “flag” (typically boolean) is helpful
8. Also review why using descriptive variable names is a really good coding practice
9. Ask the students what they would change to make it show all Prime numbers from 2 to 1000, and allow them to try it (be sure to set the ending number to 1001 instead of 1000).  Some of them will no doubt want to try using huge numbers that may end up crashing REPL.  We should remind them that if they want to use huge numbers, they cannot eat, drink, sleep or go to the bathroom while it’s running.
10. Ask the students to PRINT a message if the number is NOT a Prime Number

   if prime_flag:
      print(i, "is a Prime Number")
   else:
      print (i, "is not a Prime Number")
11. Ask the students how they would COUNT the number of Prime numbers in a specified range:
Updated Code
num_primes = 0
for i in range(1,1001):
 prime_flag = True
 for divisor in range(2, i-1):
    if i % divisor == 0:
       prime_flag = False
       print (i, "is not a Prime Number")
       break
 if prime_flag:
    print(i, "is a Prime Number")
    num_primes += 1
 
print("There are a total of", num_primes, "prime numbers.")

Note: we moved the PRINT statement for NOT a Prime Number inside the loop in which we perform the modulo calculation, to simplify the code.


12. For the more advanced students only, we can use a function named "isPrime( )" that returns either True or False, which will results in much tighter and cleaner code:

def isPrime(number):
   for divisor in range(2, number-1):
      if number % divisor == 0:
         return False
   return True
 
num_primes = 0
for i in range(1,101):
   if isPrime(i):
      print(i, "is a Prime Number")
      num_primes += 1
   else:
      print (i, "is not a Prime Number")
print("There are a total of", num_primes, "prime numbers.")
 

13. Discuss how incremental development methodology (adding new features only after the initial features are stable) helps us develop good quality code that is reliable and maintainable

      
      """
