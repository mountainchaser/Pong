

import turtle
#import winsound

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)

left_score = 0
right_score = 0

#Left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.color("white")
left_paddle.penup()
left_paddle.goto(-350, 0)

#Right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.color("white")
right_paddle.penup()
right_paddle.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = 5


def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Left Player: {}   Right Player: {}".format(left_score, right_score), align="center", font=("Courier", 23, "normal"))

win.listen()
win.onkeypress(left_paddle_up, "w")
win.onkeypress(left_paddle_down, "s")
win.onkeypress(right_paddle_up, "Up")
win.onkeypress(right_paddle_down, "Down")


while True:
    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #top bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #winsound.PlaySound("bounce.wav", winsound.SND_async)
    
    #bottom bounce
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        #winsound.PlaySound("bounce.wav", winsound.SND_async)
    
    if ball.xcor() > 390:
        ball.goto(0, 0 )
        ball.dx *= -1
        left_score += 1
        pen.clear()
        pen.write("Left Player: {}   Right Player: {}".format(left_score, right_score), align="center", font=("Courier", 23, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0 )
        ball.dx *= -1
        right_score += 1
        pen.clear()
        pen.write("Left Player: {}   Right Player: {}".format(left_score, right_score), align="center", font=("Courier", 23, "normal"))

    #paddle bounce
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor()> right_paddle.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        #winsound.PlaySound("bounce.wav", winsound.SND_async)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor()> left_paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        #winsound.PlaySound("bounce.wav", winsound.SND_async)
    

