import os
import sys
try:
    import tkinter
    
    root = tkinter.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    print(f"Screen width: {screen_width} pixels")
    print(f"Screen height: {screen_height} pixels")
    root.destroy()
except:
    print("bhe")