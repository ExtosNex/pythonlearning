#Clicking Thing

import threading as th
import pyautogui
import time

screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.    



#Breaking the loop. Click Enter my Broskis
moveby = 40
counter = 0
keep_going = True
def key_capture_thread():
    global keep_going
    input()
    keep_going = False

def do_stuff():
    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    while keep_going:
        global counter
        while counter < 3:
            print(pyautogui.position())
            pyautogui.move(0,moveby)
            pyautogui.click()
            counter += 1
            print("C = " + str(counter))
            time.sleep(0.1)
        while 3 <= counter < 6:
            print(pyautogui.position())
            pyautogui.move(0,-moveby)
            pyautogui.click()
            counter += 1
            print("C = " + str(counter))
            time.sleep(0.1)
        if counter == 6:
            counter = 0
do_stuff()

#pyautogui.move(0,100)
#pyautogui.click()
#pyautogui.write("abcdefghijklmnopqrstuvwxyz", interval=0.1)





