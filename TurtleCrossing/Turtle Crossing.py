import random
import turtle
import time

class player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.initial_game()
    def initial_game(self):
        self.shape('turtle');self.penup(); self.goto(0,-280)
        self.setheading(90)
    def move_up(self):
        self.setheading(90); self.forward(10)
    def move_down(self):
        self.setheading(270);self.forward(10)
    def move_left(self):
        self.setheading(180);self.forward(10)
    def move_right(self):
        self.setheading(0);self.forward(10)
    def level_up(self):
        self.clear()
        self.initial_game()


class car():
    def __init__(self):
        super().__init__
        self.colors = ['blue','yellow','purple','red','green','white','orange']
        self.cars = []
        self.level = 1
        self.initiate_game()

    def create_car(self,number):
        for _ in range(number):
            new_car = turtle.Turtle(); new_car.shape('square'); new_car.shapesize(1,2,1)
            new_car.color(random.choice(self.colors))
            new_car.penup(); new_car.goto(random.choice(range(-270,270)),random.choice(range(-270,270)))
            new_car.setheading(180); self.cars.append(new_car)
    
    def initiate_game(self):
        self.create_car(10)
    
    def move(self):
        for car in self.cars:
            car.forward(8+(self.level*2))

    def level_up(self):
        self.level +=1
        self.create_car(2)
    
    def detect_wall(self):
        for car in self.cars:
            if car.xcor()<-270:
                car.goto(270,random.choice(range(-270,270)))
    
    def detect_collision(self,who):
        for car in self.cars:
            if car.distance(who)<20:
                return True

class Level(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.color('white'); self.penup(); self.goto(-30,280)
        self.write(f'Level: {self.level}',move=False,align='center',font=('Arial',20,'normal')); self.hideturtle()
    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}',move=False,align='center',font=('Arial',20,'normal'))

screen=turtle.Screen(); screen.screensize(canvwidth=600,canvheight=600)
screen.bgcolor('black'); screen.tracer(0)

p1 = player()
c = car()
L = Level()

screen.listen(); screen.onkey(p1.move_down,'Down');screen.onkey(p1.move_left,'Left')
screen.onkey(p1.move_right,'Right');screen.onkey(p1.move_up,'Up')

game_on = True

while game_on == True:
    c.move()
    c.detect_wall()
    if c.detect_collision(p1) == True:
        game_on = False
        game_over = Level();game_over.goto(0,0);game_over.write('Game Over.',move=False,align='center',font=('Arial',20,'normal'))
    if p1.ycor()>280:
        p1.level_up()
        c.level_up()
        L.level_up()   
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
