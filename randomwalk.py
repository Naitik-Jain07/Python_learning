import turtle as t
import random
tin = t.Turtle()

colours = ["red", "green", "blue", "yellow", "orange", 
          "purple", "pink", "cyan", "black", "white"]
tin.pensize(5)
tin.speed("fastest")

direction = [0 , 90 , 180 , 270]
for _ in range(200):
    tin.forward(30)
    tin.setheading(random.choice(direction))
    tin.color(random.choice(colours))
    
