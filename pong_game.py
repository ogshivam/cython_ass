from turtle import Screen,Turtle,title 
from ball import Ball 
from new_player import NewPlayer

screen = Screen()
screen.screensize(canvwidth=1000,canvheight=500,bg = "black")

title("Pong Game")

# score turtle
score_tur = Turtle()
score_tur.pencolor("white")
score_tur.penup()
score_tur.goto(x = -100,y = screen.canvheight/2 + 20)
score_tur.write("Pong Game",font = ("Arial",30,"normal"))
score_tur.hideturtle()

#dividing the screen

X,Y = 0,-screen.canvheight/2

while Y <= screen.canvheight/2:
    s = Turtle()
    s.color("white")
    s.shape("square")
    s.turtlesize(stretch_wid =1,stretch_len = 0.25)
    s.penup()
    s.goto(x = X,y = Y)
    Y += 50
    
    
p1 = NewPlayer(screen.canvwidth,1)
p1.crt_paddle()   
 
p2 = NewPlayer(screen.canvwidth,2)
p2.crt_paddle()  


#p1.paddle_bd() 
#p2.paddle_fd() 

screen.listen()
screen.onkey(p2.paddle_fd, "Up")
screen.onkey(p2.paddle_bd, "Down")
screen.onkey(p1.paddle_fd, "w")
screen.onkey(p1.paddle_bd, "s")

ball = Ball(screen.canvwidth,screen.canvheight)
ball.crt_ball()

accuracy_mt = 25

# ball movement and entire game function
i = 1
while True:
    if i%2 != 0:
        ball.ball_mvmt(-screen.canvwidth/2)
        if p1.paddle.xcor()-ball.ball.xcor()==0 and abs(p1.paddle.ycor()-ball.ball.ycor())<accuracy_mt:
            pass
        else:
            print("game over p1")
            score_tur.goto(x = -screen.canvwidth/2,y = screen.canvheight/2)
            score_tur.write("game over p1")
            break
    else:
        ball.ball_mvmt(screen.canvwidth/2) 
        if p2.paddle.xcor()-ball.ball.xcor()==0 and abs(p2.paddle.ycor()-ball.ball.ycor())<accuracy_mt:
            pass
        else:
            print("game over p2")
            score_tur.goto(x = screen.canvwidth/2,y = screen.canvheight/2)
            score_tur.write("game over p2")
            break
    i += 1    



screen.exitonclick()