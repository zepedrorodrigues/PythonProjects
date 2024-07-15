import csv
import pandas
import turtle

turtle.bgpic(r"blank_states_img.gif")

screen = turtle.Screen()
screen.screensize(canvheight=900,canvwidth=900)

states = pandas.read_csv(r"50_states.csv")

state_list = [item for item in states['state']]

score_value = 0
game_on = True

def game_over():
    global game_on
    game_on = False
    for state in state_list:
        data = states[states['state']== state]; x = float(data['x']);y=float(data['y'])
        t1 = turtle.Turtle(); t1.hideturtle(); t1.color('red'); t1.penup(); t1.goto(x,y); 
        t1.write(f'{state}',move=False,align='center',font=('Arial',11,'bold'))    

while game_on == True:
    response = turtle.textinput(f'{score_value}/50 States Guessed','Write a name of a State or \'End\' to Give up').strip().title()
    if response in state_list:
        state_list.remove(response)
        score_value += 1
        data = states[states['state']==f'{response}']
        x = float(data['x']); y = float(data['y'])
        t = turtle.Turtle(); t.hideturtle(); t.color('black'),t.penup();t.goto(x,y);t.write(f'{response}',move=False,align='center',font=('Arial',10,'normal'))
        
    elif response == 'End':
        game_over()
    else:
        continue

turtle.mainloop()

