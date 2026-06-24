# import colorgram
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

screen = t.Screen()
t.colormode(255)

tinny = t.Turtle()
tinny.speed("fastest")
tinny.hideturtle()
tinny.penup()
color_list = [(231, 206, 85), (218, 229, 219), (231, 222, 226), (224, 150, 89),
              (215, 224, 230), (120, 166, 185), (159, 14, 21), (34, 110, 157), (232, 82, 46)]
starting_x = -200
starting_y = -200
tinny.setpos(starting_x, starting_y)

def draw_dot():
    tinny.fillcolor(random.choice(color_list))
    tinny.begin_fill()
    tinny.circle(10)
    tinny.end_fill()

for row in range(10):
    for col in range(10):
        draw_dot()
        tinny.forward(50)
    tinny.setpos(starting_x, starting_y + (row + 1) * 50)

screen.exitonclick()