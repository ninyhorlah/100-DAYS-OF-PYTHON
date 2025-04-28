import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
score = Scoreboard()
# car2 = CarManager()
# car3 = CarManager()
# car4 = CarManager()
# car5 = CarManager()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.is_finish_line():
        player.next_stage()
        car.level_up()
        score.increase_score()

    # car.multiple_cars()


    


screen.exitonclick()