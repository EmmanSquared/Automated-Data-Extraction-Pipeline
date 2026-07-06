import time
import pynput

from pynput.mouse import Button as bt
from pynput.keyboard import Key

kb = pynput.keyboard.Controller()
ms = pynput.mouse.Controller()

def searcher(input):
    search = str(input)
    time.sleep(3)
    kb.press('/')
    kb.release('/')
    kb.type(search)
    kb.press(Key.enter)
    kb.release(Key.enter)