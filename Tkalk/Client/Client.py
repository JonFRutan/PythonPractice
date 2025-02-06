from socket import *
from tkinter import *
from tkinter import ttk
import re, sys

root = Tk()
display_frame = ttk.Frame(root, padding=10)
display_frame.grid()
ttk.Label(display_frame, text="Client").grid(column=0, row=0)
ttk.Button(display_frame, text="Exit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
