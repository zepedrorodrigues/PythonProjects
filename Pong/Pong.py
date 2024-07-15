import turtle
from turtle import Turtle
from turtle import Screen
import random
import time

class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white') 
        self.shape('circle')
        self.shapesize(0.8,0.8,1)
        self.speed('fastest')
        self.initiate_movement()
    def initiate_movement(self):
        self.home()
        self.setheading(random.choice(range(360)))
    def move(self):
        self.penup()
        self.forward(10)
        time.sleep(0.02)
    def reset(self):
        self.home()
        self.initiate_movement()
    def collision_wall(self):
        self.setheading(-self.heading())
    def collision_pad(self):
        self.setheading(180-self.heading())

class court():
    def __init__(self):
        self.create_court()
    def create_court(self):
        court = Turtle(); court.color('white'); court.penup(); court.goto(0,290);court.setheading(270)
        for x in range(30):
            court.pendown();court.forward(10); court.penup();court.forward(10)
        court.penup(); court.goto(400,300);court.setheading(180) ; court.pendown()
        for x in range(4):
            if x%2==0:
                court.forward(800)
            else:
                court.forward(600)
            court.left(90)
        court.hideturtle()

class padle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=4,stretch_len=0.5)
        self.penup()

    def go_up(self):
        self.goto(self.xcor(),self.ycor()+30)

    def go_down(self):
        self.goto(self.xcor(),self.ycor()-30)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.individual_self = [0,0]
        self.set_score()
    def set_score(self):
        self.clear()
        self.hideturtle(); self.color('white');self.penup();self.goto(-30,280)
        self.write(f'{self.individual_self[0]}',align='center',font=('Arial',30,'normal'))
        self.goto(30,280); self.write(f'{self.individual_self[1]}',align='center',font=('Arial',30,'normal'))

game_on = True

def game_onoff():
    if game_on==True:
        game_on = False
    elif game_on == False:
        game_on = True

screen = Screen(); screen.bgcolor('black'); screen.screensize(canvwidth=800,canvheight=600,);screen.title('Pong ou lá o crl, farto disto')
screen.tracer(0)

bal = ball(); coutr = court(); pad = padle(); pad.goto(380,0); pad_pc = padle(); pad_pc.goto(-380,0)
score = Scoreboard()
screen.listen(); screen.onkey(pad.go_down,'Down');screen.onkey(pad.go_up,'Up')
screen.onkey(pad_pc.go_down,'s');screen.onkey(pad_pc.go_up,'w');screen.onkey(game_onoff,'p')


while game_on == True:
    screen.update()
    bal.move()
    screen.tracer(0)
    if pad.distance(bal)<15 or pad_pc.distance(bal)<15 or pad_pc.distance(bal)<50 and bal.xcor()<-389 or pad.distance(bal)<50 and bal.xcor()>389:
        bal.collision_pad()
        bal.move()
    elif bal.ycor()>290 or bal.ycor()<(-290):
        bal.collision_wall()
        bal.move()    
    elif bal.xcor()>395 or bal.xcor()<-395:
        if bal.xcor()>395:
            score.individual_self[0] +=1
        if bal.xcor()<-395:
            score.individual_self[1] +=1
        score.set_score()
        bal.reset()
    
    
        

screen.exitonclick()




