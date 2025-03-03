from turtle import Turtle,Screen
from random import randint
import time
Screen_Object=Screen()
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.setheading(20)
        self.moving_distance=20
        self.move_speed=0.1
    def moving(self):    
        self.fd(self.moving_distance)
    def Bounce_Vertical(self):
        self.seth(-self.heading())
    def Bounce_Horizonatal(self):
        self.move_speed*=0.95
        self.seth(180-self.heading())
    def reset_ball(self):
        self.goto(0,0)
        self.Bounce_Horizonatal()