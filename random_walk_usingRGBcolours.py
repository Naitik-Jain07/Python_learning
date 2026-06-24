import random
import turtle as t


tin = t.Turtle()
t.colormode(255) #U DONT HAVE TO CALL OBJ BUT THE MODULE AND CHANGE THE COLOUR OF THE MODULE

def random_color():
    global tin
    r = random.randint(0,250) # for red
    g = random.randint(0,250) #for green
    b = random.randint(0,250) #for blue
    random_color = (r,g,b)
    return random_color

direction = [ 0 , 90 , 180 , 270 ]
tin.pensize(5)
tin.speed("fastest")

for _ in range(200):
    tin.color(random_color())
    tin.forward(30)
    tin.setheading(random.choice(direction))