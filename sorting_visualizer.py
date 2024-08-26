from tkinter import *
from tkinter import ttk
import random
import time

# Sorting Algorithms
def bubble(data, drawData, timer):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['#FF6F61' if x == j + 1 else '#209CEE' for x in range(len(data))])
                time.sleep(timer)
    drawData(data, ['#8BC34A' for x in range(len(data))])

def selection_sort(data, drawData, timer):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        drawData(data, ['#FF6F61' if x == i or x == min_idx else '#209CEE' for x in range(len(data))])
        time.sleep(timer)
    drawData(data, ['#8BC34A' for x in range(len(data))])

def insertion_sort(data, drawData, timer):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        drawData(data, ['#FF6F61' if x <= i else '#209CEE' for x in range(len(data))])
        time.sleep(timer)
    drawData(data, ['#8BC34A' for x in range(len(data))])

# initializing root class for Tkinter
root = Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(1000, 700)
root.config(bg="#1E272E")

select_alg = StringVar()
data = []

# Function to generate the data values by accepting a given range
def generate():
    global data
    minval = int(minEntry.get())
    maxval = int(maxEntry.get())
    sizeval = int(sizeEntry.get())
    data = [random.randrange(minval, maxval + 1) for _ in range(sizeval)]
    drawData(data, ['#209CEE' for x in range(len(data))])

# Function to create the data bars by creating a canvas in Tkinter
def drawData(data, colorlist):
    canvas.delete("all")
    can_height = 400
    can_width = 850
    x_width = can_width/(len(data) + 1)
    offset = 30
    spacing = 10
    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing
        y0 = can_height - height * 340
        x1 = ((i + 1) * x_width) + offset
        y1 = can_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorlist[i], outline="")
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), fill="white", font=("Helvetica", 8, "bold"))
    root.update_idletasks()

# Function to display time complexity based on selected algorithm
def display_time_complexity():
    algorithm = algmenu.get()
    if algorithm == 'Bubble Sort':
        best_label.config(text="Best Case: O(n)")
        avg_label.config(text="Average Case: O(n^2)")
        worst_label.config(text="Worst Case: O(n^2)")
        space_label.config(text="Space Complexity: O(1)")
    elif algorithm == 'Selection Sort':
        best_label.config(text="Best Case: O(n^2)")
        avg_label.config(text="Average Case: O(n^2)")
        worst_label.config(text="Worst Case: O(n^2)")
        space_label.config(text="Space Complexity: O(1)")
    elif algorithm == 'Insertion Sort':
        best_label.config(text="Best Case: O(n)")
        avg_label.config(text="Average Case: O(n^2)")
        worst_label.config(text="Worst Case: O(n^2)")
        space_label.config(text="Space Complexity: O(1)")

# Function to initiate the sorting process
def start_algorithm():
    global data
    display_time_complexity()
    if algmenu.get() == 'Bubble Sort':
        bubble(data, drawData, speedbar.get())
    elif algmenu.get() == 'Selection Sort':
        selection_sort(data, drawData, speedbar.get())
    elif algmenu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, speedbar.get())

# Creating main user interface frame and basic layout by creating a frame
Mainframe = Frame(root, width=900, height=200, bg="#2F3640")
Mainframe.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=900, height=400, bg="#1E272E", bd=0, highlightthickness=0)
canvas.grid(row=1, column=0, padx=10, pady=5)

# Time Complexity Frame
complexity_frame = Frame(root, width=900, height=100, bg="#2F3640")
complexity_frame.grid(row=2, column=0, padx=10, pady=5)

best_label = Label(complexity_frame, text="Best Case: ", fg="#F5F6FA", bg="#2F3640", font=("Helvetica", 12, "bold"))
best_label.grid(row=0, column=0, padx=20, pady=5)

avg_label = Label(complexity_frame, text="Average Case: ", fg="#F5F6FA", bg="#2F3640", font=("Helvetica", 12, "bold"))
avg_label.grid(row=0, column=1, padx=20, pady=5)

worst_label = Label(complexity_frame, text="Worst Case: ", fg="#F5F6FA", bg="#2F3640", font=("Helvetica", 12, "bold"))
worst_label.grid(row=0, column=2, padx=20, pady=5)

space_label = Label(complexity_frame, text="Space Complexity: ", fg="#F5F6FA", bg="#2F3640", font=("Helvetica", 12, "bold"))
space_label.grid(row=0, column=3, padx=20, pady=5)

# Creating user interface area in grid manner
Label(Mainframe, text="ALGORITHM", bg='#2F3640', fg="#F5F6FA", font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky=W)

# Algorithm menu for showing the name of the sorting algorithm
algmenu = ttk.Combobox(Mainframe, textvariable=select_alg, values=["Bubble Sort", "Selection Sort", "Insertion Sort"], font=("Helvetica", 10, "bold"))
algmenu.grid(row=0, column=1, padx=5, pady=5)
algmenu.current(0)

# Creating Start Button to start the sorting visualization process
Button(Mainframe, text="START", bg="#E74C3C", fg="White", font=("Helvetica", 12, "bold"), command=start_algorithm).grid(row=1, column=3, padx=5, pady=5)

# Creating Speed Bar using scale in Tkinter
speedbar = Scale(Mainframe, from_=0.10, to=2.0, length=150, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed", fg="#F5F6FA", bg="#2F3640", font=("Helvetica", 10))
speedbar.grid(row=0, column=2, padx=5, pady=5)

# Second row components
sizeEntry = Scale(Mainframe, from_=3, to=60, resolution=1, orient=HORIZONTAL, label="Size", fg="#F5F6FA", bg="#2F3640", font=("Helvetica", 10))
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(Mainframe, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Minimum Value", fg="#F5F6FA", bg="#2F3640", font=("Helvetica", 10))
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(Mainframe, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Maximum Value", fg="#F5F6FA", bg="#2F3640", font=("Helvetica", 10))
maxEntry.grid(row=1, column=2, padx=5, pady=5)

# Creating generate button
Button(Mainframe, text="Generate", bg="#27AE60", fg="White", font=("Helvetica", 12, "bold"), command=generate).grid(row=0, column=3, padx=5, pady=5)

root.mainloop()