#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import tkinter as tk
import tkinter.font
from functools import partial
import arduino

board = arduino.Uno()
root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("EDD Interface")

volume_input = tk.Frame(root)
volume_input.pack()
volume_input.place(height = 2000, width = 2000)

home_frame = tk.Frame(root)
home_frame.pack()
home_frame.place(height = 2000, width = 2000)

our_font = tkinter.font.Font(family = "Times", size = 30)

input_amount = ''
desired_amount = 0

#buttons on home_frame
volume = tk.Button(home_frame, text="Input New Volume", font = our_font, command=volume_input.lift, height = 5, width=20)
cont = tk.Button(home_frame, text="Continue Pour", font = our_font, width=20, height = 5)
clean = tk.Button(home_frame, text="Clean", font = our_font, command=board.clean_container, width=20, height = 5)

#quit button on home_frame
quit = tk.Button(home_frame, text="Quit", font = our_font, command = root.destroy, width = 20, height = 5)



#buttons on volume_input
number = tk.Label(volume_input, text = input_amount, font = our_font)
confirm = tk.Button(volume_input, text="Ok", font = our_font, command=lambda: board.set_amount(desired_amount))
pour=tk.Button(volume_input, text="Pour", font = our_font, command=board.pour_amount, width = 20)
back=tk.Button(volume_input, text="Back to Home", font = our_font, command = home_frame.lift, width = 20)

#packing buttons on home_frame
volume.pack(side=tk.TOP)
cont.pack(side=tk.TOP)
clean.pack(side=tk.TOP)
quit.pack(side=tk.TOP)

#grid buttons on volume_input
number.grid(row = 0, column = 0)
confirm.grid(row = 0, column = 1)
pour.grid(row = 1, column = 0)
back.grid(row = 1, column = 1)

def add_to_entry(val):
    global desired_amount, input_amount, number
    input_amount += val
    desired_amount = int(input_amount)
    print(desired_amount)
    number = tk.Label(volume_input, text=input_amount, font = our_font)
    number.grid(row = 0, column = 0)


#creating num_pad
btn_list = [
'1',  '2',  '3',
'4',  '5',  '6',
'7',  '8',  '9', '0']

r = 4
c = 3
num = 0
cmd = lambda x: add_to_entry(x)
for b in btn_list:
    button = tk.Button(volume_input, text=b, width=7, font = our_font, command=lambda num = b: cmd(num)).grid(row=r, column=c)
    c += 1
    if c > 7:
        c = 3
        r += 1

root.mainloop()
