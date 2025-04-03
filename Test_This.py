import os
from tf_keras.models import model_from_json
import numpy as np
from tf_keras.preprocessing import image
import cv2
from PIL import Image

file = open("model.json")
json = file.read()
file.close()
model = model_from_json(json)
model.load_weights("model.h5")
print("Loaded Model from Disk")

images = []

for files in os.listdir("test"):
    images.append(os.path.join("test",files))
    print(*images,sep="\n")

for pics in images:
    img = image.load_img(pics,target_size=(64,64))
    arr_img = image.img_to_array(img)
    cv_img = Image.open(pics)
    cv_img = cv_img.resize((400,400))
    cv_img = np.array(cv_img)
    cv_img = cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
    arr_img = np.expand_dims(arr_img,axis=0)
    result = model.predict(arr_img)
    print(result)
    classes = ["Cat","Dog","Human"]
    output = np.argmax(result)
    cv2.putText(cv_img,classes[output],(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(25,255,50),3)
    # print("Dog" if result[0][0] > 0.8 else "Cat",end="\n\n")
    cv2.imshow("Img",cv_img)
    if cv2.waitKey(0) == ord('q'):
        break