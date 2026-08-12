import pandas as pd
import os

# from . 
import config
from tqdm import tqdm
from time import sleep

class Formatter:
    def __init__(self):
        for x in tqdm(range(0,14,2)):
            print("Formatting: ", config.provinces[x].title())
            df = pd.read_csv(os.path.join(config.download_dir,'bantay_presyo',config.provinces[x],f"{config.provinces[x]}.csv"),sep=';')
            df1 = df.iloc[:,:7]
            df1.columns = ['Category','Item','Unit','Low','High','Average','Current']
            df1.to_csv(os.path.join(config.download_dir,'bantay_presyo',config.provinces[x],f"{config.provinces[x]}.csv"),index=False,index_label=False)


if __name__ == '__main__':
    i_range = tqdm(range(0,14,2), leave=False)
    for x in i_range:
        print("\nFormatting: ", config.provinces[x].title())
        i_range.clear()
        sleep(.1)
        # os.system('cls' if os.name == 'nt' else 'clear')


    