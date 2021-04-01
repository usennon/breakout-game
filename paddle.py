from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super(Paddle, self).__init__()
        self.penup()
        self.speed('fastest')
        self.color('white')
        self.shape('square')
        self.goto(x, y)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def move_left(self):
        self.backward(40)

    def move_right(self):
        self.goto(x=self.xcor() + 40, y=self.ycor())