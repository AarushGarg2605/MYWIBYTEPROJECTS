import tkinter as tk
from collections import defaultdict, deque

def calculate():
    start = start_station.get()
    stop = stop_station.get()
    
    if not start or not stop:
        farelabel.configure(text='Select both stations')
        return

    if start == stop:
        farelabel.configure(text='FARE = INR 0')
        return

    # 1. Build a network graph connecting adjacent stations
    graph = defaultdict(list)
    lines = [purple_line, green_line, yellow_line, pink_line, blue_line]
    
    for line in lines:
        for i in range(len(line)):
            if i > 0:
                graph[line[i]].append(line[i-1])
            if i < len(line) - 1:
                graph[line[i]].append(line[i+1])

    # 2. Use Breadth-First Search (BFS) to find the shortest route
    queue = deque([[start]])
    visited = {start}
    shortest_path = None

    while queue:
        path = queue.popleft()
        current_station = path[-1]

        if current_station == stop:
            shortest_path = path
            break

        for neighbor in graph[current_station]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    # 3. Calculate fare based on number of stops
    if shortest_path:
        n_stops = len(shortest_path) - 1
        fare = n_stops * 10
        farelabel.configure(text='FARE = INR ' + str(fare))
    else:
        farelabel.configure(text='Route not found')

window = tk.Tk()
window.title("Namma Metro Map - Bangalore")
window.configure(bg='DarkGreen')
window.geometry("900x850+10+0")

c = tk.Canvas(window, width=850, height=650, bg='white')
c.pack(pady=10)

purple_line = ['Challaghatta', 'Kengeri', 'Mysore Road', 'Vijayanagar', 'Majestic', 'MG Road', 'Indiranagar', 'Baiyappanahalli', 'KR Puram', 'Whitefield']
green_line = ['BIEC', 'Dasarahalli', 'Yeshwanthpur', 'Malleswaram', 'Majestic', 'Chickpet', 'Jayanagar', 'Banashankari', 'Silk Institute']
yellow_line = ['Jayanagar', 'BTM Layout', 'Silk Board', 'Electronic City', 'Bommasandra']
pink_line = ['Kalena Agrahara', 'Dairy Circle', 'MG Road', 'Cantonment', 'Nagawara']
blue_line = ['Silk Board', 'Bellandur', 'Marathahalli', 'KR Puram', 'Kalyan Nagar', 'Nagawara', 'Hebbal', 'Airport']

r_stn = 6

def draw_metro_line(stn_list, init_pos, step, label_offset, clr):
    x_s = init_pos[0]
    y_s = init_pos[1]
    x_step = step[0]
    y_step = step[1]
    for stn in stn_list:
        if stn != stn_list[-1]:
            c.create_line(x_s, y_s, x_s + x_step, y_s + y_step, fill=clr, width=4)
        c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, fill='white', outline=clr, width=2)
        c.create_text(x_s + label_offset[0], y_s + label_offset[1], text=stn, fill='black', font=('Helvetica 7 bold'))
        x_s = x_s + x_step
        y_s = y_s + y_step

draw_metro_line(purple_line, [50, 300], [80, 0], [0, 15], 'purple')
draw_metro_line(green_line, [370, 50], [0, 65], [50, 0], 'green')
draw_metro_line(yellow_line, [370, 440], [70, 40], [45, 5], 'gold')
draw_metro_line(pink_line, [450, 550], [0, -90], [-45, 0], 'deep pink')
draw_metro_line(blue_line, [510, 520], [60, -45], [35, -10], 'blue')

all_stations = sorted(list(set(purple_line + green_line + yellow_line + pink_line + blue_line)))

controls_frame = tk.Frame(window, bg='DarkGreen')
controls_frame.pack(pady=10)

tk.Label(controls_frame, text='Start Station:', bg='DarkGreen', fg='white', font=('Helvetica 10 bold')).grid(row=0, column=0, padx=10)
start_station = tk.StringVar()
drop_start = tk.OptionMenu(controls_frame, start_station, *all_stations)
drop_start.grid(row=0, column=1, padx=10)

tk.Label(controls_frame, text='Stop Station:', bg='DarkGreen', fg='white', font=('Helvetica 10 bold')).grid(row=0, column=2, padx=10)
stop_station = tk.StringVar()
drop_stop = tk.OptionMenu(controls_frame, stop_station, *all_stations)
drop_stop.grid(row=0, column=3, padx=10)

button = tk.Button(window, text="Calculate Fare", command=calculate, font=('Helvetica 10 bold'), bg='Orange', fg='black')
button.pack(pady=5)

farelabel = tk.Label(window, text='FARE = ', font=('Helvetica 14 bold'), bg='DarkGreen', fg='white')
farelabel.pack(pady=5)

tk.mainloop()