import sys
import cv2
import os, glob
import numpy as np

from panel_detection.get_blue444_panel import get_blue444_panel
from panel_detection.get_red650_panel import get_red650_panel
from panel_detection.panel_kmeans import get_panel_kmeans

imagePath = '/media/davidjm/Disco_Compartido/david/datasets/ProyectoAgro/AGUACATE23noviembre/BLUE/000'
imageName = glob.glob(os.path.join(imagePath,'IMG_00**_3.tif'))#[0]#IMG_0038_3

panels_1 = []
panels_3 = []
for image in imageName[:]:
    #panels_1.append(get_blue444_panel(image))#(os.path.join(imagePath,'IMG_0032_1.tif'))
    panels_3.append(get_red650_panel(image))
    # if '03_1' in image:
    #     get_panel_kmeans(image)



#print(f'Num panels blue 444 (1) = {len(panels_1)}')
print(f'Num panels red 650 (3) = {sum(panels_3)}')





