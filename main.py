from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from objectManager import ObjectManager
import time

screen = Screen()
screen.setup(width=800, height=850)
screen.bgcolor('black')
screen.title('Breakout Game')
screen.tracer(0)

paddle = Paddle(0, -250)
ball = Ball()
scoreboard = Scoreboard()
objects = ObjectManager()
objects_dict = objects.objects_generate()

screen.listen()
screen.onkey(paddle.move_left, 'a')
screen.onkey(paddle.move_right, 'd')

count = 0
speed = 0.05
game_is_on = True
checker_blue = 0
checker_orange = 0

while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()
    for i in range(8):
        try:
            for item in objects_dict[i]:
                    if ball.distance(item) < 30:
                        if objects_dict[i][-1] == 5:
                            checker_orange += 1
                            if checker_orange == 1:
                                speed *= 0.8
                                checker_orange += 1
                        elif objects_dict[i][-1] == 7:
                            checker_blue += 1
                            if checker_blue == 1:
                                speed *= 0.8
                                checker_blue += 1
                        index_pos = objects_dict[i].index(item)
                        objects_dict[i][index_pos].reset()
                        del objects_dict[i][index_pos]
                        scoreboard.score_update(objects_dict[i][-1])
                        count += 1
                        ball.bounce()
        except UnboundLocalError:
            pass
        except KeyError:
            pass
    if count == 4:
        count += 1
        speed *= 0.8
    elif count == 13:
        count += 1
        speed *= 0.8
    if ball.ycor() < -280:
        count = 0
        speed = 0.05
        checker_blue = 0
        checker_orange = 0
        ball.reset_position()
    elif ball.ycor() > 280:
        paddle.shapesize(stretch_len=2.5)
        ball.bounce()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    if ball.ycor() < -220 and ball.distance(paddle) < 50:
        ball.bounce()

    for i in range(8):
        try:
            if len(objects_dict[i]) == 1:
                del objects_dict[i]
        except KeyError:
            pass
    if objects_dict == {}:
        game_is_on = False

screen.exitonclick()
