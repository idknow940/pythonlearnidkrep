import pyautogui
import time

text = open('rickroll.txt', 'r')

time.sleep(3)
for i in text:
    pyautogui.typewrite(i)
    pyautogui.press('enter')