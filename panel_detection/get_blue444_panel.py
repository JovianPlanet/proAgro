import sys
import cv2
import os, glob
import numpy as np
from .utils import blur, erosion, get_shape, get_intensity

'''
Funcion que retorna las coordenadas del panel para las imagenes BLUE.
Sufijo: 1
Band name: Blue-444
'''

def get_blue444_panel(image):

    img = cv2.imread(image)

    # if '29_1' in image:
    #     img = img*3
    #     #img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8), iterations=2)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgray = gray.copy()

    blurred = blur(gray, canny=False)

    #ret, thresh = cv2.threshold(blurred, 120, 255, 0)
    ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    #thresh = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,2)
    eroded = erosion(thresh)
    # if '29_1' in image:
    #     cv2.imshow(f'Imagen eroded: {image[-15:]}', eroded)
    #     cv2.waitKey(0)

    contours, hierarchy = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    i = 0
    for contour in contours:

        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        
        if area > 15000 and len(contour) < 1000 and perimeter < 900:

            n = img.copy()

            cv2.destroyAllWindows()

            epsilon = 0.09 * perimeter
            approx = cv2.approxPolyDP(contour, epsilon, True)

            intensity = get_intensity(n, approx)

            shape = get_shape(approx)

            # if '29_1' in image:
            #     print(f'{image[-15:]}:\n')
            #     print(f'area = {area:.3f}, perimetro = {perimeter:.3f}, Forma = {shape}, intensidad {intensity:.3f}\n')
            #     cv2.drawContours(n, contour, -1, (0, 255 - i*50, 0), 3)
            #     cv2.imshow(f'Imagen {image[-15:]}', n)
            #     cv2.waitKey(0)


            if 110 < intensity < 145 and shape == 'square':

                print(f'***La imagen {image[-15:]} contiene panel***\n')

                # cv2.drawContours(n, contour, -1, (0, 255 - i*50, 0), 3)
                # cv2.imshow(f'Imagen {image[-15:]}', n)
                # cv2.waitKey(0)

                # print(f'Area = {area:.3f}, perimetro = {perimeter:.3f}, Num points = {len(contour)} intensidad {intensity:.3f}')
                # print(f'Area panel (aproximado) = {cv2.contourArea(approx)}, Forma = {shape}')
                # print(f'Las coordenadas del panel son: \n\n{approx}\n')

                # temp = np.zeros(n.shape, np.uint8)
                # cv2.drawContours(temp, [approx], -1, (255, 255, 255), -1)
                # cv2.imshow("Panel segmentado", temp)
                # cv2.waitKey(0)

                return True #approx, intensity 

    return False #None
    