import sys
import cv2
import os, glob
import numpy as np

from panel_detection.get_blue444_panel import get_blue444_panel
from panel_detection.get_red650_panel import get_red650_panel
from panel_detection.get_green531_panel import get_green531_panel
from panel_detection.get_redEdge705_panel import get_redEdge705_panel
from panel_detection.get_redEdge740_panel import get_redEdge740_panel


from panel_detection.panel_kmeans import get_panel_kmeans

imagePath = '/media/davidjm/Disco_Compartido/david/datasets/ProyectoAgro/AGUACATE23noviembre/BLUE/000'
imageName = glob.glob(os.path.join(imagePath,'IMG_00**_5.tif'))#[0]#IMG_0038_3

panels_1 = []
panels_2 = []
panels_3 = []
panels = [[], [], [], [], []]
for image in imageName[:]:
    #panels_1.append(get_blue444_panel(image))#(os.path.join(imagePath,'IMG_0032_1.tif'))
    #panels[1].append(get_green531_panel(image))
    #panels_3.append(get_red650_panel(image))
    panels[4].append(get_redEdge740_panel(image))
    # if '03_1' in image:
    #get_panel_kmeans(image)


#print(f'Num panels blue 444 (1) = {len(panels_1)}')
print(f'Num panels green 531 (2) = {sum(panels[1])}')
#print(f'Num panels red 650 (3) = {sum(panels_3)}')
print(f'Num panels Red edge 705 (4) = {sum(panels[3])}')
print(f'Num panels Red edge 740 (5) = {sum(panels[4])}')



