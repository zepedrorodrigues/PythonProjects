from turtle import Turtle
from turtle import Screen
import random
from random import choice


timmy = Turtle();timmy.color('blue')
tommy = Turtle();tommy.color('red')
tammy = Turtle();tammy.color('yellow')
teddy = Turtle(); teddy.color('purple')

turtles = [timmy,tommy,tammy,teddy]

def start_race():
    timmy.penup()
    timmy.goto(-100,100)
    tommy.penup()
    tommy.goto(-100,50)
    tammy.penup()
    tammy.goto(-100,0)
    teddy.penup()
    teddy.goto(-100,-50)
    race_on = True
    race(race_on)

def check_winner(winner):
    if user_bet == winner:
        print(f'Great bet! Your {winner} turtle won!')
    else:
        print(f'Wrong bet, the winner was the {winner} turtle!')

def race(race_on):
    while race_on == True:
        for turtle in turtles:
            if turtle.xcor()<240:
                turtle.forward(random.choice(range(0,11)))
            else:
                race_on = False
                winner = turtle.color()[0]
                check_winner(winner)

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title='Make your bet',prompt='Which will be the winner? Blue, Red, Yellow or Purple?').strip().lower()
start_race()
screen.exitonclick()    