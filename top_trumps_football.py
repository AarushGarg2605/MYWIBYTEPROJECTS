import csv
import random

with open('players.csv', mode ='r') as file:
  csvFile = csv.DictReader(file)
  all_cards = list(csvFile)


def Training():
  display_best__card()

def display_best__card():
  # Display the best card for each attribute
  # The best card is the one with the highest value for that attribute

  print('Best cards for each attribute are:')
  print()

  for key in relevant_keys:
    best_card = max(all_cards, key=lambda x: float(x[key]))
    print(key, ': ', best_card[key], ' (', best_card['Name'], ')') 
  input('Press Enter to continue')
    


print("Welcome to the Top Trumps Game, Football theme")
print('Make your choices wisely and try to win all the cards')
print('Click Enter to begin')

input()




def display_card(card):
  

  max_chars = 0
  
  for keys in card:
    if len(keys) > max_chars:
      max_chars = len(keys)
  
  for keys in card:
    print(keys, (max_chars-len(keys))*' ', ': ', card[keys])
  
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


def category_rank(test_card, category):
  global rank
  metric = [float(card[mapping_dict[category]])for card in all_cards]      
  if category in ['O','S', 'P','A','R','D']:
    metric_sorted =  sorted(metric, reverse=True)
  rank = metric_sorted.index(float(test_card[mapping_dict[category]])) + 1
  return rank
  

random.shuffle(all_cards)

comput_cards = all_cards[0::2]
player_cards = all_cards[1::2]
table_cards = []
game_over = False
chance = 'player'


relevant_keys = list(all_cards[0].keys())
relevant_keys = relevant_keys[2::]

mapping_dict = {}

for key in relevant_keys:
  mapping_dict[key[0]] = key

input()

training = input('Do you want to have a  training mode? (y/n)')

if training == 'Y'or training == 'y':
 Training()


while not game_over:

  print('player cards: ', len(player_cards), 'computer cards: ', len(comput_cards), 'table_cards: ', len(table_cards))
  
  player = player_cards.pop(0)
  comput = comput_cards.pop(0)

  table_cards.append(player)
  table_cards.append(comput)

  print()
  print(f'It is now {chance}\'s chance')
  print()

  print('Your (Player) card is ')
  display_card(player)
  print()

  if chance == 'player':
    
    chosen_key = input('What is your choice?')
    if chosen_key not in list(mapping_dict.keys()):
      print('Invalid choice, computer will choose for you')
      chosen_key = random.choice(list(mapping_dict.keys()))
    chance = 'computer'    

  else:
    
    chosen_key = random.choice(list(mapping_dict.keys()))
    chance = 'player'
  key_requested = mapping_dict[chosen_key]
  value_player = player[key_requested]
  value_comput = comput[key_requested]
  
  print('Key of interest is ', key_requested)

  if chosen_key in ['O','S', 'P','A','R','D']:
    winner = determine_winner(float(value_player), float(value_comput)); 

    
  
    
  
  player_rank = category_rank(player, chosen_key)
  computer_rank = category_rank(comput, chosen_key)
  print('Player ', key_requested, 'is', value_player,'(rank = ', player_rank, ')')
  print('Computer ', key_requested, 'is', value_comput,'(rank = ', computer_rank, ')')
  print()
  print('Winner is ... ', winner)
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
#bonus ideas added -
# 1- Add a training mode that displays the best card for each attribute
# 2- Add a ranking system that shows the rank of the player's and computer's card for the chosen attribute
# 3- Added a failsafe for invalid input from the player when choosing an attribute, and the computer will choose a random attribute instead
#  