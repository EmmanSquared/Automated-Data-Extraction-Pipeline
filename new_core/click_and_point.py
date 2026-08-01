import pynput
import time

from pynput.mouse import Button as bt
from pynput.keyboard import Key
from .config import *

class MouseController:
    def pnt_clk(x,y): 
        ms.position = (x, y)
        time.sleep(2)
        ms.click(bt.left)

    def scroll(num):
        ms.scroll(0,num)

if __name__ == '__main__':
    # MouseController.pnt_clk(1,1)

    yew = MouseController()
    yew.pnt_clk(250,250)