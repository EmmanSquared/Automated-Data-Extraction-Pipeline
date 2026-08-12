import time
import sys
import os

from rich import print
from tqdm import tqdm
from PIL import Image
from . import config

class Directory:
    def directory(self):
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

    def cropper(self):
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
            # Removed for now as a failsafe for iterating through posts so you can pick up where it went off.
            # os.remove(dir)

# if __name__ == '__main__':
    
#     cropper()
