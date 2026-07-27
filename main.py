import pynput
import rich
import time
import tqdm
import os

from core import initial_check as i_chk
from core import click_and_point as clk
from pynput.keyboard import Controller
from core import langchain_pipeline as pipe
from core import directory as drr
from core import searcher as srch
from core import scraper as scrape
from rich.live import Live
from rich.text import Text
from core import config
from rich import print
from tqdm import tqdm

# Start of the program

i_chk.browser_chk()

try:
    print("Return to the browser within 8 seconds. The program will start in:")
    with Live(refresh_per_second=4) as live:
        for i in range(5, -1, -1):
            time.sleep(1)
            live.update(Text(f"Countdown: {i}s", style="green"))
            match i:
                case 0:
                    live.update(Text("Program Has Started", style="cyan blue"))
    
    # Linker to Page
    srch.lksearcher(config.link_of_interest)
    time.sleep(10)
    clk.scroll(-4)
    
    # Adjust to Price Post
    config.kb.press('j')
    config.kb.release('j')
    time.sleep(3)
    clk.scroll(-1)
    time.sleep(1)
    clk.pnt_clk(config.mouse_psx, config.mouse_psy)
    time.sleep(10)

    # Loop through Posts 
    clk.pnt_clk(config.screen_psx,config.screen_psy)
    scrape.picture_scrape()

    print('[green]Ran Successfully[/green]')
except KeyboardInterrupt:
    print('\n[green]User Cancelled. Proceeding to File Processing[/green]\n')
except:
    print('[bold red]Error Occured[/bold red]')

# File Processing

try:
    drr.directory()
    time.sleep(1)
    drr.cropper()
    pipe.image_to_csv_pipeline()

except:
    print('[bold red]Error Occured[/bold red] either on Files, Cropper, AI Pipeline')

