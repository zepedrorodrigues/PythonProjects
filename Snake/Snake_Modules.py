import turtle
from turtle import Turtle
import time
import random
import os

class Snake():
    def __init__(self):
        self.group = []
        self.starting_positions = [(0,0),(-20,0),(-40,0)]
        self.create_snake()
        self.head = self.group[0]
            
    def create_snake(self):
        for position in self.starting_positions:
            self.add_block(position) 
    
    def add_block(self,position):
        new_block = Turtle('square')
        new_block.width(4); new_block.color('white')
        new_block.penup()
        new_block.goto(position)
        new_block.setheading(0)
        self.group.append(new_block)

    def extend(self):
        self.add_block(self.group[-1].pos())
    
    def move(self):
        for x in range(-1,-len(self.group),-1):
            self.group[x].goto(self.group[x-1].pos())
        self.head.forward(20)
        time.sleep(0.1)
    
    def reset(self):
        for g in self.group:
            g.goto(500,500)
        self.group.clear()
        self.create_snake()
        self.head = self.group[0]
    
    def turn_up(self):
        if self.head.heading()==270:
            return
        else:
            self.head.setheading(90)

    def turn_right(self):
        if self.head.heading()==180:
            return
        else:
            self.head.setheading(0)

    def turn_left(self):
        if self.head.heading()==0:
            return
        else:
            self.head.setheading(180)

    def turn_down(self):
        if self.head.heading()==90:
            return
        else:
            self.head.setheading(270)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.width(4);self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.penup()
        self.speed('fastest')
        
    def move(self):
        self.goto(random.choice(range(-280,280)),random.choice(range(-280,280)))

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0; self.penup(); self.goto(0,250); self.color('white'); self.hideturtle()
        with open(r'C:\Users\jpnms\Documents\GitHub\Python_Projects\Python Project Files\Snake_Highscore.txt','r') as file:
            a = file.read(); self.highscore=int(a)
        self.update_scoreboard()
         
    def collision_food(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open(r"C:\Users\jpnms\Documents\GitHub\Python_Projects\Python Project Files\Snake_Highscore.txt",'r') as file:
                a = file.read(); self.highscore = int(a)
        self.write(f'Score: {self.score} Highscore: {self.highscore}',align='center',font=('Arial',15,'normal'))

    def reset(self):
        if self.highscore<self.score:
            with open(r"C:\Users\jpnms\Documents\GitHub\Python_Projects\Python Project Files\Snake_Highscore.txt",'w') as file:
                  file.write(f'{self.score}')
        self.clear()
        self.score = 0
        self.update_scoreboard()