import sys
import os
# from pathlib import Path this is also can be used
from PIL import Image


#my try 
# i = sys.argv[1]
# # ent = Path(i)
# # for s in ent.iterdir():
# #     if Path(s) == 'pocedek/bulbasaur.jpg':
# #         s1 = Image.open(s)
# #         # s1.convert("s1.png",'png')
# #         s1.save('s1.png','png')
# #         print(s.name)
# j = os.listdir(i)
# for s in j:
#     s.save('s.new','png')

#solution

opened_folder = sys.argv[1]
final_folder = sys.argv[2]

if not os.path.exists(final_folder):
    os.makedirs(final_folder)

for filename in os.listdir(opened_folder):
    img = Image.open(f'{opened_folder}{filename}')
    clean_name = os.path.splitext(f'{filename}')[0]
    img.save(f'{final_folder}{clean_name}.png','png')
    print("alll done")
