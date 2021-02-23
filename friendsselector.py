import random

friends = [
    'Arianna',
    'Michaela',
    'Lauren',
    'Gianina',
    'Kenneth',
    'Claribel',
    'Yvonne',
    'Lorie',
    'Chris'
]

# random.randint(1, 5) --> random number between 1 and 5
# print(random.choice(friends)) --> random item in this array

selected = random.choice(friends) # randomly choose a friend

print('Who should I facetime today?')
print(selected)


# import random imports the random module, which contains a variety of things to do with random number generation. Among these is the random() function, which generates random numbers between 0 and 1. Doing the import this way this requires you to use the syntax random. random()

# List
#Lists are used to store multiple items in a single variable.

#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets: [] 
# THEY ARE CHANGEABLE (ADD and MOVE ITEMS), indexed,

# example. thislist = ["apple", "banana", "cherry"]
#print(thislist)
#print(len(thislist)) gives the length of the list
