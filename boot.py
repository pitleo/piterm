# imports
import time
import os
import matplotlib
# varboots
longboot = False
whatsbroken= 'uitest is broken!'
name = "Piterm"
version = "Version 1.4"
time_edited = "June 10, 8:40 pm - 4:51 pm"
author = "pitleo"
apploader = 1
teversion = 1
shutdownver = 1
timever = 1
t1= "//::::::::::::::::::::::::::::::::::\\\\"
t2= "::                                  ::"
t3= f":: {name} {version} by {author}.  ::"
t4= f":: Edited: {time_edited}::"
# boot load
if longboot == False:
    print(whatsbroken)
    #time.sleep(2)
    print(f"{t1}\n{t2}\n{t3}    \n{t4}\n{t2}\n{t1}")
    print(f"{name} {version} by {author}")
    print(f"Last edited: {time_edited}")
    time.sleep(1.5)
if longboot == True:
    print(f"{name} {version} by {author}")
    print(f"Last edited: {time_edited}")
    time.sleep(1.5)
    print(f"Apploader Version: {apploader}")
    print(f"TE version: {teversion}")
    print(f"Shutdown version: {shutdownver}")
    print(f"Time version: {timever}")
    time.sleep(0.5)
