from pynput.keyboard import Key,Controller
from time import sleep

keyboard= Controller()


keyboard.press(Key.alt)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.release(Key.alt)
sleep(0.50)

for i in range(7):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.10)       

for i in range(18):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.10)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    
for i in range(5):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.10)
    keyboard.type('a')

    
for i in range(3):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.10)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    keyboard.press(Key.left)
    keyboard.release(Key.left)

keyboard.press(Key.enter)
keyboard.release(Key.enter)
