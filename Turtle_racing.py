import random
from turtle import Turtle , Screen
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= 'Make ur bet', prompt='Which turtle is gonna win race. Enter colour:')
is_race_on = False
all_turtles = []

colours = ['red','green','blue','yellow','orange','pink']
y_position = [-70 , -40 , -10 , 20 , 50 , 80]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

        if turtle.xcor()>230:
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print("You win!")

            else:
                print("You lose!")
            is_race_on = False

screen.exitonclick()