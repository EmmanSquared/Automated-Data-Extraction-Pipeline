import os
import time

from pathlib import Path
from PIL import Image

box = (290,250,1100,1875)

provinces = ("aurora", "bataan", "bulacan", "nueva_ecija", "pampanga", "tarlac", "zambales")

home = Path.home()

download_dir = str(home) + "\\Downloads\\"

for x in provinces:
    os.mkdir(download_dir + x)

time.sleep(5)


for x in range(13):
    dir = str(home) + "\\Downloads" + f"\\{x}.jpg"
    im = Image.open(dir)
    region = im.crop(box)
    file = f"{x}.jpg"
    match x:
        case 0:
            region.save(download_dir + "Aurora\\" + file)
        case 1:
            region.save(download_dir + "Aurora\\" + file)
        case 2:
            region.save(download_dir + "Bataan\\" + f"{x}.jpg" )
        case 3:
            region.save(download_dir + "Bataan\\" + f"{x}.jpg" )
        case 4:
            region.save(download_dir + "Bulacan\\" + f"{x}.jpg" )
        case 5:
            region.save(download_dir + "Bulacan\\" + f"{x}.jpg" )
        case 6:
            region.save(download_dir + "Nueva Ecija\\" + f"{x}.jpg" )
        case 7:
            region.save(download_dir + "Nueva Ecija\\" + f"{x}.jpg" )
        case 8:
            region.save(download_dir + "Pampanga\\" + f"{x}.jpg" )
        case 9:
            region.save(download_dir + "Pampanga\\" + f"{x}.jpg" )
        case 10:
            region.save(download_dir + "Tarlac\\" + f"{x}.jpg" )
        case 11:
            region.save(download_dir + "Tarlac\\" + f"{x}.jpg" )
        case 12:
            region.save(download_dir + "Zambales\\" + f"{x}.jpg" )
        case 13:
            region.save(download_dir + "Zambales\\" + f"{x}.jpg" )
        # case 14:
        #     region.save(download_dir + "Regional\\" + f"{x}.jpg" )
        # case 15:
        #     region.save(download_dir + "Regional\\" + f"{x}.jpg" )
        # case 16:
        #     region.save(download_dir + "DPI\\" + f"{x}.jpg" )  
        # case 17:
        #     region.save(download_dir + "DPI\\" + f"{x}.jpg" ) 


# region.save()
# region.save("cropped.jpg")