#program data
'''
Title: Logreader
Version: 1.1
Author: pitleo
Comment: hi! im pretty proud of this :D
'''
#imports
import os
#vars
title = 'Logreader'
version = 1.1
author = 'pitleo'
path = "/home"
dir_list = os.listdir(path)
cwd = os.getcwd()
prompt = '>>'
border = "==============="
#program
print(f"{title} {version} by {author}")
print("type in the filename")
while True:
    a = input(">>")
    if a == 'ls':
        print(cwd)
        print(dir_list)
    try:
        f = open(a)
        os.system('clear')
        print(f.read())
    except:
        print(border)