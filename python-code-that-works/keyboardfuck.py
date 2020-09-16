import pyautogui
import time

time.sleep(3)

while True:
	pyautogui.write("FUCK",interval=0.05)
	pyautogui.press("enter")
	pyautogui.move(1000,0)
	pyautogui.click()
	pyautogui.write("FUCK",interval=0.05)
	pyautogui.press("enter")
	pyautogui.move(-1000,0)
	pyautogui.click()
