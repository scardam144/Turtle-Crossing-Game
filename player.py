from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.setposition(STARTING_POSITION)
        self.move()

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)


