import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


tim = Player()

# Key control of the game
screen.listen()
screen.onkey(tim.move, "Up")
car = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(car.car_speed)
    screen.update()
    car.create_car()
    car.move()
    score.current_level()
    # check collision
    if car.check_collision(tim):
        score.game_over()
        game_is_on = False

    # level update
    if tim.ycor() > 300:
        tim.goto(0, -280)
        score.check_level()
        car.increase_speed()


screen.exitonclick()
