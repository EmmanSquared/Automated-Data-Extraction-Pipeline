import time
import sys
import os

from core import config
from rich import print
from tqdm import tqdm
from PIL import Image

class file_state:
    def __init__(self):
        self.while_state = True
        self.input_answer = 'n'

    def try_input(self):
        try:
            self.input_answer = input('Response: ') or 'n'
            self.while_state = False

        except KeyboardInterrupt:
            print('[bold yellow]\nSelecting Default Response[/bold yellow]')
            self.input_answer = 'n'
            self.while_state = False

    def ps_input(self):
        try:
            config.mouse_psx = input("Input X Coordinate: ")
        except KeyboardInterrupt:
            print("[bold red]Invalid. Terminating Program [/bold red]")   
            sys.exit()

        try:
            config.mouse_psy = input("Input Y Coordinate: ")
        except KeyboardInterrupt:
            print("[bold red]Invalid. Terminating Program [/bold red]")
            sys.exit()
        
        with open("mouse_position.txt","w") as f:
            f.write("({},{})".format(config.mouse_psx,config.mouse_psy))
            print("[bold green]\nMouse Coordinate is Updated\n[/bold green]")

    def mschk(self):
        try:
            while True:
                time.sleep(1)
                print("[bold yellow]The Mouse Position is: [/bold yellow]" + str(config.ms.position) + " (Press Ctrl+C to Input)")
        except KeyboardInterrupt:
            print("[bold yellow]Tracking Ended[/bold yellow]")
            self.ps_input()

    def ms_calibrator(self):
        try:
            print('[bold green]\nStarting Calibrator[/bold green]')
            self.mschk()
        except KeyboardInterrupt:
            print("[bold red]tester[/bold red]")
            self.ps_input()


def file_chk():
    mouse_file_state = file_state()

    if os.path.exists('mouse_position.txt'):
        with open('mouse_position.txt') as f:
            config.mouse_psx, config.mouse_psy = tuple(map(int,f.read().strip('()').split(',')))
        print('\nChange the Needed Mouse Position (Y/n)? (Default=n)')
        while mouse_file_state.while_state:
            mouse_file_state.try_input()

    else:
        print("[bold yellow]No File Found. Creating File.[/bold yellow]")
        time.sleep(.5)
        with open("mouse_position.txt","x") as f:
            mouse_file_state.ms_calibrator()

    if mouse_file_state.input_answer == 'Y':
        mouse_file_state.ms_calibrator()
        
    # while_state = True
    # input_answer = 'n'
    # def try_input():
    #     nonlocal input_answer
    #     nonlocal while_state
    #     try:
    #         input_answer = input('Response: ') or 'n'
    #         while_state = False

    #     except KeyboardInterrupt:
    #         print('[bold yellow]\nSelecting Default Response[/bold yellow]')
    #         input_answer = 'n'
    #         while_state = False

    # def ps_input():
    #     try:
    #         mouse_psx = input("Input X Coordinate: ")
    #     except KeyboardInterrupt:
    #         print("[bold red]Invalid. Terminating Program [/bold red]")   
    #         exit()

    #     try:
    #         mouse_psy = input("Input Y Coordinate: ")
    #     except KeyboardInterrupt:
    #         print("[bold red]Invalid. Terminating Program [/bold red]")
    #         exit()
        
    #     with open("mouse_position.txt","w") as f:
    #         f.write("({},{})".format(mouse_psx,mouse_psy))
    #         print("[bold green]\nMouse Coordinate is Updated\n[/bold green]")
    
    # def ms_calibrator():
    #     try:
    #         print('[bold green]\nStarting Calibrator[/bold green]')
    #         mschk.mschk()
    #     except KeyboardInterrupt:
    #         ps_input()
            


# ============================

