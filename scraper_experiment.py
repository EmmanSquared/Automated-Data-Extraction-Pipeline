import time
import pynput

from core import fbsearcher as srch
from pynput.mouse import Button as bt
from pynput.keyboard import Key

kb = pynput.keyboard.Controller()
ms = pynput.mouse.Controller()

mouse_psx, mouse_psy = (956, 277)

try:
    srch.searcher('bantay presyo ng gitnang luzon')

    time.sleep(10)

    ms.position = (mouse_psx, mouse_psy)
    ms.click(bt.left)

    time.sleep(5)

    ms.scroll(0,-6) #-6 or -8 depending if its the first time to be opened

    time.sleep(5)

    ms.click(bt.left)

    time.sleep (5)


    # loop through the posts
    for x in range(18):
        ms.click(bt.right)

        time.sleep(2)
        ms.move(50,50)

        time.sleep (1)

        ms.click(bt.left)
        time.sleep(4)
        kb.type(f'{x}')
        kb.press(Key.enter)
        kb.release(Key.enter)
        time.sleep(2)
        kb.press(Key.right)
        kb.release(Key.right)
        ms.position = (956, 277)
        time.sleep(1)

    print('Ran Successfully')
except:
    print('Error Occured')

# Next is File Processing

path = "/home/m/Downloads/filename.jpg"

