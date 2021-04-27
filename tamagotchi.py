""" This project creates a small digital pet. It will ask for choices that affect it's mood and size. """



from turtle import *
 
name = input("What is your pet's name?")
lifespan = int(input("What is your pet's expected lifespan?"))
age = 0
mood = 0
size = 50
 
goto(0,0)
hideturtle()
speed(0)
 
def draw_pet(mood, size):
   mood_colors = ["red", "light salmon","white", "light blue", "medium blue"]
   clear()
   penup()
   goto(0, -size)
   pendown()
   fillcolor(mood_colors[mood+2])
   begin_fill()
   circle(size)
   end_fill()
   
   penup()
   goto(-size/2,0)
   begin_fill()
   fillcolor("black")
   circle(size/10)
   end_fill()
 
   goto(size/2,0)
   begin_fill()
   fillcolor("black")
   circle(size/10)
   end_fill()
 
   goto(-size/5,-size/5)
   right(90)
   begin_fill()
   circle(size/5,180)
   end_fill()
   right(90)


 
draw_pet(mood, size)
while(age < lifespan):
   command = input("Pet, Poke, Feed, Run, None or Quit")
   if command.lower() == "pet":
      mood += 1
      if mood > 2:
         mood = 2
   elif command.lower() == "poke":
      mood -= 1
      if mood < -2:
         mood = -2
   elif command.lower() == "feed":
      size += 10
      if size > 80:
         size = 80
   elif command.lower() == "run":
      size -= 10
      if size < 20:
         size = 20
   elif command.lower() == "none":
       pass
   elif command.lower() == "quit":
       break
   else:
      print ("Invalid input, please try again...")
      continue
   draw_pet(mood, size)
   age += 1
 
if(age >= lifespan):
   print(name, "lived to the ripe old age of", age)
