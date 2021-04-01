from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.score_update(self.score)

    def score_update(self, points):
        self.score += points
        self.clear()
        self.goto(x=250, y=300)
        self.write(self.score, font=('Courier', 60, 'normal'))