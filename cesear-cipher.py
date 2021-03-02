offset = 1
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def encrypt(text, offset):
   result = ""
   for letter in text:
      position = characters.find(letter)
      if position >= 0:
         result += characters[(position + offset) % len(characters)]
      else:
         result += letter
   return result

text = input("Enter a text string to be encrypted: ")
print ("The encrypted text string is: ", encrypt(text, offset))


"""
we will implement the logic for a Caesar Cipher, 
which was named for Julius Caesar, who was a famous military general and statesman 
known for building the Roman Empire over 2,000 years ago.  
The cipher allowed Julius Caesar to communicate private messages to his army commanders, 
while preventing any of his enemies from understanding the messages.  
He did this by shifting the letters of his messages by a certain number of characters, 
so that A becomes B, B becomes C, C becomes D, and so on.  We can start with lower-case letters (a-z), 
upper-case letters (A-Z), and numbers (0-9).  All other characters will remain unchanged.

"""
