from pynput.keyboard import Key, Controller
import time
import keyboard
keyboard = Controller()

while True:
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    time.sleep(5)