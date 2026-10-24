import turtle
import time
print("Welcome to the game! ")
print('This is a fusion of what all we have learnt so far in this course. ')
print('Reach the green square to play the laptop store game, reach the red square to play the fractals game, reach the yellow square to play the welcome message game and reach the purple square to play the top trumps game. ')
print('Open the turtle window and use the arrow keys to move the turtle. ')
input('Press Enter to start the game')
t = turtle.Turtle()
t.showturtle()
t.shape('square')
t.color('blue')
doorway = turtle.Turtle()
doorway.shape('square')
doorway.color('green')
doorway.penup()
doorway.goto(270, 270)
doorway.shapesize(5,5)
doorway.stamp()
doorway.color('red')
doorway.goto(-270,270)
doorway.stamp()
doorway.goto(-270,-270)
doorway.color('yellow')
doorway.stamp()
doorway.goto(270,-270)
doorway.color('purple')
doorway.stamp()



ts = turtle.Screen()
ts.bgcolor('black')

def down():
    if t.heading() != 90.0:    
        t.setheading(270.0)

def up():
    if t.heading() != 270.0:   
        t.setheading(90.0)

def left():
    if t.heading() != 0.0:     
        t.setheading(180.0)

def right():
    if t.heading() != 180.0:   
        t.setheading(0.0)

ts.onkey(down, 'Down')
ts.onkey(up, 'Up')
ts.onkey(left, 'Left')
ts.onkey(right, 'Right')
ts.listen()
t.speed(0)
doorway.hideturtle()

tgame = False
laptopstore = False
fractals = False
welcome_message = False
top_trumps = False
while not tgame:
    t.forward(1)
    time.sleep(0.001)
    if t.distance(270, 270) < 45:
        laptopstore = True
        tgame = True
    elif t.distance(-270, 270) < 45:
        fractals = True
        tgame = True
    elif t.distance(-270, -270) < 45:
        welcome_message = True
        tgame = True
    elif t.distance(270, -270) < 45:
        top_trumps = True
        tgame = True



doorway.clear()
t.clear() 
t.hideturtle()



import random 

try:
    
    from colorama import Fore
except ImportError:
      class _NoColour:
        def __getattr__(self, _name):
            return ''

      Fore = _NoColour()
print()
print()
print()
print()

