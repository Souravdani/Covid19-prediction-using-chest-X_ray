# -*- coding: utf-8 -*-
"""
Detecting Covid-19 from chest X-ray
Created on Tue May 23 19:58:52 2023
@author: Soura
"""
import pandas as pd
import os
import shutil

FILE_PATH= "metadata.csv"
IMAGES_PATH= "images"
df= pd.read_csv(FILE_PATH)

## Creating a folder in dataset using od module
TARGET_DIR= 'Dataset\\covid'
if not os.path.exists(TARGET_DIR):
    os.mkdir(TARGET_DIR)
    print("Covid folder created")
    
cnt=0
for (i,row) in df.iterrows():
    if row["finding"]== "Pneumonia/Viral/COVID-19":
        cnt+=1
print(cnt)   ## 584


## We only need X_rays having front views not side or back views
cnt=0
for (i,row) in df.iterrows():
    if row["finding"]== "Pneumonia/Viral/COVID-19" and row["view"]== "PA":
        filename= row["filename"]
        image_path= os.path.join(IMAGES_PATH,filename)
        image_copy_path= os.path.join(TARGET_DIR,filename)
        shutil.copy2(image_path,image_copy_path)
        print("Moving image", cnt)
        cnt+=1
print(cnt)  ## 196

# Sampling of images from kaggle
import random
KAGGLE_FILE_PATH= "chest_xray/train/NORMAL"
TARGET_NORMAL_DIR= "Dataset/Normal"

image_names= os.listdir(KAGGLE_FILE_PATH)
image_names
random.shuffle(image_names)

for i in range(196):
    image_name= image_names[i]
    image_path= os.path.join(KAGGLE_FILE_PATH, image_name)
    
    target_path= os.path.join(TARGET_NORMAL_DIR, image_name)
    shutil.copy(image_path, target_path)
    print("Copying image", i)    




















