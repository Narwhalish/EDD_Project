import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        self.master = master
        master.title("EDD Interface")

        self.label("[PRODUCT NAME]")
        self.label.pack()

        button-new-volume = Button(master, text = "Input New Volume", command = volume)
        button-cont-pour = Button(master, text = "Continue Pour", command = pour)
        button-clean = Button(master, text = "Clean", command = clean)

        
        
    def volume():
        pass

    def pour():
        pass

    def clean():
        pass

def main():
    app = Application()

