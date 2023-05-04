import sys
import cv2
import os, glob
import numpy as np
from .utils import blur, erosion, get_shape, get_intensity

'''
Funcion que retorna las coordenadas del panel
para las imagenes BLUE.
Sufijo: 3
Band name: Red-650
'''

def get_red650_panel(image):

    areas = []
    #for image in imageName[:]:
    img = cv2.imread(image)

    if '01_3' in image:
        img = cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8), iterations=2)
    elif '07_3' in image:
        img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8), iterations=2)
    elif '36_3' in image:
        img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8), iterations=2)
    elif '54_3' in image:
        img = cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8), iterations=4)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #imgray = gray.copy()

    blurred = blur(gray, canny=False)

    #blurred = cv2.morphologyEx(blurred, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))

    ret, thresh = cv2.threshold(blurred, 127, 255, 0)
    #thresh = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,2)
    eroded = erosion(thresh)
    # if '54_3' in image:
    #     cv2.imshow('Eroded', thresh)
    #     cv2.waitKey(0)

    contours, hierarchy = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    i = 0
    for contour in contours:

        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        
        if area > 15000 and len(contour) < 1000:

            n = img.copy()

            cv2.destroyAllWindows()

            epsilon = 0.08 * perimeter
            approx = cv2.approxPolyDP(contour, epsilon, True)

            intensity = get_intensity(n, approx)

            shape = get_shape(approx)

            # if '01_3' in image:
            #     print(f'{image[-15:]}:\n')
            #     print(f'area = {area:.3f}, perimetro = {perimeter:.3f}, Num points = {len(contour)}, intensidad {intensity:.3f}\n')
            #     cv2.drawContours(n, contour, -1, (0, 255 - i*50, 0), 3)
            #     cv2.imshow(f'Imagen {image[-15:]}', n)
            #     cv2.waitKey(0)


            if intensity < 160 and intensity > 130 and shape == 'square' and perimeter < 900: # Para BLUE 3 

                areas.append(area)

                print(f'***La imagen {image[-15:]} contiene panel***\n')

                # cv2.drawContours(n, contour, -1, (0, 255 - i*50, 0), 3)
                # cv2.imshow(f'Imagen {image[-15:]}', n)
                # cv2.waitKey(0)

                print(f'Area = {area:.3f}, perimetro = {perimeter:.3f}, Num points = {len(contour)} intensidad {intensity:.3f}')
                print(f'Area panel (aproximado) = {cv2.contourArea(approx)}, Forma = {shape}')
                print(f'Las coordenadas del panel son: \n\n{approx}\n')

                # cv2.imshow("Panel segmentado", blank_image)
                # cv2.waitKey(0)

            i += 1
    areas = np.array(areas)
    print(f'Numero de paneles = {areas.shape}')
    print(f'Area promedio: {np.mean(areas)}, area min = {np.min(areas)}, area max = {np.max(areas)}\n')

    return approx