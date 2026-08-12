import shutil
import os

from rich import print
from . import config

class Zipper:
    def zipper(self):
        print('[green]Zipping Started[/green]')
        shutil.make_archive(
        base_name=config.bantay_presyo,
        format='zip',
        root_dir=config.bantay_presyo
        )
        if os.path.exists(config.zip_bp):
            print('[green]The program outputted a ZIP file. You may proceed to uploading.[/green]')
            sys.exit() 

    def __init__(self):
        self.zipper()