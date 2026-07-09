FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level= 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.clear()
        self.level +=1
        self.penup()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)




