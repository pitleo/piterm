# imports
import os
import subprocess
import time
import time
import urllib
import json
import sys
import matplotlib
import errors
# vars
cursorSprites = ['A:', ':3>', '[>]']
#with open('save.json', 'r') as file:
    #data = json.load(file)
    #prompt = cursorSprites[data['cursor'] - 1]
prompt = "A:"
cmavl = 3
timenow = time.localtime()
current_time = time.strftime("%H:%M:%S", timenow)
secret_message = ':3>'
cursors = ['1: Normal','2: Cat','3: Minimalist']
# terminal itself
while True:
    inp = input(prompt)
    if inp == 'help':
        print(f"There are {cmavl} commands!")
        print("Type 1 for normal HELP, 2 for interactive.")
        inhelp = input(prompt)
        if inhelp == '1':
            print("help, exit, apl, time, timeloop, cursor")
        if inhelp == '2':
            print("Enter in format: command")
            inhelpa = input(prompt)
            if inhelpa == 'help':
                print("Shows all commands, and interactive help")
            if inhelpa == 'exit':
                print("Shuts the system down.")
            if inhelpa == 'time':
                print("Prints your time")
            if inhelpa == 'time{loop}':
                print("Prints the time and date at a constant.")
            if inhelpa == 'custom':
                print("Customize things about the terminal")
                
    if inp == 'exit':
        import shutdown
        break
    if inp == 'vis':
        try:
            import apl
        except:
            print(errors.errorFH())
    if inp == 'time':
        timenow = time.localtime()
        current_time = time.strftime("%H:%M:%S", timenow)
        print(current_time)
    if inp == 'timeloop':
        import clock
    if inp == 'blog':
        def open():
            return urllib.urlopen('https://piterminal.blogspot.com/')
    if inp == 'custom':
        print("What do you want to set the cursor to?")
        print(cursors)
        al = input(prompt)
        if al == '1':
            prompt = 'A:'
        if al == '2':
            prompt = secret_message
        if al == '3':
            prompt = '[>]'
        #with open("save.json", 'w') as file:
            #file.truncate(0)
            #data['cursor'] = int(al)
            #json.dump(data, file, indent = 4)
            #file.close()
        #sys.exit(0)
