import pynput
import rich
import time
import tqdm
import os

from core import initial_check as i_chk
from core import click_and_point as clk
from core import mouse_ps_chk as mschk
from pynput.keyboard import Controller
from core import langchain_pipeline as pipe
from core import directory as drr
from core import searcher as srch
from core import loop as lp
from rich.live import Live
from rich.text import Text
from core import config
from rich import print
from tqdm import tqdm

# Start of the program

if __name__ == '__main__':
    i_chk.browser_chk()
    drr.file_chk()

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
        config.kb.press('j')
        config.kb.release('j')
        time.sleep(3)
        clk.scroll(-1)
        time.sleep(1)
        clk.pnt_clk(config.mouse_psx, config.mouse_psy)
        time.sleep(10)

        # Loop through Posts 
        lp.picture_scrape(config.mouse_psx,config.mouse_psy)

        print('[/green]Ran Successfully[/green]')
    except KeyboardInterrupt:
        print('\n[green]User Cancelled. Proceeding to File Processing[/green]\n')
    except:
        print('[bold red]Error Occured[/bold red]')

# Next is File Processing


    try:
        drr.directory()
        time.sleep(1)
        drr.cropper()
        pipe.image_to_csv_pipeline()

    except:
        print('error occured')
