import csv
import random

# Load player data
with open('players.csv', mode='r') as file:
    csvFile = csv.DictReader(file)
    all_cards = list(csvFile)

# Explicit mapping for shorthand keys
mapping_dict = {
    'O': 'Overall(O)',
    'P': 'Pace(P)',
    'S': 'Shooting(S)',
    'A': 'Passing(A)',     
    'R': 'Dribbling(R)', 
    'D': 'Defense(D)'
}

# Training mode
def Training():
    display_best_card()

def display_best_card():
    print('Best cards for each attribute are:\n')
    for key in mapping_dict.values():
        best_card = max(all_cards, key=lambda x: float(x[key]))
        print(key, ': ', best_card[key], ' (', best_card['Name'], ')')
    input('Press Enter to continue')

# Display card neatly
def display_card(card):
    max_chars = max(len(keys) for keys in card)
    for keys in card:
        print(keys, (max_chars - len(keys)) * ' ', ': ', card[keys])

# Determine winner
def determine_winner(m1, m2, order=1):
    dct = {'player': m1, 'computer': m2}
    v = list(dct.values())
    k = list(dct.keys())
    if m1 == m2:
        return 'draw'
    else:
        if order == 1:
            return k[v.index(max(v))]
        else:
            return k[v.index(min(v))]

# Rank system
def category_rank(test_card, category):
    global rank
    metric = [float(card[mapping_dict[category]]) for card in all_cards]
    metric_sorted = sorted(metric, reverse=True)
    rank = metric_sorted.index(float(test_card[mapping_dict[category]])) + 1
    return rank

# Shuffle and distribute cards
random.shuffle(all_cards)
comput_cards = all_cards[0::2]
player_cards = all_cards[1::2]
table_cards = []
game_over = False
chance = 'player'

print("Welcome to the Top Trumps Game, Football theme")
print('Make your choices wisely and try to win all the cards')
print('Click Enter to begin')
input()

# Training mode option
training = input('Do you want to have a training mode? (y/n): ')
if training.lower() == 'y':
    Training()

# Main game loop
while not game_over:
    print('Player cards:', len(player_cards), 
          'Computer cards:', len(comput_cards), 
          'Table cards:', len(table_cards))
    
    player = player_cards.pop(0)
    comput = comput_cards.pop(0)
    table_cards.extend([player, comput])

    print(f"\nIt is now {chance}'s turn\n")
    print('Your (Player) card is:')
    display_card(player)
    print()

    if chance == 'player':
        chosen_key = input('Choose a category (O, P, S, A, R, D): ').upper()
        if chosen_key not in mapping_dict:
            print('Invalid choice, computer will choose for you')
            chosen_key = random.choice(list(mapping_dict.keys()))
        chance = 'computer'
    else:
        chosen_key = random.choice(list(mapping_dict.keys()))
        print(f'Computer chose {chosen_key}')
        chance = 'player'

    key_requested = mapping_dict[chosen_key]
    value_player = player[key_requested]
    value_comput = comput[key_requested]

    print('Key of interest is', key_requested)

    winner = determine_winner(float(value_player), float(value_comput))

    player_rank = category_rank(player, chosen_key)
    computer_rank = category_rank(comput, chosen_key)

    print(f'Player {key_requested} is {value_player} (rank = {player_rank})')
    print(f'Computer {key_requested} is {value_comput} (rank = {computer_rank})\n')
    print('Winner is ...', winner)
    input()

    if winner == 'player':
        player_cards.extend(table_cards)
        table_cards.clear()
    elif winner == 'computer':
        comput_cards.extend(table_cards)
        table_cards.clear()

    if len(player_cards) == 0:
        print('Computer Won')
        game_over = True
    elif len(comput_cards) == 0:
        print('Player Won')
        game_over = True 