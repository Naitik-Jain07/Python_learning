from turtle import Turtle , Screen
tin = Turtle()
screen = Screen()

def move_forward():
    tin.pendown()
    tin.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
#higher order function is function that operates with other minor functions
screen.exitonclick()


