# introduction  | author: Divit
"""
- 
"""

# libraries
import pyautogui
import time

# get time to get to the textbox
time.sleep(10)

# select the spam word
spam_word = "sussy baka rizzing up skibidi ohio giga chad which got fanux taxed by lvl 100 gyatt"

# printing
for i in range(10):  # replace with while loop
    pyautogui.typewrite(spam_word.replace(" ", "_"))
    pyautogui.press("enter")
