import tkinter as tk
import motor_test

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("EDD Interface")

volume = tk.Button(frame, text="Input New Volume", command = motor.measure)
volume.pack(side=tk.LEFT)
cont = tk.Button(frame, text="Continue Pour", command = motor.pour)
cont.pack(side=tk.LEFT)
clean = tk.Button(frame, text="Clean", command = motor.clean)
clean.pack(side=tk.LEFT)

#testing connection with arduino
blink = tk.Button(frame, text="BLINK", command = motor.blink)
blink.pack(side=tk.BOTTOM)

root.mainloop()
