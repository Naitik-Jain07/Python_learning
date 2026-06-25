from turtle import Turtle , Screen
tin = Turtle()
screen = Screen()

def move_forwards():
    tin.forward(10)

def move_back():
    tin.backward(10)

def move_clockwise():
    tin.right(10)

def move_counterclockwise():
    tin.left(10)

def clear():
    tin.setpos(0, 0)
    tin.clear()


screen.listen()
screen.onkey(move_forwards,'w')
screen.onkey(move_back,'s')
screen.onkey(move_clockwise,'d')
screen.onkey(move_counterclockwise,'a')
screen.onkey(clear,'c')
screen.exitonclick()