from turtle import Turtle


FONT = ("Courier", 24, "normal")
POSITION = (-215, 240)
ALIGNMENT = "center"

class Scoreboard(Turtle):
    level = 1
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color("black")
        self.setpos(POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def scored(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.setpos(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)