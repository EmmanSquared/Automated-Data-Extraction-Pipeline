import time
import pynput

from pynput.keyboard import Controller

kb = pynput.keyboard.Controller()


from core import searcher as srch
from core import click_and_point as clk
from core import loop as lp

mouse_psx, mouse_psy = (640, 252)

try:
    # Link to Page
    srch.lksearcher('https://www.facebook.com/DABantayPresyoGitnangLuzon')
    time.sleep(10)
    clk.scroll(-3)
    
    # Adjust to Price Post
    kb.press('j')
    kb.release('j')
    time.sleep(3)
    clk.scroll(-1)
    time.sleep(1)
    clk.pnt_clk(mouse_psx, mouse_psy)
    time.sleep(10)

    # Loop through Posts 
    lp.picture_scrape(mouse_psx,mouse_psy)

    print('Ran Successfully')
except:
    print('Error Occured')

# Next is File Processing

path = "/home/m/Downloads/filename.jpg"

