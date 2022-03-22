from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0

    def current_level(self):
        self.goto(-150, 150)
        self.write(f"Level:{self.level}", align="center", font=("Courier", 25, "normal"))

    def check_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level:{self.level}", align="center", font=("Courier", 25, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game-Over", align="center", font=("Courier", 70, "normal"))


