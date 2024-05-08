from turtle import Turtle
import random

class Ball:
    def __init__(self,sc_width,sc_lenght):
        self.ball = 0
        self.x = 0
        self.y = 0
        self.sc_width = sc_width
        self.sc_lenght = sc_lenght
        
    def crt_ball(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("blue")
        self.ball.turtlesize(0.75,0.75)
        self.ball.speed("slowest")
        self.ball.penup()
        
    def ball_mvmt(self,x_cor):
        self.ball.speed("slowest")
        self.ball.goto(x = x_cor,y = random.randint(-self.sc_lenght/2, self.sc_lenght/2))
            
        
        
        
