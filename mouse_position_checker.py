import time
import pynput

from pynput.mouse import Button, Controller    

ms = Controller()

while True:
    time.sleep(2)
    print(ms.position)