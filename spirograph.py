import turtle as t
import random

screen = t.Screen()
t.colormode(255)
tin = t.Turtle()

def random_color():
    r = random.randint(0,250) # for red
    g = random.randint(0,250) #for green
    b = random.randint(0,250) #for blue
    random_color = (r,g,b)
    return random_color

tin.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tin.color(random_color())
        tin.circle(100)
        current_heading = tin.heading()
        tin.setheading(current_heading + size_of_gap)

draw_spirograph(5)
screen.exitonclick()
