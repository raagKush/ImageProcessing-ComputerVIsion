import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"histogram-equalization.jpg",0)


count = {}

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i,j] in count.keys():
            count[img[i,j]] +=1
        
        else:
            count[img[i,j]] = 1

sortedDict = dict(sorted(count.items()))

sortedKeys = list(sortedDict.keys())
sortedValues = list(sortedDict.values())

totalPix = img.shape[0]*img.shape[1]

cdf = [sortedValues[0]/totalPix]
for i in range(1,len(sortedValues)):
    cdf.append(cdf[i-1]+sortedValues[i]/totalPix)

mapping = {}

for i in range(len(sortedKeys)):
    mapping[sortedKeys[i]] = int(cdf[i]*255)
    
equalizedImg = img.copy()

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        
        equalizedImg[i,j] = mapping[img[i,j]]
