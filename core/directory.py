import time
import os

from rich import print

from pathlib import Path
from tqdm import tqdm
from PIL import Image

box = (290,250,1100,1875)

provinces = ("aurora", "bataan", "bulacan", "nueva_ecija", "pampanga", "tarlac", "zambales")

home = Path.home()

download_dir = str(home) + "\\Downloads\\"

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
    cropper()
