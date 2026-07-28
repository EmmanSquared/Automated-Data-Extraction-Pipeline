import pynput
import time

from pynput.mouse import Button as bt
from pynput.keyboard import Key
from core import config

def pnt_clk(x,y): 
    config.ms.position = (x, y)
    time.sleep(2)
    config.ms.click(bt.left)

def scroll(num):
    config.ms.scroll(0,num)

if __name__ == '__main__':
    pnt_click(1,1)