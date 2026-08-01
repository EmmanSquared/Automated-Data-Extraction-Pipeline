import time

from rich.live import Live
from rich.text import Text
from rich import print
from tqdm import tqdm

class Loading:
    def timer(self):
        print("Return to the browser within 8 seconds. The program will start in:")
        with Live(refresh_per_second=4) as live:
            for i in range(5, -1, -1):
                time.sleep(1)
                live.update(Text(f"Countdown: {i}s", style="green"))
                match i:
                    case 0:
                        live.update(Text("Program Has Started", style="cyan blue"))
    
    def __init__(self):
        self.timer()