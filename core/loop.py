import time
import pynput

from pynput.mouse import Button as bt
from pynput.keyboard import Key

kb = pynput.keyboard.Controller()
ms = pynput.mouse.Controller()

def picture_scrape(x,y):
    for x in range(13):
        ms.click(bt.right)
        time.sleep(1.3)
        ms.move(50,50)
        time.sleep (1.3)

        ms.click(bt.left)
        time.sleep(8)
        kb.type(f'{x}')
        time.sleep(1)
        kb.press(Key.enter)
        kb.release(Key.enter)
        time.sleep(2)
        kb.press(Key.right)
        kb.release(Key.right)
        time.sleep(3)
        ms.move(-50, -50)
        time.sleep(1)