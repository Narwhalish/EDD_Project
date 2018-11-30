import tkinter as tk
import serial

#remember to install serial and RPi
ser = serial.Serial("/dev/ttyACM0", 9600)
#execute ls/dev/tty* when arduino is connected to raspi

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("EDD Interface")


"""
class Application(tk.Frame):
    def __init__(self, master):
        self.master = master
        master.title("EDD Interface")

        self.label("[PRODUCT NAME]")
        self.label.pack()

        button-new-volume = Button(master, text = "Input New Volume", command = volume)
        button-cont-pour = Button(master, text = "Continue Pour", command = pour)
        button-clean = Button(master, text = "Clean", command = clean)
"""
def volume():
    pass

def pour():
    pass

def clean():
    pass


volume = tk.Button(frame,
                   text="Input New Volume",
                   command = volume)
volume.pack(side=tk.LEFT)
cont = tk.Button(frame,
                   text="Continue Pour", command = pour)
cont.pack(side=tk.LEFT)
clean = tk.Button(frame, text="Clean", command = clean)
clean.pack(side=tk.LEFT)
root.mainloop()
