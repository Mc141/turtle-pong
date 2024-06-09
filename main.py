from turtle import Screen
from time import sleep

screen = Screen()

screen.bgcolor("black")
screen.setup(1500, 900)
screen._root.resizable(False, False)


game_is_running = True

while game_is_running:
    sleep(0.1)
    screen.update()










    screen.listen()





screen.mainloop()