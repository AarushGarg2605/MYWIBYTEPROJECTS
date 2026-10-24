import turtle
import time
print("Welcome to the game! ")
print('This is a fusion of what all we have learnt so far in this course. ')
print('Reach the green square to play the laptop store game, reach the red square to play the fractals game, reach the yellow square to play the welcome message game and reach the purple square to play the top trumps game. ')

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

gameover = False
laptopstore = False
fractals = False
welcome_message = False
top_trumps = False
while not gameover:
    t.forward(1)

    if t.distance(270, 270) < 45:
        laptopstore = True
        gameover = True
    elif t.distance(-270, 270) < 45:
        fractals = True
        gameover = True
    elif t.distance(-270, -270) < 45:
        welcome_message = True
        gameover = True
    elif t.distance(270, -270) < 45:
        top_trumps = True
        gameover = True


ts.bye()

    

ts.mainloop() 
import random 

try:
    
    from colorama import Fore
except ImportError:
      class _NoColour:
        def __getattr__(self, _name):
            return ''

      Fore = _NoColour()

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

    # =========================
    # Finish
    # =========================

    turtle.done()
elif welcome_message == True:
    print("You have reached the welcome message game!")
elif top_trumps == True:
    print("You have reached the top trumps game!")
