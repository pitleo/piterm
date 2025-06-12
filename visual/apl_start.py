from tkinter import *
import bg

root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, 'Starting VIS\nPlease wait!!\n')
mainloop()

bg.start_game()