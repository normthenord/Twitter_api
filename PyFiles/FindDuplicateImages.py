from PIL import Image
import glob
import os

img_list = glob.glob(
    "MediaFiles/#HollowKnight/*.jpg")

print(len(img_list))

data_list = []
new_list = []
for img in img_list:
    data = Image.open(img).getdata()
    repeat = False
    for img_data in data_list:
        if list(data) == list(img_data):
            repeat = True
    if repeat == False:
        data_list.append(data)
        new_list.append(img)


print(len(new_list))

for img in img_list:
    if img not in new_list:
        os.remove(img)
