import sys
import cv2
import os, glob
import numpy as np

from panel_detection.get_blue444_panel import get_blue444_panel
from panel_detection.get_green531_panel import get_green531_panel
from panel_detection.get_red650_panel import get_red650_panel
from panel_detection.get_redEdge705_panel import get_redEdge705_panel
from panel_detection.get_redEdge740_panel import get_redEdge740_panel


from panel_detection.panel_kmeans import get_panel_kmeans

imagePath = '/media/davidjm/Disco_Compartido/david/datasets/ProyectoAgro/AGUACATE23noviembre/BLUE/000'
imageName = glob.glob(os.path.join(imagePath,'IMG_00**_2.tif'))#[0]#IMG_0038_3

get_panel_kmeans(os.path.join(imagePath,'IMG_0001_1.tif'))

# panels = {'Blue444': [], 'Green531': [], 'Red650': [], 'RedEdge705': [], 'RedEdge740': []}
# for image in imageName[:]:
#     #panels['Blue444'].append(get_blue444_panel(image)) # (os.path.join(imagePath,'IMG_0032_1.tif'))
#     panels['Green531'].append(get_green531_panel(image))
#     #panels['Red650'].append(get_red650_panel(image))
#     #panels['RedEdge705'].append(get_redEdge705_panel(image))
#     #panels['RedEdge740'].append(get_redEdge740_panel(image))
#     # if '03_1' in image:
#     #get_panel_kmeans(image)


# print(f'Num panels blue 444 (1) = {sum(panels["Blue444"])}')
# print(f'Num panels green 531 (2) = {sum(panels["Green531"])}')
# print(f'Num panels red 650 (3) = {sum(panels["Red650"])}')
# print(f'Num panels Red edge 705 (4) = {sum(panels["RedEdge705"])}')
# print(f'Num panels Red edge 740 (5) = {sum(panels["RedEdge740"])}')



