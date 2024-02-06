from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title('Draw Board')
root.geometry('1200x700+149+52')  # Increased canvas size
root.configure(bg='#f0f3f5')
root.resizable(False, False)

def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_x, current_y, erasing
    if not erasing:
        canvas.create_line((current_x, current_y, work.x, work.y), width=get_current_value(), fill=color, capstyle=ROUND, smooth=TRUE)
        current_x, current_y = work.x, work.y
    else:
        canvas.create_line((work.x, work.y, work.x + 1, work.y + 1), width=get_current_value() * 2, fill='white', capstyle=ROUND, smooth=TRUE)

def show_color(new_color):
    global color
    color = new_color
    update_highlight(new_color)

def update_highlight(selected_color):
    for tag in colors.find_all():
        if selected_color in colors.gettags(tag):
            colors.itemconfig(tag, outline='#8B4513', width=3)  # Use a darker brown shade and increase the width
        else:
            colors.itemconfig(tag, outline='')

def new_canvas():
    canvas.delete('all')
    display_palette()




image_icon = PhotoImage(file="C:\\Users\\dutta\\Downloads\\logo (2).png")
root.iconphoto(False, image_icon)

color_box = PhotoImage(file="C:\\Users\\dutta\\Downloads\\color section (1).png")
Label(root, image=color_box, bg='#f2f3f5').place(x=10, y=20)

eraser = PhotoImage(file="C:\\Users\\dutta\\Downloads\\eraser.png")
eraser_button = Button(root, image=eraser, bg='#f2f3f5', command=new_canvas)
eraser_button.place(x=30, y=375)

colors = Canvas(root, bg='#ffffff', width=37, height=300, bd=0)
colors.place(x=30, y=60)

def display_palette():
    color_list = ['black', 'red', 'green', 'blue', 'pink', 'yellow', 'orange', 'purple', 'grey', 'white']
    for i, color in enumerate(color_list):
        id = colors.create_rectangle((10, 10 + i * 30, 30, 30 + i * 30), fill=color, outline='', tags=(color,))
        colors.tag_bind(id, '<Button-1>', lambda event, col=color: show_color(col))

display_palette()

canvas = Canvas(root, width=930, height=600, background='white', cursor='hand2')  # Increased canvas size
canvas.place(x=150, y=10)  # Adjusted canvas position

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addLine)

current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=slider_changed, variable=current_value)
slider.place(x=3, y=530)

value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27, y=550)

erasing = False  # Flag to indicate whether eraser mode is active

root.mainloop()
