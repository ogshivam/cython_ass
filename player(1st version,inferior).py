from turtle import Turtle


class Player:
    def __init__(self,sc_width,player_no):
        self.player_no = player_no
        self.len_of_paddle = 5
        self.sc_width = sc_width
        self.paddle = []
        

    def crt_paddle(self):
        if self.player_no == 1:
            p_x,p_y = -self.sc_width/2,-20
        elif self.player_no == 2:
            p_x,p_y = self.sc_width/2,-20
        for i in range(self.len_of_paddle):
            p = Turtle()
            p.color("white")
            p.shape("square")
            p.turtlesize(stretch_wid = 0.5,stretch_len = 0.5)
            p.penup()
            p.goto(x = p_x,y = p_y)
            p_y += 10
            self.paddle.append(p)
            
            
    def paddle_bd(self):
       for i in range(len(self.paddle)):
           a = self.paddle[i]
           a.speed("fastest")
           a.seth(270)
           a.fd(50)
           
    def paddle_fd(self):
        l = len(self.paddle)
        for i in range(l):
            a = self.paddle[l-1-i]
            a.speed("fastest")
            a.seth(90)
            a.fd(50)
        
            


