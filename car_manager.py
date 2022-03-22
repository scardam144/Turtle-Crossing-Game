from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = 0.1

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setposition(x=300, y=random.randint(-250, 250))
            self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            car.backward(STARTING_MOVE_DISTANCE)

    def check_collision(self, tim):
        for car in self.car_list:
            if tim.distance(car) < 20:
                return True

    def increase_speed(self):
        self.car_speed *= 0.7


