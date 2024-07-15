import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock,paper,scissors]

def greeting():
    print('Hello, wanna play Rock Paper Scissors?')
    inp =input('')
    options_()

def options_():
    option_player =input('Great, let\'s start!\nPick\n1.Rock\n2.Paper\n3.Scissors?\n')
    if option_player in "123":
        if option_player == '1':
            option_player = rock
        elif option_player == '2':
            option_player = paper
        elif option_player == '3':
            option_player = scissors
    else:
        print('invalid option, pick again')
        options_()

    option_computer = random.choice(options)
    if option_computer == options_.option_player:
        result = 'It\'s a draw!'
    elif options.option_computer == rock and option_player==paper or option_computer ==paper and option_player==scissors:
        result = 'Player wins!'
    else:
        result = 'Computer wins!'

    print(f'Player:\n{option_player}\nComputer:\n{option_computer}\n\n{result}\n')

greeting()