try:
  from colorama import Fore
except ImportError:
  class _NoColour:
    def __getattr__(self, _name):
      return ''

  Fore = _NoColour()
import random
cars = {'brand':'', 'Model': '', 'Engines': '','Seat ':'','Transmission':'','Fuel':'','Colour': '','Price':''}


print('Welcome to STORE OF GREATNESS.')
print('We have a huge inventory of cars, phones and .')
User_choice = input('Please type 1 for cars and 2 for phones(i know this is random but....) ')
print()


def append_s(name):
  return name + 's'




print()

if User_choice == '1':

 Cars_list      = []
 print('You have chosen Cars')
 print('Please selct your specs')

 specs = ['Brand', 'Model', 'Engine', 'Seat', 'Transmission','Fuel', 'Colour','Price']

 specs_new = list(map(append_s, specs))
 master_dict = dict.fromkeys(specs_new)

 master_dict['Brands'] =  ['Ferrari', 'Lamborghini', 'Lotus', 'Koenisegg', 'Pagani','Aston martin','Bentley','Rolls Royce','Buggati']

 brand_model_mapping = {
     'Ferrari': ['812 Superfast', 'SF90 Stradale','250GTO','Testarossa','F40','F50','Enzo','360 Modena','F430','458 Italia','488 GTB','F8 Tributo','Luce','LaFerrari','Roma'],
     'Lamborghini': ['Aventador SVJ','Urus','Revuelto','Aventador','Huracán','Veneno','Diablo','Countach','Miura','350 GT','Espada','Murciélago'],
     'Lotus': ['Evija', 'Emira','Cortina','Elite','Eletre','3-Eleven'],
     'Koenisegg': ['Jesko', 'Regera'],
     'Pagani': ['Huayra', 'Zonda R','Utopia','Zonda Cinque'],
     'Aston martin': ['Rapide', 'DB11','Vantage','Vanquish','Vulcan','Valhalla'],
     'Bentley': ['Mulsanne', 'Continental GT','Flying spur','Azure','Batur','Turbo R'],
     'Rolls Royce': ['Phantom', 'Cullinan','Ghost','Wraith','Dawn','Spectre','Silver Shadow','Silver Resaph','Camargue','Corniche','Park Ward','Sweptail','Droptail'],
     'Buggati': ['Chiron', 'Divo','Veyron','Chiron Pur Sport','Centodieci','Bolide','Mistral','Tourbillion']
 }
 # master_dict['Models'] is kept for reference but not directly used for random choice in the new logic
 master_dict['Models'] = list(set(model for models in brand_model_mapping.values() for model in models))
 master_dict['Engines'] = ['V12', 'V8', 'W16','Hybrid V6','Hybrid V8','Hybrid V12','Turbo V8','Turbo V6','V6']
 master_dict['Transmissions'] = ['Manual', 'Automatic', 'Dual clutch']
 master_dict['Fuels'] = [ 'Petrol','Diesel','Ev']
 master_dict['Colours'] = [ 'Red', 'Green', 'Yellow', 'Blue','Black','Silver','White']
 master_dict['Prices'] = [ 'INR 10,00,00,000', 'INR 15,00,00,000', 'INR 5,00,00,000', ' INR 35,00,00,000','INR 20,00,00,000','INR 25,00,00,000','INR 30,00,00,000','INR 40,00,00,000']
 master_dict['Seats'] = ['2 seater', '4 seater']



 
 for n_Cars  in range(100):
  new_car = dict.fromkeys(specs)

  # First, choose a Brand for the car
  chosen_brand = random.choice(master_dict['Brands'])
  new_car['Brand'] = chosen_brand

  # Then, choose a Model that is specific to the chosen Brand
  if chosen_brand in brand_model_mapping:
      new_car['Model'] = random.choice(brand_model_mapping[chosen_brand])
  else:
      # Fallback: if a brand is unexpectedly not in the mapping, pick a model from the general list
      # This should ideally not happen with the current setup.
      new_car['Model'] = random.choice(master_dict['Models'])

  # Populate other specs randomly
  for kk in new_car:
    if kk not in ['Brand', 'Model']: # Skip Brand and Model as they are already set
        new_car[kk] = random.choice(master_dict[kk+'s'])
  Cars_list.append(new_car)  # Moved outside the inner loop

 pref = input('Please indicate the specifications which you have a preference for (comma seperated):')
 pref_list = pref.split(',')
 pref_list = list(map(str.strip, pref_list))


 user_choice = dict.fromkeys(specs)




 for kk in specs:
  if kk in pref_list:
    if kk != 'Model':
     pref_str = '/'.join(master_dict[kk+'s'])
    else:
     pref_str = '/'.join(brand_model_mapping[user_choice['Brand']]) # Changed 'models' to 'brand_model_mapping'

    user_choice[kk] = input('Any preference for ' + kk +':'+ pref_str+ ' (Enter none for no preference)'+'\n')
  else:
    user_choice[kk]= 'none'




 query = ''

 for kk in user_choice:
  # Treat empty input or 'none' as no preference
  if user_choice[kk].lower() == 'none' or user_choice[kk].strip() == '':
    pass
  else:
 
    query = query + "Car['" + kk + "'] == '" + user_choice[kk] + "' and "

 print(query)


 

 
 query = query[0:-4] if query else ''



 if query != '':
   selected = [Car for Car in Cars_list if eval(query)] # Changed variable name from Cars to Car for clarity
 else:
   selected = Cars_list # If query is empty, all cars are selected


 print(len(selected), 'These are the cars that met your preference .')



 Sorting_key = input('Results to be sorted by(none for no sorting)')
 sorting_rev = input('enter D for descending order')

 # Mapping for sorting keys to handle singular/plural and case variations
 sorting_key_map = {
     'brand': 'Brand',
     'brands': 'Brand',
     'model': 'Model',
     'models': 'Model',
     'engine': 'Engine',
     'engines': 'Engine',
     'seat': 'Seat',
     'seats': 'Seat',
     'transmission': 'Transmission',
     'transmissions': 'Transmission',
     'fuel': 'Fuel',
     'fuels': 'Fuel',
     'colour': 'Colour',
     'colours': 'Colour',
     'price': 'Price',
     'prices': 'Price'
 }

 sort_by = sorting_key_map.get(Sorting_key.lower())

 if sort_by:
    if sort_by == 'Price':
        selected = sorted(selected, key=lambda x: float(x[sort_by].split()[1].replace(',', '')), reverse=(sorting_rev == 'D'))
    else: # For all other string-based keys like Brand, Model, etc.
        selected = sorted(selected, key=lambda x: x[sort_by], reverse=(sorting_rev == 'D'))



 characters = 0
 for kk in specs:
  print(kk, end = '')
  characters = len(kk)
  print((15 - characters)*' ', end = '')
 print()

 characters = 0


 Colours = {'Ferrari':'RED','Lamborghini':'LIGHTGREEN_EX','Lotus':'LIGHTRED_EX' , 'Pagani':'CYAN','Lotus':'LIGHTBLACK_EX','Koenisegg':'MAGENTA','Aston martin':'YELLOW','Buggati':'BLUE','Rolls Royce':'WHITE','Bentley':'GREEN'} 



 for Cars in selected:
  for kk in Cars:
    print(getattr(Fore,Colours[Cars['Brand']].upper())+Cars[kk],  end = '')
    characters = len(Cars[kk])
    print((15 - characters)*' ', end = '')
  print()


elif User_choice == '2':
  print('You have chosen Phones')
  print('Please select your specs')
  Phone_list      = []


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
    print((70

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

