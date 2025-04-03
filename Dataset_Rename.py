import os
from PIL import Image
home = "D:\Suryansh\Workspace\AI\CV\Image Classification\\train"
filetype = ".jpeg"

objects=["Cat","Dog","Human"]

for i in objects:
    count = 0
    pathh = os.path.join(home,i)
    # print("Listing Directory - ", i)
    # print(os.listdir(path=pathh))
    for file in os.listdir(path=pathh):
        filename_old = os.path.join(pathh,file)
        filename_new = os.path.join(pathh,str(count) + filetype)
        img = Image.open(filename_old)
        try:
            img.save(filename_new)
        except:
            pass
        print(f"Renamed {file} -> {filename_new}")
        count+=1
