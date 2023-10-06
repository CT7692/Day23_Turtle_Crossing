from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.reset_position()

    def move_up(self):
        y_pos = self.ycor()
        y_pos += MOVE_DISTANCE
        self.sety(y_pos)

    def move_down(self):
        y_pos = self.ycor()
        y_pos -= MOVE_DISTANCE
        self.sety(y_pos)

    def reset_position(self):
        self.setpos(STARTING_POSITION)