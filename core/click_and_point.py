import time
import pynput

from pynput.mouse import Button as bt
from pynput.keyboard import Key

kb = pynput.keyboard.Controller()
ms = pynput.mouse.Controller()

def pnt_clk(x,y):
    ms.position = (x, y)
    time.sleep(2)
    ms.click(bt.left)

def scroll(num):
    ms.scroll(0,num)