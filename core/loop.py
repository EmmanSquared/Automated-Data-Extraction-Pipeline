import pynput
import time

from pynput.mouse import Button as bt
from pynput.keyboard import Key
from core import config

def picture_scrape(x,y):
    for x in range(14):
        config.ms.click(bt.right)
        time.sleep(1.3)
        config.ms.move(50,50)
        time.sleep (1.3)

        config.ms.click(bt.left)
        time.sleep(8)
        config.kb.type(f'{x}')
        time.sleep(1)
        config.kb.press(Key.enter)
        config.kb.release(Key.enter)
        time.sleep(2)
        config.kb.press(Key.right)
        config.kb.release(Key.right)
        time.sleep(3)
        config.ms.move(-50, -50)
        time.sleep(1)