from turtle import Turtle,Screen
Screen_Object=Screen()
class Paddle(Turtle):
    def __init__(self,Position):
        super().__init__()
        self.Position=Position
        self.create_peddle()
    def create_peddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(self.Position)
    def Up(self):
        if  self.ycor()<=280:
            new_y=self.ycor()+40
            self.goto(self.xcor(),new_y)
        Screen_Object.update()
    def Down(self):
        if  self.ycor()>=-280:
            new_y=self.ycor()-40
            self.goto(self.xcor(),new_y)
        Screen_Object.update()
    def Paddle_robbot(self, Ball_Object):
        if abs(self.ycor() - Ball_Object.ycor()) > 10:  # Add buffer to prevent jitter
            if self.ycor() > Ball_Object.ycor():
                new_y = self.ycor() - 10  # Move in smaller steps
                self.goto(self.xcor(), new_y)
            elif self.ycor() < Ball_Object.ycor():
                new_y = self.ycor() + 10
                self.goto(self.xcor(), new_y)

        