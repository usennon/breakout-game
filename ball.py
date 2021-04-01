from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.speed(2)
        self.shape('circle')
        self.color('white')
        self.goto(0, 0)
        self.x_cor = 10
        self.y_cor = -10

    def move(self):
        self.goto(x=self.xcor() + self.x_cor, y=self.ycor() + self.y_cor)

    def bounce(self):
        self.y_cor *= - 1

    def bounce_x(self):
        self.x_cor *= - 1

    def reset_position(self):
        self.goto(0, -30)
        self.bounce_x()