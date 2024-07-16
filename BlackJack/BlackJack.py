import random

def deck_make():
    """Create a deck of cards as a list of dictionaries, each representing a card with its number, suit, and value."""
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['clubs', 'hearts', 'spades', 'diamonds']
    deck = []
    for suit in suits:
        for number in numbers:
            # Assign values to cards
            if number in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
                value = int(number)
            elif number in ['J', 'Q', 'K']:
                value = 10
            else:
                value = [1, 11]  # Ace can be 1 or 11
            card1 = {'card': number, 'suit': suit, 'value': value}
            deck.append(card1)
    random.shuffle(deck)  # Shuffle the deck
    return deck

def draw(number_of_cards, hand, hand_display, deck):
    """Draw a specified number of cards from the deck and add to the player's or computer's hand."""
    for _ in range(number_of_cards):
        crd = deck.pop()  # Draw card from the deck
        hand.append(crd)
        name = f'{crd["card"].lower()}_of_{crd["suit"].lower()}'
        hand_display.append(name)
    return hand, hand_display, deck

def score_check(hand):
    """Calculate and return the score of the given hand."""
    score = 0
    aces = 0
    for card in hand:
        if type(card["value"]) == int:
            score += card["value"]
        else:
            # Handle the ace value
            aces += 1
            score += 11
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

def check_winner(score_computer, score_player):
    """Determine and return the winner based on the final scores."""
    result = ''
    if score_computer == score_player:
        result = 'It\'s a draw!'
    elif score_computer > score_player:
        result = 'House wins!'
    else:
        result = 'Player wins!'
    return result

# Note: The functions `beginning`, `player_plays`, `computer_playing`, and `prt_scr`
# are not needed in the GUI version, as their functionality will be handled by the GUI.

if __name__ == '__main__':
    beginning()
