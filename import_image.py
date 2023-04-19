import cv2
import matplotlib.pyplot as plt
import numpy as np
import os,glob
import math

imagePath = os.path.join('.','data','0000SET','000')
imagePath = '/media/davidjm/Disco_Compartido/david/datasets/ProyectoAgro/AGUACATE23noviembre/BLUE/000'
imageName = os.path.join(imagePath,'IMG_0000_4.tif')

# Read raw image DN values
# reads 16 bit tif - this will likely not work for 12 bit images
imageRaw = plt.imread(imageName)

# Display the image
fig, ax = plt.subplots(figsize=(8,6))
ax.imshow(imageRaw, cmap='gray')
plt.show()

