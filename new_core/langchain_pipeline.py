import pandas as pd
import shutil
import base64
import tqdm
import time
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage
from google import genai
from ollama import chat
from tqdm import tqdm
from .config import *

class AIPipeline:
    def image_to_csv_pipeline(self):
        try:
            for x in tqdm(range(0,14,2)):
                tqdm.write(str(config.provinces[x].title() + ' CSV is now being processed.\n'))
                image_to_pass = []
                image_to_pass.append(os.path.join(config.download_dir,'bantay_presyo',config.provinces[x],f"{x}.jpg"))
                image_to_pass.append(os.path.join(config.download_dir,'bantay_presyo',config.provinces[x],f"{x+1}.jpg"))

                response = chat(
                    model=config.ai_model,
                    messages=[{'role':'assistant', 'content': config.system_prompt},
                    {'role': 'user', 'content': config.prompt, 'images': image_to_pass }],
                )

                try:
                    with open (os.path.join(config.download_dir,'bantay_presyo',config.provinces[x],f"{config.provinces[x]}.csv"),"w") as csv_file:
                        csv_file.write(response.message.content)
                        tqdm.write(str(config.provinces[x].title() + " CSV is now Complete.\n"))

                    df = pd.read_csv(os.path.join(config.download_dir,'bantay_presyo',config.provinces[x],f"{config.provinces[x]}.csv"),sep=';')
                    df.to_csv(os.path.join(config.download_dir,'bantay_presyo',config.provinces[x],f"{config.provinces[x]}.csv"),index=False,index_label=False)

                except:
                    print(str(config.provinces[x]) + ' part had a problem\n')

        except:
            print('[blue cyan]Ollama[/blue cyan] is Not Available. Switching to [bold yellow3]Gemini[/bold yellow3]')

            llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash",api_key=config.apiKey)

            for x in tqdm(range(0,14,2)):
                tqdm.write(str(config.provinces[x].title() + ' CSV is now being processed.'))
                first_image = os.path.join(config.download_dir,'bantay_presyo',config.provinces[x],f"{x}.jpg")
                second_image = os.path.join(config.download_dir,'bantay_presyo',config.provinces[x],f"{x+1}.jpg")

                with open(first_image, "rb") as image_file:
                    first_encoded = base64.b64encode(image_file.read()).decode('utf-8')
                with open(second_image, "rb") as image_file:
                    second_encoded = base64.b64encode(image_file.read()).decode('utf-8')
                
                message_local = HumanMessage(
                    content=[
                        {"type": "text", "text": config.prompt},
                        {"type": "image_url", "image_url": f"data:image/png;base64,{first_encoded}"},
                        {"type": "image_url", "image_url": f"data:image/png;base64,{second_encoded}"}
                    ]
                )
                
                result_local = llm.invoke([message_local])

                try:
                    with open (os.path.join(config.download_dir,'bantay_presyo',f"{config.provinces[x]}.csv"),"w") as csv_file:
                        csv_file.write(result_local.text)
                        tqdm.write(str(config.provinces[x].title() + " CSV is now Complete.\n"))


                except:
                    print(str(config.provinces[x].title()) + ' part had a problem\n')
            
            shutil.make_archive(
                config.bantay_presyo,
                'zip',
                config.download_dir
            )

            if os.path.exists(config.zip_bp):
                print('The program outputted a ZIP file. You may proceed to inputting.')
                sys.exit()

if __name__ == '__main__':

    image_to_csv_pipeline()
