#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import tkinter as tk
import tkinter.font
import arduino

# Initialize custom PyMata3 object and nest Tk object within root
board = arduino.Uno()
root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("EDD Interface")

volume_input = tk.Frame(root)
volume_input.pack()
volume_input.place(height = 480, width = 800)

home_frame = tk.Frame(root)
home_frame.pack()
home_frame.place(height = 480, width = 800)

# Create fonts for proper sizing in GUI
main_page_font = tkinter.font.Font(family = "Times", size = 60)
our_font = tkinter.font.Font(family = "Times", size = 27)

# Initialize variables to store desired amounts
input_amount = ''
desired_amount = 0

# Create buttons for home_frame
volume = tk.Button(home_frame, text="Input New Volume", font = main_page_font, command=volume_input.lift)
cont = tk.Button(home_frame, text="Continue Pour", font = main_page_font, command=board.pour_amount())
clean = tk.Button(home_frame, text="Clean", font = main_page_font, command=board.clean_container)

# quit = tk.Button(home_frame, text="Quit", font = our_font, command = root.destroy) Quit functionality is not required in production version

# Clear inputted values saved and displayed rfom input_amount
def clear_input():
    global desired_amount, input_amount, number
    desired_amount = 0
    input_amount = ''
    number.config(text=input_amount)

# Create buttons for volume_input
number = tk.Label(volume_input, text = input_amount, font = our_font)
confirm = tk.Button(volume_input, text="Ok", font = our_font, command=lambda: board.set_amount(desired_amount))
pour=tk.Button(volume_input, text="Pour", font = our_font, command=board.pour_amount)
back=tk.Button(volume_input, text="Back to Home", font = our_font, command = home_frame.lift)
clear = tk.Button(volume_input, text="Clear", font = our_font, command = clear_input)

# Pack buttons in home_frame
volume.pack(side=tk.TOP)
cont.pack(side=tk.TOP)
clean.pack(side=tk.TOP)
#quit.pack(side=tk.TOP) Quit functionality is not required in production version


# Grid buttons in volume_input
number.grid(row = 0, column = 0)
confirm.grid(row = 0, column = 1)
pour.grid(row = 1, column = 0)
back.grid(row = 1, column = 1)
clear.grid(row = 0, column = 2)

# Adds numbers entered by the buttons to the displayed number
def add_to_entry(val):
    global desired_amount, input_amount, number
    input_amount += val
    desired_amount = int(input_amount)
    print(desired_amount)
    number.config(text=input_amount)

# Create buttons for numberpad using an algorithm to set 3 buttons per row. Button '0' is placed on its own row.
btn_list = [
'1',  '2',  '3',
'4',  '5',  '6',
'7',  '8',  '9', '0']

r = 4
c = 3
num = 0
cmd = lambda x: add_to_entry(x)
for b in btn_list:
    button = tk.Button(volume_input, text=b, font = our_font, command=lambda num = b: cmd(num)).grid(row=r, column=c)
    c += 1
    if c > 5:
        c = 3
        r += 1

# Begin main loop of Tkinter window
root.mainloop()
