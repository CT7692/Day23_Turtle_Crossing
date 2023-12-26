from turtle import Turtle
import secrets

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_NUM = 16
OFF_SCREEN = -400


class CarManager:
    car_list = []
    num_cars = STARTING_NUM
    time_counter = 0
    move_increment = 10
    spawn_interval = 6
    def __init__(self):
        self.populate_cars()

    def populate_cars(self):
        while len(self.car_list) < self.num_cars:
            car = self.get_car()
            car.setpos(x=secrets.SystemRandom().randint(a=-50, b=280), y=secrets.SystemRandom().randint(a=-240, b=270))
            self.car_list.append(car)
    def add_cars(self):
        if len(self.car_list) > 0:
            for car in self.car_list:
                car.setx(OFF_SCREEN)
            self.car_list.clear()
        self.move_increment += 2
        if self.spawn_interval > 1:
            self.spawn_interval -= 1
        self.populate_cars()


    def get_car(self):
        car_unit = Turtle()
        car_unit.up()
        car_unit.shape("square")
        car_unit.color(secrets.SystemRandom().choice(COLORS))
        car_unit.shapesize(stretch_len=2, stretch_wid=1)
        return car_unit


    def move_cars(self):
        for car in self.car_list:
            x_pos = car.xcor()
            x_pos -= self.move_increment
            car.setx(x_pos)


    def spawn_car(self):
        if self.time_counter % self.spawn_interval == 0:
            car = self.get_car()
            car.setpos(x=300, y=secrets.SystemRandom().randint(a=-250, b=250))
            self.car_list.append(car)


    def clean_up(self):
        for car in self.car_list:
            if car.xcor() < OFF_SCREEN:
                self.car_list.remove(car)
