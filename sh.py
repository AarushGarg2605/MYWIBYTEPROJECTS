import csv

print("Welcome to the Sports Heros project")
print('We are going to do some analysis on Fifa men\'s and womens singles champions')
print('Please see the file analysis.dat for the results')


def print_line(report_line):
  filename = 'analysis.dat'
  
  with open(filename, mode ='a') as file:
    file.write(report_line)

def print_table(table):
 
  
  filename = 'analysis.dat'

  with open(filename, mode ='a') as file:
    all_keys = list(table[0].keys())

    keys_line = ''
    for key in all_keys:
      keys_line = keys_line + key + (20 - len(key))*' '
      
    file.write(keys_line + '\n')

    for data in table:
      # Each data is a dictionary, we print the values.
      values_line = ''
      for values in data.values():
        values_line = values_line + str(values) + (20-len(str(values)))*' '

      file.write(values_line + '\n')



def initialize():
  filename = 'analysis.dat'

  with open(filename, mode ='w') as file:
    file.write('Analysis Results \n')


def print_set(winner_set):
  # Pass in a set and print its members one on each line. 
  filename = 'analysis.dat'

  with open(filename, mode ='a') as file:
    for winner in winner_set:
       file.write(winner + ' , ')
    file.write('\n\n')



def readcsvdata(tournament_name):
  filename = tournament_name + '.csv'
  # Open the file
  # Read the data into a list of dictionaries
  with open(filename, mode ='r') as file:
    csvFile = csv.DictReader(file)
    tournament_data = list(csvFile)

  return tournament_data

  
  


def analyze(tname, tdata):
  # Create a list of winners
  winners_list = []
  
  for winner in tdata:
    winners_list.append(winner['Champion'])


  winners_set = set(winners_list)

  print_line('Reporting for ' + tname + '\n' )
  print_line('Total Winners : ' + str(len(winners_list)) + '\n')
  print_line('Unique Winners : ' + str(len(winners_set)) + '\n')

  winners_info_list = []  
  for player in winners_set:
    # Look through the list to find all items where the Champion is the particular player
    # (SAME problem statement as we had in the laptop store)
    # Use list comprehension to do this. 
    country_info = {}
    selected = [chosen for chosen in tdata if chosen['Champion'] == player]
    # Update the dictionary
    
    country_info['Country'] = selected[0]['Country']
    country_info['Times Won'] = len(selected)
    country_info['Years Won'] = []
    for kk in selected:
      country_info['Years Won'].append(kk['Year'])

    winners_info_list.append(country_info)

  print_table(winners_info_list)


  
  mto_winners_set = set()

  for player in winners_set:
    mto_winners_set.add(player)

  for player in winners_set:
    selected = [chosen for chosen in winners_info_list if chosen['Country'] == player]
    if selected[0]['Times Won'] == 1:
      mto_winners_set.remove(player)

  
  return winners_set, mto_winners_set




def comparative_analysis(winner_set1, winner_set2):

  winners_eitheror = winner_set1 | winner_set2
  winners_both = winner_set1 & winner_set2
  winners_only1 = winner_set1 - winner_set2
  winners_only2 = winner_set2 - winner_set1
  winners_onlyone_notboth = winner_set1 ^ winner_set2

  print_line('Winners (Either/Or): ' + str(len(winners_eitheror)) + '\n')
  print_line('These are: \n')
  print_set(winners_eitheror)
  
  print_line('Winners (Both): ' + str(len(winners_both)) + '\n')
  print_line('These are: \n')
  print_set(winners_both)
  
  print_line('Winners (Only 1, not both): ' + str(len(winners_onlyone_notboth)) + '\n')

  print_line('These are: \n')
  print_set(winners_onlyone_notboth)

  
  print_line('Winners (Only only men not women): ' + str(len(winners_only1)) + '\n')
  print_line('These are: \n')
  print_set(winners_only1)

  
  print_line('Winners (only women not men): ' + str(len(winners_only2)) + '\n')
  print_line('These are: \n')
  print_set(winners_only2)
  

      
initialize()


fifamen_data = readcsvdata('fifamen')
fifawomen_data = readcsvdata('fifawomen')

fifamen_winners, fifamen_mto_winners = analyze('fifamen', fifamen_data)
fifawomen_winners, fifawomen_mto_winners = analyze('fifawomen', fifawomen_data)

comparative_analysis(fifamen_winners, fifawomen_winners)