import pynput
import time

from pynput.mouse import Button as bt
from pynput.mouse import Controller
from pynput.keyboard import Key
from core import config

def picture_scrape():
    for x in range(14):
        config.ms.click(bt.right)
        time.sleep(1.3)
        config.ms.move(50,50)
        time.sleep (1.3)

        config.ms.click(bt.left)
        time.sleep(8)
        config.kb.type(f'{x}')
        time.sleep(1)
        config.kb.press(Key.f4)
        config.kb.release(Key.f4)
        time.sleep(1)
        config.kb.press(Key.ctrl_l)
        config.kb.press('a')
        config.kb.release(Key.ctrl_l)
        config.kb.release('a')
        time.sleep(1)
        config.kb.type(config.download_dir)
        time.sleep(1)
        config.kb.press(Key.enter)
        config.kb.release(Key.enter)
        time.sleep(1)
        config.kb.press(Key.enter)
        config.kb.release(Key.enter)
        time.sleep(1)
        config.kb.press(Key.enter)
        config.kb.release(Key.enter)
        time.sleep(1)
        config.kb.press(Key.enter)
        config.kb.release(Key.enter)
        time.sleep(2)
        config.kb.press(Key.right)
        config.kb.release(Key.right)
        time.sleep(3)
        config.ms.move(-50, -50)
        time.sleep(1)

if __name__ == '__main__':
    time.sleep(2)
    # config.kb.press(Key.f4)
    # config.kb.release(Key.f4)
    # time.sleep(2)
    # config.kb.press(Key.ctrl_l)
    # config.kb.press('a')
    # config.kb.release(Key.ctrl_l)
    # config.kb.release('a')
    # ms = Controller()
    # ms.position = (config.screen_psx,config.screen_psy)
    picture_scrape()