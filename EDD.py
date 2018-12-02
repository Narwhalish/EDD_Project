import tkinter as tk
import motor_test

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("EDD Interface")

def volume():
    pass

def pour():
    pass

def clean():
    pass

volume = tk.Button(frame, text="Input New Volume", command = volume)
volume.pack(side=tk.LEFT)
cont = tk.Button(frame, text="Continue Pour", command = pour)
cont.pack(side=tk.LEFT)
clean = tk.Button(frame, text="Clean", command = clean)
clean.pack(side=tk.LEFT)

#testing connection with arduino
blink = tk.Button(frame, text="BLINK", command = motor_test.blink)
blink.pack(side=tk.BOTTOM)

root.mainloop()
