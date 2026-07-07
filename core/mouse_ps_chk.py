import pynput
import rich
import time

from pynput.mouse import Button, Controller    
from rich import print

ms = Controller()

def mschk():
    while True:
        time.sleep(1)
        print("[bold yellow]The Mouse Position is: [/bold yellow]" + str(ms.position) + " (Press Ctrl+C to Input)")

if __name__ == '__main__':
    mschk()

