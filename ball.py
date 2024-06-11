from turtle import Turtle
from random import randint

right_angle = [randint(0, 70), randint(290, 360)]
left_angle = randint(120, 250)
angles = [left_angle, right_angle[randint(0, 1)]]
strating_angle = angles[randint(0, 1)]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(1.3)
        self.setheading(strating_angle)


    def change_direction(self):
        current_direction = self.heading()
        if current_direction <= 180:
            new_direction = current_direction + randint(10, 120)
        else:
            new_direction = current_direction + randint(130, 280)