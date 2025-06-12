import time
import os
from datetime import date

# vars
timenow = time.localtime()
current_time = time.strftime("%H:%M:%S", timenow)
today = date.today()

print("ENTER to start timer")
input()
while True:
    timenow = time.localtime()
    current_time = time.strftime("%H:%M:%S", timenow)
    today = date.today()
    print(current_time)
    print("Today's date:", today)

    time.sleep(1)
    os.system('clear')
    
    