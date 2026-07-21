import os

from ollama import chat
from core import config

def image_to_csv_pipeline():
    for x in tqdm(range(0,15,2)):
        image_to_pass = []
        image_to_pass.append(os.path.join(config.home,'Downloads',config.provinces[x],f"{x}.jpg"))
        image_to_pass.append(os.path.join(config.home,'Downloads',config.provinces[x],f"{x+1}.jpg"))

        response = chat(
            model='minimax-m3:cloud',
            messages=[{'role':'assistant', 'content': config.system_prompt},
            {'role': 'user', 'content': config.prompt, 'images': image_to_pass }],
        )

        try:
            with open (f"{config.provinces[x]}.csv","w") as csv_file:
                os.path.join(config.home,"Downloads",config.provinces[x],csv_file.write(response.message.content))
                tqdm.write(str(config.provinces[x] + " CSV is now Complete"))

        except:
            print(str(config.provinces[x]) + ' part had a problem')


