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
    sleep(0.050)       

for i in range(2):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.050)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    
for i in range(1):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.050)
    keyboard.type('a')

keyboard.press(Key.tab)
keyboard.release(Key.tab)

keyboard.press(Key.enter)
keyboard.release(Key.enter)