import time
from turtle import Screen
from player import Player, FINISH_LINE_Y, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

TOO_CLOSE = 20
def gameplay(player, screen_obj):
    player.setpos(STARTING_POSITION)
    screen_obj.listen()
    screen_obj.onkeypress(key="p", fun=player.move_up)
    screen_obj.onkeypress(key="l", fun=player.move_down)


def goal(player, board, screen_obj, car_manager):
    if player.ycor() >= FINISH_LINE_Y:
        player.reset_position()
        board.scored()
        screen_obj.tracer(0)
        car_manager.add_cars()
        screen_obj.update()

def hit_by_car(player, car_manager, condition):
    for car in car_manager.car_list:
        if player.distance(car) < TOO_CLOSE:
            condition = False
    return  condition


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

my_turtle = Player()
my_score = Scoreboard()
cars = CarManager()
gameplay(my_turtle, screen)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move_cars()
    cars.spawn_car()
    cars.clean_up()
    goal(my_turtle, my_score, screen, cars)
    game_is_on = hit_by_car(my_turtle, cars, game_is_on)
    cars.time_counter += 1
    if not game_is_on:
        my_score.game_over()
        screen.exitonclick()


