import tkinter as tk

class GUI(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.home_buttons()

    def volume():
        for widget in self.winfo_children():
            widget.destroy
        number = tk.Entry(frame)


    def pour():
        pass

    def clean():
        pass

    def home_buttons(self):

        volume = tk.Button(self, text="Input New Volume", command = self.volume, height = 10, width = 20)
        cont = tk.Button(self, text="Continue Pour", command = self.pour, height = 10, width = 20)
        clean = tk.Button(self, text="Clean", command = self.clean, height = 10, width = 20)

        volume.grid(columnspan = 1)
        cont.grid(columnspan = 1)
        clean.grid(columnspan = 1)

root = GUI()
root.mainloop()

"""
root = tk.Tk()
root.geometry("500x500")
root.title("EDD Interface")
frame = tk.Frame(root)
frame.pack()
volume = 0

def home():
    frame.pack_forget()
    frame = tk.Frame(root)
    frame.pack()
    volume.pack(side=tk.LEFT)
    cont.pack(side=tk.LEFT)
    clean.pack(side=tk.LEFT)

def volume():
    volume.pack_forget()
    clean.pack_forget()
    cont.pack_forget()
    var = 0
    number.pack()
    confirm.pack()

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

volume = tk.Button(frame, text="Input New Volume", command = volume, height = 10, width = 20)
cont = tk.Button(frame, text="Continue Pour", command = pour, height = 10, width = 20)
clean = tk.Button(frame, text="Clean", command = clean, height = 10, width = 20)
number = tk.Entry(frame)
pour=tk.Button(frame, text="Pour", command = pour, height = 10, width = 20)
back=tk.Button(frame, text="Back to Home", command = home, height = 10, width = 20)
confirm = tk.Button(frame, text="Ok", command = input)

volume.pack(side=tk.LEFT)
cont.pack(side=tk.LEFT)
clean.pack(side=tk.LEFT)
root.mainloop()
"""
