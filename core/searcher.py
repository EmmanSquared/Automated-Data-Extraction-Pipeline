import time
import pynput

from pynput.mouse import Button as bt
from pynput.keyboard import Key

kb = pynput.keyboard.Controller()
ms = pynput.mouse.Controller()

def fbsearcher(input):
    search = str(input)
    time.sleep(3)
    kb.press('/')
    kb.release('/')
    time.sleep(1)
    kb.type(search)
    time.sleep(1)
    kb.press(Key.enter)
    kb.release(Key.enter)

def lksearcher(input):
    search = str(input)
    time.sleep(3)
    kb.press(Key.f6)
    kb.release(Key.f6)
    time.sleep(1)
    kb.type(search)
    time.sleep(1)
    kb.press(Key.enter)
    kb.release(Key.enter)

def kwsearcher(input):
    search = str(input)
    time.sleep(3)
    kb.press(Key.f3)
    kb.release(Key.f3)
    time.sleep(1)
    kb.type(search)
    time.sleep(1)
    kb.press(Key.enter)
    kb.release(Key.enter)