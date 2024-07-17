import os
import turtle
import pandas

# Set up the screen and background image
screen = turtle.Screen()
screen.title("U.S. States Game")

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "blank_states_img.gif")

# Check if the image file exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Background image file not found: {image_path}")

screen.bgpic(image_path)
screen.setup(width=725, height=491)  # Adjust dimensions based on the actual image size

# Read the states data
csv_path = os.path.join(current_dir, "50_states.csv")
states = pandas.read_csv(csv_path)
state_list = states['state'].tolist()

score_value = 0
game_on = True

# Function to handle game over
def game_over():
    global game_on
    game_on = False
    for state in state_list:
        data = states[states['state'] == state]
        x = int(data['x'].iloc[0])
        y = int(data['y'].iloc[0])
        t1 = turtle.Turtle()
        t1.hideturtle()
        t1.color('red')
        t1.penup()
        t1.goto(x, y)
        t1.write(state, align='center', font=('Arial', 11, 'bold'))

# Main game loop
while game_on:
    response = turtle.textinput(f'{score_value}/50 States Guessed', 'Write the name of a State or \'End\' to Give up')
    if response is None:
        continue
    response = response.strip().title()
    if response in state_list:
        state_list.remove(response)
        score_value += 1
        data = states[states['state'] == response]
        x = int(data['x'].iloc[0])
        y = int(data['y'].iloc[0])
        t = turtle.Turtle()
        t.hideturtle()
        t.color('black')
        t.penup()
        t.goto(x, y)
        t.write(response, align='center', font=('Arial', 10, 'normal'))
    elif response == 'End':
        game_over()
    else:
        continue

turtle.mainloop()