if laptopstore == True:
        print("You have reached the phone store !")
       
        print('You have chosen Phones')
        print('Please select your specs')
        Phone_list      = []
       

        def append_s(name):
          return name + 's'
      
        # Define specs for phones
        specs_phones = ['Brand', 'Model', 'Storage', 'Colour', 'Price', 'OS']
      
        specs_new_phones = list(map(append_s, specs_phones))
        master_dict_phones = dict.fromkeys(specs_new_phones)
      
        master_dict_phones['Brands'] = ['Apple', 'Samsung', 'Google', 'OnePlus', 'Xiaomi']
      
        # Define a mapping of phone brands to their specific models
        brand_model_mapping_phones = {
            'Apple': ['iPhone 15 Pro Max', 'iPhone 15', 'iPhone SE','iPhone 17 Pro Max','iPhone16','','',''],
            'Samsung': ['Galaxy S24 Ultra', 'Galaxy Z Fold5', 'Galaxy A54','Galaxy S25','Galaxy S25 Pro'
      
      
      
      
            ],
            'Google': ['Pixel 8 Pro', 'Pixel 8', 'Pixel Fold'],
            'OnePlus': ['OnePlus 12', 'OnePlus Open', 'OnePlus Nord 3'],
            'Xiaomi': ['Xiaomi 14 Ultra', 'Redmi Note 13 Pro+', 'Poco F5']
        }
        master_dict_phones['Models'] = list(set(model for models in brand_model_mapping_phones.values() for model in models if model)) # Filter out empty strings
        master_dict_phones['Storages'] = ['64GB', '128GB', '256GB', '512GB', '1TB']
        master_dict_phones['Colours'] = ['Black', 'White', 'Blue', 'Green', 'Red', 'Gold']
        master_dict_phones['Prices'] = ['INR 50,000', 'INR 75,000', 'INR 1,00,000', 'INR 1,20,000', 'INR 1,50,000']
        master_dict_phones['OSs'] = ['iOS', 'Android']
      
      
      
        # Generate phone inventory
        for n_Phones  in range(100): # Generate 100 phones
          new_phone = dict.fromkeys(specs_phones)
      
          chosen_brand_phone = random.choice(master_dict_phones['Brands'])
          new_phone['Brand'] = chosen_brand_phone
      
          if chosen_brand_phone in brand_model_mapping_phones:
              new_phone['Model'] = random.choice([m for m in brand_model_mapping_phones[chosen_brand_phone] if m]) # Filter out empty strings
          else:
              new_phone['Model'] = random.choice([m for m in master_dict_phones['Models'] if m]) # Filter out empty strings
      
          for kk in new_phone:
            if kk not in ['Brand', 'Model']: # Skip Brand and Model as they are already set
                new_phone[kk] = random.choice(master_dict_phones[kk+'s'])
          Phone_list.append(new_phone)
      
        
        pref_phones = input('Please indicate the specifications which you have a preference for (comma seperated):')
        pref_list_phones = pref_phones.split(',')
        pref_list_phones = list(map(str.strip, pref_list_phones))
      
      
        user_choice_phones = dict.fromkeys(specs_phones)
        for kk in specs_phones:
          if kk in pref_list_phones:
            pref_str_phones = ''
            if kk == 'Brand':
                pref_str_phones = '/'.join(master_dict_phones['Brands'])
            elif kk == 'Model':
                if user_choice_phones['Brand'] and user_choice_phones['Brand'].lower() != 'none' and user_choice_phones['Brand'] in brand_model_mapping_phones:
                    pref_str_phones = '/'.join([m for m in brand_model_mapping_phones[user_choice_phones['Brand']] if m])
                else:
                    pref_str_phones = '/'.join([m for m in master_dict_phones['Models'] if m])
            else:
              pref_str_phones = '/'.join(master_dict_phones[kk+'s'])
      
            user_choice_phones[kk] = input('Any preference for ' + kk +':'+ pref_str_phones+ ' (Enter none for no preference)'+'\n')
          else:
            user_choice_phones[kk]= 'none'
        
      
      
        query_phones = ''
      
        for kk in user_choice_phones:
          # Treat empty input or 'none' as no preference
          if user_choice_phones[kk].lower() == 'none' or user_choice_phones[kk].strip() == '':
            pass
          else:
            query_phones = query_phones + "Phone['" + kk + "'] == '" + user_choice_phones[kk] + "' and "
      
        print(query_phones)
      
      
        query_phones = query_phones[0:-4] if query_phones else ''
      
      
      
        if query_phones != '':
          selected_phones = [Phone for Phone in Phone_list if eval(query_phones)]
        else:
          selected_phones = Phone_list
      
      
      
        print(len(selected_phones), 'These are the phones that met your preference .')
      
        Sorting_key_phones = input('Results to be sorted by(none for no sorting)')
        sorting_rev_phones = input('enter D for descending order')
      
        sorting_key_map_phones = {
            'brand': 'Brand', 'brands': 'Brand',
            'model': 'Model', 'models': 'Model',
            'storage': 'Storage', 'storages': 'Storage',
            'colour': 'Colour', 'colours': 'Colour',
            'price': 'Price', 'prices': 'Price',
            'os': 'OS', 'oss': 'OS'
        }
      
        sort_by_phones = sorting_key_map_phones.get(Sorting_key_phones.lower())
      
        if sort_by_phones:
            if sort_by_phones == 'Price':
                selected_phones = sorted(selected_phones, key=lambda x: float(x[sort_by_phones].replace('INR ', '').replace(',', '')), reverse=(sorting_rev_phones == 'D'))
            else:
                selected_phones = sorted(selected_phones, key=lambda x: x[sort_by_phones], reverse=(sorting_rev_phones == 'D'))
      
        characters = 0
        for kk in specs_phones:
          print(kk, end = '')
          characters = len(kk)
          print((15
      
                 - characters)*' ', end = '')
        print()
      
        characters = 0
      
        Colours_phones = {
            'Apple': 'WHITE',
            'Samsung': 'BLUE',
            'Google': 'RED',
            'OnePlus': 'MAGENTA',
            'Xiaomi': 'CYAN'
        }
      
        for Phone in selected_phones:
          for kk in Phone:
            brand_color = Colours_phones.get(Phone['Brand'], 'RESET')
            print(getattr(Fore, brand_color) + Phone[kk],  end = '')
            characters = len(Phone[kk])
            print((15 - characters)*' ', end = '')
          print()
      
          
