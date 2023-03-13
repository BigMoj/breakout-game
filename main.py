import random
import turtle
import time

# Set up the screen
win = turtle.Screen()
win.title("Breakout")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

text = turtle.Turtle()
text.penup()
text.hideturtle()
text.color("black")
text.goto(0, 0)

# Create the bricks
colors = ["red", "skyblue", "purple", "yellow", "orange", "green"]
bricks = []
for i in range(-200, 240, 80):
    for j in range(25, 250, 30):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(random.choice(colors))
        brick.shapesize(stretch_wid=1, stretch_len=4)
        brick.penup()
        brick.goto(i, j)
        bricks.append(brick)


# Move the paddle
def move_left():
    x = paddle.xcor()
    if x > -250:
        x -= 20
    paddle.setx(x)


def move_right():
    x = paddle.xcor()
    if x < 250:
        x += 20
    paddle.setx(x)


# Keyboard bindings
win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")

# Main game loop
life = 3
game_is_on = True
while game_is_on:
    win.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for border collision
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -285:
        ball.goto(0, 0)
        ball.dy *= -1

    # Check for paddle collision
    if ball.ycor() < -240 and ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50:
        ball.dy *= -1

    # Check for brick collision
    for brick in bricks:
        if ball.distance(brick) < 30:
            brick.goto(1000, 1000)
            bricks.remove(brick)
            ball.dy *= -1

    # Check for game over
    if len(bricks) == 0:
        win.clear()
        text.write("You win!", align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        win.bye()
        game_is_on = False

    if ball.ycor() < -280:
        ball.goto(0, 0)
        ball.dy *= -1
        life -= 1
        if life == 0:
            win.clear()
            text.write("Game over!", align="center", font=("Courier", 24, "normal"))
            time.sleep(3)
            win.bye()
            game_is_on = False

# Exit the game
turtle.done()
