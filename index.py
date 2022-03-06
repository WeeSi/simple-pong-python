import turtle

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.cv._rootwindow.resizable(False, False)
wn.score_a = 0
wn.score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color('white')
ball.penup()
ball.goto(0,0)

# Move by 0.5 pixels
ball.dx = 0.5
ball.dy = 0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if(y<240):
        paddle_a.sety(y)
        
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if(y>-240):
        paddle_a.sety(y)
        
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if(y<240):
        paddle_b.sety(y)
        
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if(y>-240):
        paddle_b.sety(y)

def MoveTheBall():
     # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if(ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -1
    
    if(ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1    
    
    if(ball.xcor() > 390):
        ball.goto(0, 0)
        ball.dx *= -1
        wn.score_a += 1
    
    if(ball.xcor() < -390):
        ball.goto(0, 0)
        ball.dx *= -1
        wn.score_b += 1
    
    pen.clear()    
    pen.write("Player A: {}   Player B: {}".format(wn.score_a,wn.score_b), align="center", font=("Courier", 15, "bold"))
        
    
    # Paddle and ball collisions       
    if(ball.xcor() > 340 and (ball.ycor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40)):
        ball.setx(340)
        ball.dx *= -1
        
    if(ball.xcor() < -340 and (ball.ycor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40)):
        ball.setx(-340)
        ball.dx *= -1

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,'Up')
wn.onkeypress(paddle_a_down,'Down')

wn.onkeypress(paddle_b_up,'w')
wn.onkeypress(paddle_b_down,'s')



#main game loop
while True:
    wn.update()
    MoveTheBall()
    
   