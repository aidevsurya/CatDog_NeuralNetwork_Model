# CatDog_NeuralNetwork_Model
This is the small program for students who are beginner in neural network and machine learning.<br>
This program works in multiple part, First - simply download the Dataset of Cat and Dog images Then Preprocessing part comes which converts the other format images in JPEG and rename it well, Then Model Training Starts and then Testing or Predicting.

# Installation
<code> pip install -r requirements.txt </code>

# Run The Program
<code> python Dataset_Creator.py </code> <br>
This will create the dataset of Cat, Dog, Human Faces <br>
then Clean unwanted images and Move all images folder (Cat, Dog, RealHumanFace) inside Folder - Train <br>
and from subset of these images create 8:2 images for validation, You can do in 8:2 ratio = Train:Val folders <br>
<code> python Dataset_Rename.py </code> <br>
this will preprocess the images <br>
<code> python Dataset_Train.py </code> <br>
this will Train the model and save it in two files - <b>Model.json</b> and <b>Model.h5</b> <br>
<code> python Test_This.py </code> <br>
This will run the Program and Predict the result from Test Folder Images
