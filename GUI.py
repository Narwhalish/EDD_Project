import tkinter as tk
import main

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("EDD Interface")
volume = 0

def volume():
    var = 0
    number = tk.Entry(frame, textvariable = var)
    number.pack()
    confirm = tk.Button(frame, text="Ok", command = input)
    confirm.pack()

def input():
    volume = root.number.get()
    print(volume)

volume = tk.Button(frame, text="Input New Volume", command = volume)
volume.pack(side=tk.LEFT)
cont = tk.Button(frame, text="Continue Pour", command = main.pour)
cont.pack(side=tk.LEFT)
clean = tk.Button(frame, text="Clean", command = main.clean)
clean.pack(side=tk.LEFT)

root.mainloop()
