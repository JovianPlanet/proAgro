import sys
import cv2
import os, glob
import numpy as np

from panel_detection.process_img import get_panels

imagePath = '/media/davidjm/Disco_Compartido/david/datasets/ProyectoAgro/AGUACATE23noviembre/BLUE/000'
imageName = glob.glob(os.path.join(imagePath,'IMG_00**_2.tif'))#[0]#IMG_0038_3

#get_panels(os.path.join(imagePath,'IMG_0036_3.tif'), th_type='std', th_val=127, i_lo=120, i_hi=160)

th_type = 'std' # 'otsu' 'std' 'adaptive'
th_val = 127
i_lo = 110
i_hi = 165
K = 10

print(f'\nConfiguracion:\nUmbral:{th_type}, Valor umbral {th_val}, i low: {i_lo}, i hi: {i_hi}, K: {K}\n')

panels = {'Blue444': [], 'Green531': [], 'Red650': [], 'RedEdge705': [], 'RedEdge740': []}
keys = list(panels.keys())

for i in range(1, 6):
    imageName = glob.glob(os.path.join(imagePath, f'IMG_00**_{i}.tif'))
    print(f'\n*** Buscando paneles para la banda {keys[i-1]} sufijo {i}***\n')

    for image in imageName:
        panels[keys[i-1]].append(get_panels(image, 
                                         th_type=th_type, 
                                         th_val=th_val, 
                                         i_lo=i_lo, 
                                         i_hi=i_hi, 
                                         K=K)
        )
    print(f'Num panels en la banda {keys[i-1]}, sufijo ({i}) = {sum(panels[keys[i-1]])}')


print(f'\nNum panels blue 444 (1) = {sum(panels["Blue444"])}')
print(f'Num panels green 531 (2) = {sum(panels["Green531"])}')
print(f'Num panels red 650 (3) = {sum(panels["Red650"])}')
print(f'Num panels Red edge 705 (4) = {sum(panels["RedEdge705"])}')
print(f'Num panels Red edge 740 (5) = {sum(panels["RedEdge740"])}')


'''
1: th_type='otsu', i_lo=110, i_hi=145
2: th_type='otsu', i_lo=120, i_hi=155
3: th_type='std', th_val=127, i_lo=125, i_hi=160
4: th_type='otsu', i_lo=120, i_hi=155
5: th_type='otsu', i_lo=130, i_hi=165
'''

'''
exiftool IMG_0007_5.tif | grep Band
'''