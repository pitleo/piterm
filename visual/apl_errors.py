import errors
import tkinter
from tkinter.messagebox import *
from visual import bg

def errorbad():
    tkinter.messagebox.showwarning("Uh oh!", "Application has stopped!")
def errortest():
    tkinter.messagebox.showwarning("Uh oh!", "System will now close.")
def errorinfo():
    tkinter.messagebox.showinfo("Notice", "System has been configured.")
def bubble1():
    print("\a")
    tkinter.messagebox.showinfo("Hint:", "This shouldn't appear?!")
