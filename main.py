from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
#Setting up Objects
Screen_Object=Screen()
Turtle_Object=Turtle()
Ball_Object=Ball()
#Screen Settings
Screen_Object.title("Paradox's Pong Game")
Screen_Object.bgcolor("black")
Screen_Object.setup(1.0,1.0)
Screen_Object.tracer(0) # Turning off the animations
# Making The Boundary
Turtle_Object.goto(0,540)
Turtle_Object.color("white")
Turtle_Object.right(90)
Turtle_Object.hideturtle()
def rectangle(width):
    Turtle_Object.fillcolor("white")
    Turtle_Object.begin_fill()
    for _ in range(2):
        Turtle_Object.right(90)
        Turtle_Object.fd(5)
        Turtle_Object.right(90)
        Turtle_Object.fd(width)
    Turtle_Object.end_fill()

while (Turtle_Object.ycor()>=-540):
    Turtle_Object.pendown()
    rectangle(15)
    Turtle_Object.penup()
    Turtle_Object.fd(30)
Screen_Object.update()

#Making Paddles
Paddle2=Paddle((-600,0))
Paddle1=Paddle((600,0))

#Setting up controls
Paradox =set()
def Paddle1up():
     Paradox.add("up")
def Paddle1down():
     Paradox.add("down")
def Paddle2up():
     Paradox.add("w")
def Paddle2down():
     Paradox.add("s")
def Paddle1up_discard():
     Paradox.discard("up")
def Paddle1down_discard():
     Paradox.discard("down")
def Paddle2up_discard():
     Paradox.discard("w")
def Paddle2down_discard():
     Paradox.discard("s")
def listener():
     if "up" in Paradox:
            Paddle1.Up()
     if "down" in Paradox:
            Paddle1.Down()
     if "w" in Paradox:
            Paddle2.Up()
     if "s" in Paradox:
            Paddle2.Down()
     Screen_Object.ontimer(listener,50)
NOP=Screen_Object.textinput("Alert","Do you want to play Single Player[S] or Multiplayer[M]")

Screen_Object.listen()
Screen_Object.onkeypress(Paddle1up,"Up")
Screen_Object.onkeypress(Paddle1down,"Down")
Screen_Object.onkeyrelease(Paddle1up_discard,"Up")
Screen_Object.onkeyrelease(Paddle1down_discard,"Down")
if NOP.lower()=="m":
    Screen_Object.onkeypress(Paddle2up,"w")
    Screen_Object.onkeypress(Paddle2down,"s")
    Screen_Object.onkeyrelease(Paddle2up_discard,"w")
    Screen_Object.onkeyrelease(Paddle2down_discard,"s")
Score_Object=Scoreboard()
listener()

game_is_on=True
while game_is_on:
    Ball_Object.moving()
    if NOP.lower()!="m":
         Paddle2.Paddle_robbot(Ball_Object=Ball_Object)
    time.sleep(Ball_Object.move_speed)
    if Ball_Object.ycor()>=340 or Ball_Object.ycor()<=-340:
         Ball_Object.Bounce_Vertical()
    if Ball_Object.xcor()>=570 and Ball_Object.distance(Paddle1)<=55:
         Ball_Object.Bounce_Horizonatal()
    if Ball_Object.xcor()<=-570 and Ball_Object.distance(Paddle2)<=55:
         Ball_Object.Bounce_Horizonatal()
    if Ball_Object.xcor()<=-640:
         Score_Object.r_score_update()
         Ball_Object.reset_ball()
    if Ball_Object.xcor()>=640:
         Score_Object.l_score_update()
         Ball_Object.reset_ball()
    Screen_Object.update()
Screen_Object.update()


#Screen end
Screen_Object.mainloop()