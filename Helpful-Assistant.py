from pynput.keyboard import Key, Controller
from pynput.keyboard import Key, Listener
import time
import keyboard

keyboard = Controller()

#keyboard.press('a')
#keyboard.release('a')
#run = True

def exit_command(key):
    print('Exit command detected')
    if key == Key.esc:
        return False


with Listener(on_press=exit_command) as listener:
    listener.join()




# def f1_loop():
#     while True:
#         keyboard.press(Key.f1)
#         keyboard.release(Key.f1)
#         time.sleep(5)