elif fractals == True:
    print("Be blown away by the drawing of Aarush Van Gogh - The Fruit Laden Tree!")
    screen = turtle.Screen()
    screen.setup(width=1000, height=800)
    screen.bgcolor("orange")  # Sunset sky

    # =========================
    # Draw Sun
    # =========================

    sun = turtle.Turtle()
    sun.hideturtle()
    sun.speed(0)
    sun.penup()
    sun.goto(250, 150)
    sun.color("gold")

    sun.begin_fill()
    sun.circle(60)
    sun.end_fill()

    # =========================
    # Draw Grass
    # =========================

    ground = turtle.Turtle()
    ground.hideturtle()
    ground.speed(0)
    ground.penup()
    ground.goto(-500, -250)
    ground.color("darkgreen")

    ground.begin_fill()
    for _ in range(2):
        ground.forward(1000)
        ground.right(90)
        ground.forward(300)
        ground.right(90)
    ground.end_fill()

    # =========================
    # Main Turtle
    # =========================

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # =========================
    # Recursive Square Fractal
    # =========================

    def square(x, y, l):

        t.color("black")
        t.pensize(1)

        t.penup()
        t.goto(x, y)
        t.pendown()

        t.goto(x + l, y)
        t.goto(x + l, y + l)
        t.goto(x, y + l)
        t.goto(x, y)

        if l > 10:
            square(x + 3/4 * l, y + 1/4 * l, l/2)
            square(x - 1/4 * l, y + 1/4 * l, l/2)


    # =========================
    # Fruit Tree Fractal
    # =========================

    def branch(sz, level):

        if level > 0:

            t.color("saddlebrown")

            if level >= 8:
                t.pensize(10)
            elif level >= 5:
                t.pensize(6)
            else:
                t.pensize(2)

            t.forward(sz)

            angle = random.randint(20, 30)

            t.right(angle)
            branch(sz * 0.75, level - 1)

            t.left(angle * 2)
            branch(sz * 0.75, level - 1)

            t.right(angle)
            t.backward(sz)

        else:
            # Leaf
            t.color("green")
            t.dot(14)

            # Fruit
            if random.random() < .99:
                t.color("red")
                t.dot(8)


    # =========================
    # Draw Square Fractal
    # =========================

    square(-100, -100, 200)

    input("Press Enter to draw the sunset fruit tree...")

    # =========================
    # Clear only the fractal
    # =========================

    t.clear()

    # =========================
    # Draw Tree
    # =========================

    t.penup()
    t.goto(0, -250)
    t.pendown()

    t.setheading(90)

    branch(100, 9)

    ts.mainloop() 

   

    turtle.done()
