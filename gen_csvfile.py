#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2,os
import numpy as np
import csv
import glob


# In[2]:


file = open("csv/dataset.csv","w")
label = "Parasitized"
dirList = glob.glob("cell_images/"+label+"/*.png")


# In[3]:


#Label,area_0,area_1,area_2,area_3,area_4
file.write("Label,area_0,area_1,area_2,area_3,area_4\n")
for img_path in dirList:

    im = cv2.imread(img_path)
    
    im = cv2.GaussianBlur(im,(5,5),2)



    im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(im_gray,127,255,0)
    contours,_ = cv2.findContours(thresh,1,2)


    file.write("\""+label+"\"")
    file.write(",")
    
    try:
        area = cv2.contourArea(contours[1])
        file.write(str(area))
    except:
        file.write("0")
    
    for i in range(1,5):
        file.write(",")
        try:
            area = cv2.contourArea(contours[i])
            file.write(str(area))
        except:
            file.write("0")

        


    file.write("\n")


# In[4]:


label = "Uninfected"
dirList = glob.glob("cell_images/"+label+"/*.png")


# In[5]:


#Label,area_0,area_1,area_2,area_3,area_4

for img_path in dirList:

    im = cv2.imread(img_path)
    
    im = cv2.GaussianBlur(im,(5,5),2)



    im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(im_gray,127,255,0)
    contours,_ = cv2.findContours(thresh,1,2)


    file.write("\""+label+"\"")
    file.write(",")
    
    try:
        area = cv2.contourArea(contours[1])
        file.write(str(area))
    except:
        file.write("0")
    
    for i in range(1,5):
        file.write(",")
        try:
            area = cv2.contourArea(contours[i])
            file.write(str(area))
        except:
            file.write("0")

        


    file.write("\n")


# In[6]:


file.close()

