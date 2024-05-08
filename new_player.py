from turtle import Turtle

class NewPlayer:
    def __init__(self,sc_width,player_no):
        self.sc_width = sc_width
        self.paddle = 0
        self.player_no = player_no
        
    def crt_paddle(self):
        self.paddle = Turtle()
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.penup()
        self.paddle.seth(90)
        self.paddle.turtlesize(stretch_wid = 0.5,stretch_len = 3)
        
        if self.player_no == 1:
            p_x,p_y = -self.sc_width/2,0
        elif self.player_no == 2:
            p_x,p_y = self.sc_width/2,0 
            
        self.paddle.goto(x = p_x,y = p_y)
        
        
    def paddle_fd(self):
        self.paddle.fd(30)
        
    def paddle_bd(self):
        self.paddle.bk(30)

