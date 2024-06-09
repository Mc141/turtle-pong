from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x_posistion, y_posistion):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(x_posistion, y_posistion)


    def update(self, score):
        self.clear()
        self.pendown()
        self.write(score, font=("Arial", 70, "normal"))
        self.penup()