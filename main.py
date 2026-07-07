import pynput
import time
import rich
import tqdm

from core import click_and_point as clk
from pynput.keyboard import Controller
from core import directory as drr
from core import searcher as srch
from core import loop as lp
from rich.live import Live
from rich.text import Text
from rich import print
from tqdm import tqdm

kb = pynput.keyboard.Controller()
mouse_psx, mouse_psy = (969, 432)

try:
    print("Return to the browser within 8 seconds. The program will start in:")
    with Live(refresh_per_second=4) as live:
        for i in range(5, -1, -1):
            time.sleep(1)
            live.update(Text(f"Countdown: {i}s", style="green"))
            match i:
                case 0:
                    live.update(Text("Program Has Started", style="cyan blue"))
    
    # Link to Page
    srch.lksearcher('https://www.facebook.com/DABantayPresyoGitnangLuzon')
    time.sleep(10)
    clk.scroll(-4)
    
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

    print('[/green]Ran Successfully[/green]')
except KeyboardInterrupt:
    print('\n[green]User Cancelled. Proceeding to File Processing[/green]\n')
except:
    print('[bold red]Error Occured[/bold red]')

# Next is File Processing

if __name__ == '__main__':
    drr.directory()
    time.sleep(1)
    drr.cropper()

