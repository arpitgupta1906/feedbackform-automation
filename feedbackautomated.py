from pynput.keyboard import Key,Controller
# from pynput.mouse import Controller as mousecontrol 
# from pynput.mouse import Button

from time import sleep

keyboard= Controller()
# m=mousecontrol()

keyboard.press(Key.alt)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.release(Key.alt)
sleep(0.50)

for i in range(7):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.50)       
# m.click(m.Button.left,count=1)

for i in range(18):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.50)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    
for i in range(5):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.050)
    keyboard.type('a')

    
for i in range(3):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.050)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    keyboard.press(Key.left)
    keyboard.release(Key.left)

keyboard.press(Key.enter)
keyboard.release(Key.enter)
