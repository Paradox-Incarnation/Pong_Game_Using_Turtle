from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pensize(10)
        self.l_score=0
        self.r_score=0
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-80,260)
        self.write(self.l_score,align="center",font=("Courier",54,"normal"))
        self.goto(80,260)
        self.write(self.r_score,align="center",font=("Courier",54,"normal"))
    def l_score_update(self):
        self.l_score+=1
        self.update_score()
    def r_score_update(self):
        self.r_score+=1
        self.update_score()


