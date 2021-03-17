"""
In this project, we will create a Tip Calculator that can be used at a restaurant to determine how much of a tip to leave for the server, 
and also divide the total amount among multiple people.  When you dine at a restaurant, it is common to leave extra money if the server
did a great job taking care of you. 
As the customer, you get to decide how much (or how little) of a tip is appropriate based on the quality of the service, 
but typically it is 15% of the base amount of the bill.  For example, if the base amount of the bill was $10.00 and you decided to leave a 15% tip, 
the total amount would be $11.50.  Then, if you were part of a group of several people at the same table, 
you would split that total amount equally among all of the people at the table.  
Otherwise, if there is only one person, that person should pay the entire amount.
There are a number of third-party websites that can perform these calculations, 
such as: https://tipcalculator.net/  
Allow the students a few moments to explore that website, 
then tell them that we are going to implement our own version of that using Python.

"""
while True:
   base = float(input("Enter the amount of the bill, or enter 0 to exit: "))
   if base == 0:
      break

# display a menu for various tip percentages
print("How much of a tip do you want to add? ")
print("1: 10%")
print("2: 15%")
print("3: 18%")
print("4: 20%")
choice = input()

# perform the calculations
if choice == "1":
   tip = base * 0.10
elif choice == "2":
   tip = base * 0.15
elif choice == "3":
   tip = base * 0.18
elif choice == "4":
   tip = base * 0.20
print("The tip amount is $", "{:.2f}".format(tip))
total = base + tip
print("The total amount is$", "{:.2f}".format(total))

# ask how many ways to split the bill
people = int(input("How many people should split this bill? "))
each = total / people

# display the actual amount each person should pay,
# along with a dollar sign and two decimal places
print("Each person should pay $", "{:.2f}".format(each))
print()

print("Thank you for visiting Fred's Diner -- have a nice day.")
