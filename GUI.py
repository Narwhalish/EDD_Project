import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.attributes("-fullscreen", True)
root.title("EDD Interface")

volume_input = tk.Frame(root)
volume_input.pack()
volume_input.place(height = 500, width = 500)

home_frame = tk.Frame(root)
home_frame.pack()
home_frame.place(height = 500, width = 500)

volume = 0

def input():
    volume = number.get()
    confirm.pack_forget()
    pour.pack()
    back.pack()

def pour():
    pass

def clean():
    #should call the same pymata pour thing as clean, except like a billion times faster
    pass

#buttons on homepage
volume = tk.Button(home_frame, text="Input New Volume", command = volume_input.lift, height = 10, width = 20)
cont = tk.Button(home_frame, text="Continue Pour", command = pour, height = 10, width = 20)
clean = tk.Button(home_frame, text="Clean", command = clean, height = 10, width = 20)

#buttons after clicking volume button
number = tk.Entry(volume_input)
confirm = tk.Button(volume_input, text="Ok", command = input)
pour=tk.Button(volume_input, text="Pour", command = pour, height = 10, width = 20)
back=tk.Button(volume_input, text="Back to Home", command = home_frame.lift, height = 10, width = 20)

#packing buttons on homepage
volume.pack(side=tk.TOP)
cont.pack(side=tk.TOP)
clean.pack(side=tk.TOP)

#packing buttons for inputing volume
number.pack()
confirm.pack()
pour.pack()
back.pack()

root.mainloop()
