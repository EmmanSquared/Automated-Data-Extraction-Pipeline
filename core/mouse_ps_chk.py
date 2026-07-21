import pynput
import rich
import time

from core import config
from rich import print

def mschk():
    try:
        while True:
            time.sleep(1)
            print("[bold yellow]The Mouse Position is: [/bold yellow]" + str(config.ms.position) + " (Press Ctrl+C to Input)")
    except KeyboardInterrupt:
        print("[bold yellow]Tracking Ended[/bold yellow]")

if __name__ == '__main__':
    mschk()

