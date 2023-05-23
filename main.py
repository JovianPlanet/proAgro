import sys
import cv2
import os, glob
import numpy as np

from panel_detection.process_img import get_panels

red_in = ['IMG_0001', 'IMG_0003', 'IMG_0005', 'IMG_0008', 'IMG_0010', 'IMG_0012', 'IMG_0014', 'IMG_0017', 'IMG_0019', 'IMG_0021',\
          'IMG_0024', 'IMG_0026', 'IMG_0029', 'IMG_0031', 'IMG_0033', 'IMG_0035', 'IMG_0037', 'IMG_0039', 'IMG_0041', 'IMG_0043',\
          'IMG_0045', 'IMG_0047', 'IMG_0049', 'IMG_0051', 'IMG_0053', 'IMG_0055', 'IMG_0057', 'IMG_0058', 'IMG_0016', 'IMG_0000',\
          'IMG_0007', 'IMG_0023']

blue_in = ['IMG_0001', 'IMG_0003', 'IMG_0005', 'IMG_0007', 'IMG_0009', 'IMG_0011', 'IMG_0013', 'IMG_0016', 'IMG_0018', 'IMG_0020',\
           'IMG_0022', 'IMG_0024', 'IMG_0027', 'IMG_0029', 'IMG_0032', 'IMG_0034', 'IMG_0036', 'IMG_0038', 'IMG_0040', 'IMG_0042',\
           'IMG_0044', 'IMG_0046', 'IMG_0048', 'IMG_0050', 'IMG_0052', 'IMG_0054', 'IMG_0056', 'IMG_0057', 'IMG_0015', 'IMG_0000'] 

blue_nums = ['38_4']
red_nums  = ['35_4']

imagePath = '/media/davidjm/Disco_Compartido/david/datasets/ProyectoAgro/AGUACATE23noviembre/BLUE/000'

th_type = 'std' # 'otsu' 'std' 'adaptive'
th_val = 127
i_lo = 110
i_hi = 168
K = 10

print(f'\nConfiguracion:\nUmbral:{th_type}, Valor umbral {th_val}, i low: {i_lo}, i hi: {i_hi}, K: {K}\n')

panels_blue = {'Blue444': [], 'Green531': [], 'Red650': [], 'RedEdge705': [], 'RedEdge740': []}
keys = list(panels_blue.keys())

print(f'\n*** Buscando paneles (BLUE)***\n')
for i in range(1, 6):
    imageName = glob.glob(os.path.join(imagePath, f'IMG_00**_{i}.tif'))

    for image in imageName:
        if image[-14:-6] in blue_in:
            panels_blue[keys[i-1]].append(get_panels(image, 
                                             th_type=th_type, 
                                             th_val=th_val, 
                                             i_lo=i_lo, 
                                             i_hi=i_hi, 
                                             K=K,
                                             nums=blue_nums)
            )

    print(f'Num panels en la banda {keys[i-1]}, sufijo ({i}) = {sum(panels_blue[keys[i-1]])}')

print(f'\nTotal BLUE = {sum([sum(panels_blue[key]) for key in keys])}')


imagePath = '/media/davidjm/Disco_Compartido/david/datasets/ProyectoAgro/AGUACATE23noviembre/RED/000'

panels_red = {'Blue': [], 'Green': [], 'Red': [], 'NIR': [], 'RedEdge': []}
keys = list(panels_red.keys())

print(f'\n*** Buscando paneles (RED)***\n')
for i in range(1, 6):
    imageName = glob.glob(os.path.join(imagePath, f'IMG_00**_{i}.tif'))

    redins = 0
    for image in imageName:
        if image[-14:-6] in red_in:
            panels_red[keys[i-1]].append(get_panels(image, 
                                             th_type=th_type, 
                                             th_val=th_val, 
                                             i_lo=i_lo, 
                                             i_hi=i_hi, 
                                             K=K,
                                             nums=red_nums)
            )

        
    print(f'Num panels en la banda {keys[i-1]}, sufijo ({i}) = {sum(panels_red[keys[i-1]])}')

print(f'\nTotal RED = {sum([sum(panels_red[key]) for key in keys])}')


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

