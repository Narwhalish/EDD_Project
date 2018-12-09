import tkinter as tk

root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("EDD Interface")

volume_input = tk.Frame(root)
volume_input.pack()
volume_input.place(height = 500, width = 500)

home_frame = tk.Frame(root)
home_frame.pack()
home_frame.place(height = 500, width = 500)

volume = 0

def input():    #save number entered as desired volume
    volume = number.get()
    print(volume)

def pour():
    pass

def clean():
    #should call the same pymata pour thing as clean, except like a billion times faster
    pass

#buttons on home_frame
volume = tk.Button(home_frame, text="Input New Volume", command = volume_input.lift, height = 10, width = 20)
cont = tk.Button(home_frame, text="Continue Pour", command = pour, height = 10, width = 20)
clean = tk.Button(home_frame, text="Clean", command = clean, height = 10, width = 20)

#buttons on volume_input
number = tk.Entry(volume_input)
confirm = tk.Button(volume_input, text="Ok", command = input)
pour=tk.Button(volume_input, text="Pour", command = pour, height = 10, width = 20)
back=tk.Button(volume_input, text="Back to Home", command = home_frame.lift, height = 10, width = 20)

#packing buttons on home_frame
volume.pack(side=tk.TOP)
cont.pack(side=tk.TOP)
clean.pack(side=tk.TOP)

#packing buttons on volume_input
"""
number.pack(side=tk.TOP)
confirm.pack(side=tk.TOP)
pour.pack(side=tk.BOTTOM)
back.pack(side=tk.BOTTOM)
"""

#creating num_pad
btn_list = [
'1',  '2',  '3',
'4',  '5',  '6',
'7',  '8',  '9', '0']

r = 1
c = 0
for b in btn_list:
    cmd= lambda b=b: print(b)
    b = tk.Button(volume_input, text=b,width=5,command=cmd).grid(row = r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

root.mainloop()
