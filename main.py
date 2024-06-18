from turtle import Screen
from turtle import Turtle
from time import sleep
from ball import Ball
from player import Player
from scoreboard import Scoreboard
from random import randint

screen_width = 1500
screen_height = 900

screen = Screen()

screen.bgcolor("black")
screen.setup(screen_width, screen_height)
screen._root.resizable(False, False)
screen.tracer(0)
screen.title("Pong")

turtle = Turtle()
turtle.color("white")
turtle.speed("fastest")
turtle.pensize(5)
turtle.right(90)
turtle.penup()
turtle.goto(0, screen_height/2 - 50)
turtle.hideturtle()

rectangle_shape = ((40, -10), (-40, -10), (-40, 10), (40, 10))
screen.register_shape('rectangle', rectangle_shape)

ball = Ball()
player_1 = Player()
player_2 = Player()

player_1.goto(-screen_width/2 + 50, 0)
player_2.goto(screen_width/2 - 60, 0)


player_1_score = 0
player_2_score = 0

player_1_scoreboard = Scoreboard(-100, screen_height/2 - 120)
player_1_scoreboard.update(player_1_score)

player_2_scoreboard = Scoreboard(50, screen_height/2 - 120)
player_2_scoreboard.update(player_2_score)






for number in range(1, 21):
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)







    screen.onkey(player_1.up, "w")
    screen.onkey(player_1.down, "s")
    screen.onkey(player_2.up, "Up")
    screen.onkey(player_2.down, "Down")
    screen.listen()








game_is_running = True

while game_is_running:
    
    sleep(0.07)
    screen.update()






    if ball.ycor() >= 400:
        ball.setheading(randint(200, 340))
    elif ball.ycor() <= -400:
        ball.setheading(randint(20, 160))





    ball.forward(30)










screen.mainloop()