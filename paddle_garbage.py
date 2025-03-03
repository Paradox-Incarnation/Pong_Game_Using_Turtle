from turtle import Turtle,Screen
Screen_Object=Screen()
class Paddle:
    def __init__(self,L):
        self.postions=L
        self.Squares=[]
        self.create_paddle()
    def create_paddle(self):
        for i in range(5):
            Squares=Turtle("square")
            Squares.resizemode("user")
            Squares.shapesize(1)
            Squares.color("white")
            Squares.penup()
            Squares.speed(0)
            Squares.goto(self.postions[i])
            self.Squares.append(Squares)
    def Up(self):
        for i in  range(len(self.Squares)-1,0,-1):
            self.Squares[i].goto(self.Squares[i-1].pos())
        self.Squares[0].seth(90)
        self.Squares[0].fd(20)  
        Screen_Object.update()
    def Down(self):
        for i in  range(0,len(self.Squares)-1):
            self.Squares[i].goto(self.Squares[i+1].pos())
        self.Squares[len(self.Squares)-1].seth(270)   
        self.Squares[len(self.Squares)-1].fd(20)
        Screen_Object.update()
        


        