def directory():
    for x in tqdm(config.provinces):
        print(x)
        if config.provinces.index(x) % 2 == 0:
            time.sleep(0.1)
            if os.path.isdir(config.bantay_presyo) == False:
                os.mkdir(config.bantay_presyo)
                tqdm.write('Bantay Presyo directory was made.')
            if os.path.isdir(os.path.join(config.bantay_presyo,x)) == False:
                os.mkdir(os.path.join(config.bantay_presyo,x))
                tqdm.write(x.title() + ' directory was made.')
            else:
                tqdm.write(x.title() + ' path already exists.')

def cropper():
    for x in tqdm(range(14)):
        dir = os.path.join(config.download_dir, f"{x}.jpg")
        try:
            im = Image.open(dir)
            region = im.crop(config.box)
            file = f"{x}.jpg"   
        except:
            time.sleep(.08)
            print('[bold red]\n\nMissing:[/bold red]')
        match x:
            case 0:
                try:
                    region.save(os.path.join(config.bantay_presyo, config.provinces[x], file))
                except:
                    print('[bold red]Part 1 of Aurora Price is not found.[/bold red]')
            case 1:
                try:
                    region.save(os.path.join(config.bantay_presyo,config.provinces[x],file))
                    tqdm.write('Aurora is complete')
                except:
                    print('[bold red]Part 2 of Aurora Price is not found.[/bold red]')
            case 2:
                try:
                    region.save(os.path.join(config.bantay_presyo,config.provinces[x],file))
                except:
                    print('[bold red]Part 1 of Bataan Price is not found.[/bold red]')
            case 3:
                try:
                    region.save(os.path.join(config.bantay_presyo,config.provinces[x],file))
                    tqdm.write('Bataan is complete')
                except:
                    print('[bold red]Part 2 of Bataan Price is not found.[/bold red]')
            case 4:
                try:
                    region.save(os.path.join(config.bantay_presyo,config.provinces[x],file))
                except:
                    print('[bold red]Part 1 of Bulacan Price is not found.[/bold red]')
            case 5:
                try:
                    region.save(os.path.join(config.bantay_presyo,config.provinces[x],file))
                    tqdm.write('Bulacan is complete')
                except:
                    print('[bold red]Part 2 of Bulacan Price is not found.[/bold red]')
            case 6:
                try:
                    region.save(os.path.join(config.bantay_presyo,config.provinces[x],file))
                except:
                    print('[bold red]Part 1 of Nueva Ecija Price is not found.[/bold red]')
            case 7:
                try:
                    region.save(os.path.join(config.bantay_presyo,config.provinces[x],file))
                    tqdm.write('Nueva Ecija is complete')
                except:
                    print('[bold red]Part 1 of Nueva Ecija Price is not found.[/bold red]')
            case 8:
                try:
                    region.save(os.path.join(config.bantay_presyo,config.provinces[x],file))
                except:
                    print('[bold red]Part 1 of Pampanga Price is not found.[/bold red]')
            case 9:
                try:
                    region.save(os.path.join(config.bantay_presyo,config.provinces[x],file))
                    tqdm.write('Pampanga is complete')
                except:
                    print('[bold red]Part 2 of Pampanga Price is not found.[/bold red]')
            case 10:
                try:
                    region.save(os.path.join(config.bantay_presyo,config.provinces[x],file))
                except:
                    print('[bold red]Part 1 of Tarlac Price is not found.[/bold red]')
            case 11:
                try:
                    region.save(os.path.join(config.bantay_presyo,config.provinces[x],file))
                    tqdm.write('Tarlac is complete')
                except:
                    print('[bold red]Part 2 of Tarlac Price is not found.[/bold red]')
            case 12:
                try:
                    region.save(os.path.join(config.bantay_presyo,config.provinces[x],file))
                except:
                    print('[bold red]Part 1 of Zambales Price is not found.[/bold red]')
            case 13:
                try:
                    region.save(os.path.join(config.bantay_presyo,config.provinces[x],file))
                    tqdm.write('Zambales is complete')
                except:
                    print('[bold red]Part 2 of Zambales Price is not found.[/bold red]')
        # os.remove(dir)

if __name__ == '__main__':
    
    cropper()
