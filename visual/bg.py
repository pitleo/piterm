import pygame
import tkinter as tk
import os
from visual import apl_errors
from tkinter import *


# Open Apps
 


def startvis():
    print("Starting VISUAL")
    os.system("python3 visual/apl_start.py")
    
    
def notepad_command():
    try:
        os.system("python3 visual/app_notepad.py")
    except:
        apl_errors.errorbad
    
def hello_command():
    os.system("python3 visual/app_graph.py")

def about_command():
    os.system("python3 visual/app_about.py")

def exit_command():
    root.destroy()

def test_command():
    os.system("python3 visual/app_test.py")

def calc_command():
    os.system("python3 visual/app_calculator.py")

def vinc_command():
    os.system("python3 visual/app_varincrease.py")
    
def snake_command():
    os.system("python3 visual/app_snakegame.py")
    
def abit_command():
    os.system("python3 visual/app_8bit.py")
    
def turtle_command():
    os.system("python3 visual/app_turtle.py")
    
def bubble_info():
    print("NO YOURE A FUNCTION UNDEFINED")
    
def web_command():
    os.system("python3 visual/app_web.py")
    
def playsound_pop():
    # initialize tk object to use tksnack
    root = Tk()
    tkSnack.initializeSnack(root)

    # play sound
    snd = tkSnack.Sound()
    snd.read('note.wav')
    print('playing sound using tkSnack')
    snd.play(blocking=1)

# Start Menu

def start_game():
    root = tk.Tk()
    root.title('Start')
    root.geometry("800x600")
    root.wm_attributes('-type', 'splash')
    root.configure(background='blue')
    small_icon = tk.PhotoImage(file="visual/img/1-16-16.png")
    large_icon = tk.PhotoImage(file="visual/img/1.png")
    root.iconphoto(False, large_icon, small_icon)

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    
    file_menu.add_command(label="New File", command=notepad_command)
    file_menu.add_command(label="About", command=about_command)
    file_menu.add_command(label="Settings", command=test_command)
    file_menu.add_command(label="Exit", command=root.destroy)
    
    
    file_menu1 = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Games", menu=file_menu1)
    file_menu1.add_command(label="Snake", command=snake_command)
    file_menu1.add_command(label="Turtle", command=turtle_command)
    
    file_menu2 = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Utils", menu=file_menu2)
    file_menu2.add_command(label="Calculator", command=calc_command)
    file_menu2.add_command(label="Notepad", command=notepad_command)
    file_menu2.add_command(label="Browser", command=web_command)
    
    root.mainloop()



    
# Desktop BG

#def bg_color():
    (width, height) = (800, 600)
    screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    pygame.display.set_caption('')
    background_colour = (0,0,255)
    screen.fill(background_colour)
    pygame.display.flip()

