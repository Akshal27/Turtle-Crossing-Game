import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car = CarManager()
score = Scoreboard()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_car()

    for each_car in car.all_car:
        if each_car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    #Detect successful crossing

    if player.is_at_finish_line():
        car.level_up()
        player.go_to_start()


screen.exitonclick()
