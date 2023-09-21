import time
import threading
import pyautogui
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode



TOGGLE_KEY = KeyCode(char="t")

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            x, y = pyautogui.position()
            print('Primeiro -> x: ',x,'y: ',y)
            mouse.click(Button.left, 1)
            time.sleep(0.5)
            pyautogui.moveTo(960,1016)
            print('Segundo -> x: ',x,'y: ',y)
            time.sleep(1)
            mouse.click(Button.left, 1)
            time.sleep(0.5)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

clicking_thread = threading.Thread(target=clicker)
clicking_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()