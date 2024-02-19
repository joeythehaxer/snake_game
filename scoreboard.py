from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(0, 280)
        self.color("white")
        self.ht()
        self.score = 0

    def write_score(self):
        self.clear()
        self.write("Score: " + str(self.score), False, align="center", font=("Arial", 14, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=("Arial", 20, "normal"))
