
# import turtle (for 1 oe 2 objects)
# tim = turtle.Turtle()
#
# from turtle import Turtle (for more than 3 objects)
# timmy = Turtle()
# tinny = Turtle()
# tibby = Turtle()

# from turtle import * #astrick(*) means everything #try not to use it

# import turtle as t #( we are giving turtle as alias name.)
# tim = t.Turtle()

# import heroes
# import random

# DRAWING SHAPES OF DIFF COLOURS
import turtle as t
import random
tin = t.Turtle()

colours = ["red", "green", "blue", "yellow", "orange", 
          "purple", "pink", "cyan", "black", "white"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range (num_sides):
        tin.forward(100)
        tin.right(angle)

for shape_side_n in range(3,11):
    tin.color(random.choice(colours))
    draw_shape(shape_side_n)
