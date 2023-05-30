import keyboard
import pyautogui
from time import sleep

def Opener(Name):
    sleep(0.5)
    pyautogui.press('win')
    sleep(0.5)
    keyboard.write(Name)
    sleep(0.5)
    keyboard.press('enter')
    sleep(0.5)
