import numpy as np
import cv2
import keras
from keras.layers import Conv2D,Dense,MaxPooling2D,Flatten
import os
import glob

def ReadingImg():
    AnimalsList = ('butterfly', 'cat', 'chicken', 'cow', 'dog', 'elephant', 'horse', 'rabbit', 'sheep','spider')
    root='images/raw-img';

    all_images=[];
    
    train_labels = []
    train_images = []

    validation_labels = []
    validation_images = []

    
    index=0;
    
    for item in AnimalsList:
        path =os.path.join(root,item,"*.jpeg")
        files = glob.glob(path)  # Read all the jpg files name into the files list
        for file in files[:300]:
            
            img = cv2.imread(file)
            resize_img=cv2.resize(img,(300,300))
            resize_img=resize_img/255.0    #normalization
            all_images.append(resize_img)
        
        
        
ReadingImg()

