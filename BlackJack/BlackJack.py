import random
import os
from os import system

def deck_make():
    """Make a deck as a dictionary with number, suit and value. Ace is worth either 1 or 11"""
    numbers = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits = ['clubs','hearts','spades','diamonds']
    deck =  []
    for suit in suits:
        for number in numbers:
            if number in ['2','3','4','5','6','7','8','9','10']:
                value = int(number)
            elif number in ['J','Q','K']:
                value = 10
            else:
                value = [1,11]
            card1 = {'card':number,'suit':suit,'value':value}
            deck.append(card1)
    random.shuffle(deck)
    return deck

def beginning():
    print('Helllo! Welcome to Blackjack!\nThese are your cards:\n')
    deck = deck_make()
    player_hand = []; computer_hand = [] ; player = []; computer = [] 
    draw(2,player_hand,player,deck);draw(1,computer_hand,computer,deck)
    prt_scr(player,score_check(player_hand),computer,score_check(computer_hand))
    if score_check(player_hand)==21:
        print('Blackjack! Let\'s see what the House gets!\n\n')
        computer_playing(computer_hand,computer,player_hand,player,deck)
    else:
        player_plays(player_hand,player,computer_hand,computer,deck)    
    
def draw(number_of_cards,hand,hand_display,deck):
    for x in range(0,number_of_cards):
        crd = deck.pop()
        hand.append(crd)
        name = f'{crd["card"]} of {crd["suit"]}'
        hand_display.append(name)
    return hand,hand_display,deck

def score_check(who):
    score = 0
    for x in who:
        if type(x["value"]) == int:
            score = score + x["value"]
        else:
            ace = x["value"]
            if score<11:
                score = score + 11
            else:
                score = score + 1
    return score

def prt_scr(player,player_score,computer,computer_score):
    print(f'Player:\n{player}\nScore:{player_score}\n\nComputer:\n{computer}\nScore:{computer_score}\n\n')

def computer_playing(computer_hand,computer,player_hand,player,deck):
    while score_check(computer_hand)<17:
            inp = input('')
            os.system('CLS')
            draw(1,computer_hand,computer,deck)
            prt_scr(player,score_check(player_hand),computer,score_check(computer_hand))
    else:
        os.system('CLS')
        prt_scr(player,score_check(player_hand),computer,score_check(computer_hand))
        if score_check(computer_hand)>21:
            print('House busted! Player wins!')
        else:
            print(check_winner(score_check(computer_hand),score_check(player_hand)))
            return

def player_plays(player_hand,player,computer_hand,computer,deck):
    while score_check(player_hand)<= 21:
            inp = input('Want another card? ').strip().lower()
            if inp == 'yes':
                os.system('CLS')
                draw(1,player_hand,player,deck)
                prt_scr(player,score_check(player_hand),computer,score_check(computer_hand))
            elif inp == 'no':
                print('Ok,let\'s see what the house gets!\n')
                computer_playing(computer_hand,computer,player_hand,player,deck)
                break
    else:
        print('Busted! You lose!')

def check_winner(score_computer,score_player):
    result = ''
    if score_computer == score_player:
        result = 'It\'s a draw!'
    elif score_computer > score_player:
        result = 'House wins!'
    else: 
        result = 'Player wins!'
    return result          
               
def __main__():
    beginning()
if __name__ == '__main__':
    __main__()






        


        
