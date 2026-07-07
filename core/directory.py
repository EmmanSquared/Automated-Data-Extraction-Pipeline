import time
import os

# remove "from core" on mouse_ps_chk when testing on this file
from core import mouse_ps_chk as mschk
from pathlib import Path
from rich import print
from tqdm import tqdm
from PIL import Image

home = Path.home()

provinces = ("aurora", "bataan", "bulacan", "nueva_ecija", "pampanga", "tarlac", "zambales")
download_dir = str(home) + "\\Downloads\\"
box = (290,250,1100,1875)

def file_chk():
    while_state = True
    input_answer = 'n'
    def try_input():
        nonlocal input_answer
        nonlocal while_state
        try:
            input_answer = input('Response: ') or 'n'
            while_state = False

        except KeyboardInterrupt:
            print('[bold yellow]\nSelecting Default Response[/bold yellow]')
            input_answer = 'n'
            while_state = False

    def ps_input():
        try:
            mouse_psx = input("Input X Coordinate: ")
        except KeyboardInterrupt:
            print("[bold red]Invalid. Terminating Program [/bold red]")   
            exit()

        try:
            mouse_psy = input("Input Y Coordinate: ")
        except KeyboardInterrupt:
            print("[bold red]Invalid. Terminating Program [/bold red]")
            exit()
        
        with open("mouse_position.txt","w") as f:
            f.write("({},{})".format(mouse_psx,mouse_psy))
            print("[bold green]\nMouse Coordinate is Updated\n[/bold green]")
    
    def ms_calibrator():
        try:
            print('[bold green]\nStarting Calibrator[/bold green]')
            mschk.mschk()
        except KeyboardInterrupt:
            ps_input()
            

    if os.path.exists('mouse_position.txt'):
        with open('mouse_position.txt') as f:
            mouse_psx, mouse_psy = tuple(map(int,f.read().strip('()').split(',')))
        print('\nChange the Needed Mouse Position (Y/n)? (Default=n)')
        while while_state:
            try_input()

    else:
        print("[bold yellow]No File Found. Creating File.[/bold yellow]")
        time.sleep(.5)
        with open("mouse_position.txt","x") as f:
            ms_calibrator()

    if input_answer == 'Y':
        ms_calibrator()

# ============================

def directory():
    for x in tqdm(provinces):
        time.sleep(0.1)
        if os.path.isdir(download_dir + x) == False:
            os.mkdir(download_dir + x)
            tqdm.write(x.title() + ' directory was made.')
        else:
            tqdm.write(x.title() + ' path already exists.')

def cropper():
    for x in tqdm(range(14)):
        dir = str(home) + "\\Downloads" + f"\\{x}.jpg"
        try:
            im = Image.open(dir)
            region = im.crop(box)
            file = f"{x}.jpg"
        except:
            time.sleep(.08)
            print('[bold red]\n\nMissing:[/bold red]')
        match x:
            case 0:
                try:
                    region.save(download_dir + "aurora\\" + file)
                except:
                    print('[bold red]Part 1 of Aurora Price is not found.[/bold red]')
            case 1:
                try:
                    region.save(download_dir + "aurora\\" + file)
                    tqdm.write('Aurora is complete')
                except:
                    print('[bold red]Part 2 of Aurora Price is not found.[/bold red]')
            case 2:
                try:
                    region.save(download_dir + "bataan\\" + file )
                except:
                    print('[bold red]Part 1 of Bataan Price is not found.[/bold red]')
            case 3:
                try:
                    region.save(download_dir + "bataan\\" + file )
                    tqdm.write('Bataan is complete')
                except:
                    print('[bold red]Part 2 of Bataan Price is not found.[/bold red]')
            case 4:
                try:
                    region.save(download_dir + "bulacan\\" + file )
                except:
                    print('[bold red]Part 1 of Bulacan Price is not found.[/bold red]')
            case 5:
                try:
                    region.save(download_dir + "bulacan\\" + file )
                    tqdm.write('Bulacan is complete')
                except:
                    print('[bold red]Part 2 of Bulacan Price is not found.[/bold red]')
            case 6:
                try:
                    region.save(download_dir + "nueva_ecija\\" + file )
                except:
                    print('[bold red]Part 1 of Nueva Ecija Price is not found.[/bold red]')
            case 7:
                try:
                    region.save(download_dir + "nueva_ecija\\" + file )
                    tqdm.write('Nueva Ecija is complete')
                except:
                    print('[bold red]Part 1 of Nueva Ecija Price is not found.[/bold red]')
            case 8:
                try:
                    region.save(download_dir + "pampanga\\" + file )
                except:
                    print('[bold red]Part 1 of Pampanga Price is not found.[/bold red]')
            case 9:
                try:
                    region.save(download_dir + "pampanga\\" + file )
                    tqdm.write('Pampanga is complete')
                except:
                    print('[bold red]Part 2 of Pampanga Price is not found.[/bold red]')
            case 10:
                try:
                    region.save(download_dir + "tarlac\\" + file )
                except:
                    print('[bold red]Part 1 of Tarlac Price is not found.[/bold red]')
            case 11:
                try:
                    region.save(download_dir + "tarlac\\" + file )
                    tqdm.write('Tarlac is complete')
                except:
                    print('[bold red]Part 2 of Tarlac Price is not found.[/bold red]')
            case 12:
                try:
                    region.save(download_dir + "zambales\\" + file )
                except:
                    print('[bold red]Part 1 of Zambales Price is not found.[/bold red]')
            case 13:
                try:
                    region.save(download_dir + "zambales\\" + file )
                    tqdm.write('Zambales is complete')
                except:
                    print('[bold red]Part 2 of Zambales Price is not found.[/bold red]')
        # case 14:
        #     region.save(download_dir + "Regional\\" + f"{x}.jpg" )
        # case 15:
        #     region.save(download_dir + "Regional\\" + f"{x}.jpg" )
        # case 16:
        #     region.save(download_dir + "DPI\\" + f"{x}.jpg" )  
        # case 17:
        #     region.save(download_dir + "DPI\\" + f"{x}.jpg" ) 

if __name__ == '__main__':
    file_chk()
