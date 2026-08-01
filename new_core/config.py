import pynput
import os

from pynput.keyboard import Controller
from pynput.mouse import Controller
from screeninfo import get_monitors

provinces = ("aurora","aurora", "bataan","bataan", "bulacan","bulacan", "nueva_ecija","nueva_ecija", "pampanga","pampanga", "tarlac","tarlac", "zambales","zambales")
kb = pynput.keyboard.Controller()
ms = pynput.mouse.Controller()
link_of_interest = "https://www.facebook.com/DABantayPresyoGitnangLuzon"
home = os.path.expanduser("~")
ai_model = 'minimax-m3:cloud'
mouse_psx, mouse_psy = ((get_monitors()[0].width) / 2,(get_monitors()[0].height) / 3 )
screen_psx, screen_psy = ((get_monitors()[0].width) / 3,(get_monitors()[0].height) / 3)
box = (290,250,1100,1875)
apiKey = ""

download_dir = os.path.join(home, "Downloads")
bantay_presyo = os.path.join(home, "Downloads","bantay_presyo")
zip_bp = os.path.join(home, "Downloads","bantay_presyo","bantay_presyo.zip")
system_prompt = 'you are a data entry helper, parsing images prices and turning them to csv code to copy and paste'

prompt = """give me the prices listed on the image on a csv code I can copy and paste, do not add a header and footer(both text or '''), and DO NOT MODIFY the template just put in the value. Category;Item;Unit;Low;High;Average;Current;

IMPORTED COMMERCIAL RICE;Jasponica;kg;;;;;

IMPORTED COMMERCIAL RICE;Basmati Rice;kg;;;;;

IMPORTED COMMERCIAL RICE;Glutinous Rice;kg;;;;;

IMPORTED COMMERCIAL RICE;Special;kg;;;;;

IMPORTED COMMERCIAL RICE;Premium;kg;;;;;

IMPORTED COMMERCIAL RICE;Well Milled;kg;;;;;

IMPORTED COMMERCIAL RICE;Regular Milled;kg;;;;;

LOCAL COMMERCIAL RICE;Jasponica;kg;;;;;

LOCAL COMMERCIAL RICE;Basmati Rice;kg;;;;;

LOCAL COMMERCIAL RICE;Glutinous Rice;kg;;;;;

LOCAL COMMERCIAL RICE;Special;kg;;;;;

LOCAL COMMERCIAL RICE;Premium;kg;;;;;

LOCAL COMMERCIAL RICE;Well Milled;kg;;;;;

LOCAL COMMERCIAL RICE;Regular Milled;kg;;;;;

CORN;Corn (White);kg;;;;;

CORN;Corn (Yellow);kg;;;;;

CORN;Corn Grits (White - Food Grade);kg;;;;;

CORN;Corn Grits (Yellow - Food Grade);kg;;;;;

CORN;Corn Cracked (Yellow - Food Grade);kg;;;;;

CORN;Corn Grits;kg;;;;;

LEGUMES;Mung Bean;kg;;;;;

FISH;Bangus (Large);kg;;;;;

FISH;Bangus (Medium);kg;;;;;

FISH;Tilapia (Medium);kg;;;;;

FISH;Galunggong (Local) Male- med;kg;;;;;

FISH;Galunggong (Imported) Male- med;kg;;;;;

FISH;Alumahan- medium;kg;;;;;

FISH;Bonito;kg;;;;;

FISH;Salmon Head;kg;;;;;

FISH;Sardines (Tamban);kg;;;;;

FISH;Squid (Pusit);kg;;;;;

FISH;Yellow-Fin Tuna (Tambakol);kg;;;;;

LIVESTOCK;Beef Rump;kg;;;;;

LIVESTOCK;Beef Brisket;kg;;;;;

LIVESTOCK;Pork Ham;kg;;;;;

LIVESTOCK;Pork Belly;kg;;;;;

LIVESTOCK;Frozen Kasim;kg;;;;;

LIVESTOCK;Frozen Liempo;kg;;;;;

LIVESTOCK;Whole Chicken;kg;;;;;

LIVESTOCK;Chicken Egg (White- Peewe);pc;;;;;

LIVESTOCK;Chicken Egg (White- Extra Small);pc;;;;;

LIVESTOCK;Chicken Egg (White- Small);pc;;;;;

LIVESTOCK;Chicken Egg (White- Medium);pc;;;;;

LIVESTOCK;Chicken Egg (White- Large);pc;;;;;

LIVESTOCK;Chicken Egg (White- Extra Large);pc;;;;;

LIVESTOCK;Chicken Egg (White- Jumbo);pc;;;;;

LIVESTOCK;Chicken Egg (Brown- Medium);pc;;;;;

LIVESTOCK;Chicken Egg (Brown- Large);pc;;;;;

LIVESTOCK;Chicken Egg (Brown- Extra Large);pc;;;;;

LOWLAND VEGETABLES;Ampalaya;kg;;;;;

LOWLAND VEGETABLES;Sitao;kg;;;;;

LOWLAND VEGETABLES;Pechay (Native);kg;;;;;

LOWLAND VEGETABLES;Squash;kg;;;;;

LOWLAND VEGETABLES;Eggplant;kg;;;;;

LOWLAND VEGETABLES;Tomato;kg;;;;;

HIGHLAND VEGETABLES;Bell Pepper (Green);kg;;;;;

HIGHLAND VEGETABLES;Bell Pepper (Red);kg;;;;;

HIGHLAND VEGETABLES;Broccoli;kg;;;;;

HIGHLAND VEGETABLES;Cabbage (Rare ball);kg;;;;;

HIGHLAND VEGETABLES;Cabbage (Scorpio);kg;;;;;

HIGHLAND VEGETABLES;Cabbage (Wonder Ball);kg;;;;;

HIGHLAND VEGETABLES;Carrots;kg;;;;;

HIGHLAND VEGETABLES;Habichuelas (Baguio Beans);kg;;;;;

HIGHLAND VEGETABLES;White Potato;kg;;;;;

HIGHLAND VEGETABLES;Pechay (Baguio);kg;;;;;

HIGHLAND VEGETABLES;Chayote;kg;;;;;

HIGHLAND VEGETABLES;Cauliflower;kg;;;;;

HIGHLAND VEGETABLES;Celery;kg;;;;;

HIGHLAND VEGETABLES;Lettuce (Green Ice);kg;;;;;

HIGHLAND VEGETABLES;Lettuce (Iceberg);kg;;;;;

HIGHLAND VEGETABLES;Lettuce (Romain);kg;;;;;

SPICES;Red Onion;kg;;;;;

SPICES;Red Onion (Imported);kg;;;;;

SPICES;White Onion;kg;;;;;

SPICES;White Onion (Imported);kg;;;;;

SPICES;Garlic (Imported);kg;;;;;

SPICES;Garlic (Native);kg;;;;;

SPICES;Ginger;kg;;;;;

SPICES;Chilli (Red);kg;;;;;

FRUITS;Calamansi;kg;;;;;

FRUITS;Banana (Lakatan);kg;;;;;

FRUITS;Banana (Latundan);kg;;;;;

FRUITS;Banana (Saba);kg;;;;;

FRUITS;Papaya;kg;;;;;

FRUITS;Mango (Carabao);kg;;;;;

FRUITS;Avocado;kg;;;;;

FRUITS;Melon;kg;;;;;

FRUITS;Pomelo;kg;;;;;

FRUITS;Watermelon;kg;;;;;

OTHER BASIC NECESSITIES;Sugar (Refined);kg;;;;;

OTHER BASIC NECESSITIES;Sugar (Washed);kg;;;;;

OTHER BASIC NECESSITIES;Sugar (Brown);kg;;;;;

OTHER BASIC NECESSITIES;Cooking Oil (350 ml);ml;;;;;

OTHER BASIC NECESSITIES;Cooking Oil (1liter);L;;;;;

OTHER BASIC NECESSITIES;Cooking Oil Palm (350 ml);ml;;;;;

OTHER BASIC NECESSITIES;Cooking Oil Palm (1liter);L;;;;;

OTHER BASIC NECESSITIES;Cooking Oil Coconut (350ml);ml;;;;;

OTHER BASIC NECESSITIES;Cooking Oil Coconut (1liter);L;;;;;
"""