elif welcome_message == True:
    print("You have reached the welcome message game!")
    import time
    import random

    # --- Short Form Creation ---
    def short_form(idx, *names, **addons):
        final = ''
        try:
            # Build short form from names
            for name in names:
                final += name[idx]

            # Add prefix/suffix if provided
            for keys in addons:
                if keys == 'prefix':
                    final = addons[keys] + final
                elif keys == 'suffix':
                    final = final + addons[keys]
                else:
                    print('You are not good at typing, are you ...')

            # --- Time Validation ---
            current_second = int(time.time()) % 60
            if current_second % 2 == 0:
                print(" The clock favors you...")
            else:
                raise Exception(" The sands of time resist you...")

            # --- Luck Validation ---
            roll = random.randint(1, 10)
            if roll > 5:
                print(" Fortune smiles upon you...")
            else:
                raise Exception(" Luck has abandoned you...")

        except TypeError as e:
            print('Wrong data type: ', e)
        except IndexError as e:
            print('Indexing is going wrong:', e)
        except Exception as e:
            print('Validation failed:', e)
        else:
            return final
        finally:
            print("Hope you managed to pass this stage ...")

    # --- Name Strength Calculation ---
    strength = {'name':10, 'surname':20, 'nickname':30, 'alias':40, 'aka':50}

    def name_strength(**fullname):
        result = 0
        try:
            for key, value in fullname.items():
                result += strength[key] * len(value)
        except KeyError as e:
            print(" You invoked forbidden fields:", e)
        else:
            return result

    # --- Validation Trials ---
    def validate(**prelimdata):
        try:
            assert prelimdata['sc'] is not None
            assert prelimdata['ns'] is not None
        except KeyError as e:
            print(" You dropped the scrolls of data...")
            print("Validation failed due to", e)
        except AssertionError:
            print(" One of the earlier steps has gone wrong.")
            print("Validation failed.")
        else:
            print(" Looking good so far...")
            print("Sending for deeper validation...")
            print(" Opening connection to the Oracle server...")
            try:
                deep_validate(prelimdata)
                luck_validate()
                time_validate()
                final_boss()
            except ValueError as e:
                print(" The Oracle rejects you:", e)
                print("Validation failed.")
            else:
                print(" Congrats, hero! Validation Successful.")
                print("Welcome to the Den of Coders!")
            finally:
                print(" Closing connection to the Oracle server")

    def deep_validate(prelimdata):
        print(" The Oracle studies your scrolls:", prelimdata)
        threshold_ns = random.randint(1, 200)
        threshold_sc = random.randint(10, 20)
        print(f" Thresholds: ns={threshold_ns}, sc={threshold_sc}")
        if prelimdata['ns'] > threshold_ns or len(prelimdata['sc']) > threshold_sc:
            raise ValueError("Your power is unstable...")



    # --- Final Boss Stage ---
    def final_boss():
        riddles = {
            "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?": "echo",
            "The more you take, the more you leave behind. What am I?": "footsteps",
            "I’m always running but never move. You can’t see me but you can feel me. What am I?": "time"
        }
        riddle, answer = random.choice(list(riddles.items()))
        print(" The Final Boss appears!")
        print(" Riddle of the Oracle:")
        print(riddle)
        user_answer = input("Your answer, adventurer: ").strip().lower()
        if user_answer != answer:
            raise ValueError("The riddle defeated you...")
        else:
            print(" You solved the riddle! The Oracle bows to your wisdom.")

    # --- Storyline Intro ---
    print(" Welcome, brave coder, to the Programmers' Den!")
    print("Your quest: forge your identity, prove your strength, and survive the trials of validation...")
    print()
    print(" Step 1: Create a short code → sc = short_form(idx, words..., prefix= , suffix= )")
    print(" Step 2: Measure your name strength → ns = name_strength(name= , surname= , aka= , alias= )")
    print(" Step 3: Face the Oracle → validate(sc=sc, ns=ns)")
    print()
    print("Good luck, adventurer...")



elif top_trumps == True:
    print("You have reached the top trumps game!")
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
