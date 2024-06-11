from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("rectangle")
        self.color("white")
        self.penup()

    def up(self):
        if self.ycor() <= 350:      
            new_y = self.ycor() + 50
            self.goto(self.xcor(), new_y)
    
    def down(self):
         if self.ycor() >= -350:   
            new_y = self.ycor() - 50
            self.goto(self.xcor(), new_y)