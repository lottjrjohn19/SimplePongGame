import turtle

wnd = turtle.Screen()
wnd.title("Pong Game")
wnd.bgcolor("green")
wnd.setup(width=800, height=600)
wnd.tracer(0)

# Score
score_a = 0
score_b = 0

# Player A
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.color("black")
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.penup()
player_a.goto(-350, 0)

# Player B
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.color("black")
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.penup()
player_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.shapesize()
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2


# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:  Player B: ", align="center",
          font=("Arial", 24, "bold"))

# Game Functions


def player_a_up():
    y = player_a.ycor()
    y += 20
    player_a.sety(y)


def player_a_down():
    y = player_a.ycor()
    y -= 20
    player_a.sety(y)


def player_b_up():
    y = player_b.ycor()
    y += 20
    player_b.sety(y)


def player_b_down():
    y = player_b.ycor()
    y -= 20
    player_b.sety(y)

# Keyboard binding


wnd.listen()
wnd.onkeypress(player_a_up, "w")
wnd.onkeypress(player_a_down, "s")

wnd.onkeypress(player_b_up, "Up")
wnd.onkeypress(player_b_down, "Down")

while True:
    wnd.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                  font=("Arial", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                  font=("Arial", 24, "bold"))

    # Collisions

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_b.ycor() + 40 and ball.ycor() > player_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() > -340 and ball.xcor() < -350) and (ball.ycor() < player_a.ycor() + 40 and ball.ycor() > player_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
