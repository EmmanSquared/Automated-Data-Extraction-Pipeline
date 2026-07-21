import pynput
import time

from pynput.mouse import Button as bt
from pynput.keyboard import Key
from core import config

def fbsearcher(input):
    search = str(input)
    time.sleep(3)
    config.kb.press('/')
    config.kb.release('/')
    time.sleep(1)
    config.kb.type(search)
    time.sleep(1)
    config.kb.press(Key.enter)
    config.kb.release(Key.enter)

def lksearcher(input):
    search = str(input)
    time.sleep(3)
    config.kb.press(Key.f6)
    config.kb.release(Key.f6)
    time.sleep(1)
    config.kb.type(search)
    time.sleep(1)
    config.kb.press(Key.enter)
    config.kb.release(Key.enter)

def kwsearcher(input):
    search = str(input)
    time.sleep(3)
    config.kb.press(Key.f3)
    config.kb.release(Key.f3)
    time.sleep(1)
    config.kb.type(search)
    time.sleep(1)
    config.kb.press(Key.enter)
    config.kb.release(Key.enter)