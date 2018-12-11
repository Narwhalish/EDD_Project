import tkinter as tk
import board

root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("EDD Interface")

volume_input = tk.Frame(root)
volume_input.pack()
volume_input.place(height = 2000, width = 2000)

home_frame = tk.Frame(root)
home_frame.pack()
home_frame.place(height = 2000, width = 2000)

desired_height = 0

def input():    #save number entered as desired volume
    desired_height = number.get() / (11.5 * 5)
    print(desired_height)

def clean():
    #should call the same pymata pour thing as clean, except like a billion times faster
    pass

#buttons on home_frame
volume = tk.Button(home_frame, text="Input New Volume", command = volume_input.lift, height = 10, width = 20)
cont = tk.Button(home_frame, text="Continue Pour", command = lambda: board.pour(volume), height = 10, width = 20)
clean = tk.Button(home_frame, text="Clean", command = clean, height = 10, width = 20)

#buttons on volume_input
number = tk.Text(volume_input)
confirm = tk.Button(volume_input, text="Ok", command = input)
pour=tk.Button(volume_input, text="Pour", command = pour, height = 10, width = 20)
back=tk.Button(volume_input, text="Back to Home", command = home_frame.lift, height = 10, width = 20)

#packing buttons on home_frame
volume.pack(side=tk.TOP)
cont.pack(side=tk.TOP)
clean.pack(side=tk.TOP)

#grid buttons on volume_input
number.grid(row = 0, column = 0)
confirm.grid(row = 0, column = 1)
pour.grid(row = 1, column = 0)
back.grid(row = 1, column = 1)

#creating num_pad
btn_list = [
'1',  '2',  '3',
'4',  '5',  '6',
'7',  '8',  '9', '0']

def add_to_entry(self):
    global entry
    print(val)
    entry += val
    print(entry)

r = 10
c = 3
for b in btn_list:
    print(b)
    print(type(b))
    b = tk.Button(volume_input, text=b,width=5,command=lambda: add_to_entry(self.cget('text'))).grid(row = r, column = c)
    c += 1
    if c > 7:
        c = 3
        r += 1

root.mainloop()
