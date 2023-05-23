import sys
import cv2
import os, glob
import numpy as np

from .clustering import find_clusters
from .utils import blur, erosion, get_shape, get_intensity, bin_img, process_contours, bin_cluster, morph


def get_panels(path, th_type='std', th_val=127, i_lo=120, i_hi=165, K=5, nums=[]):

    '''
    img: imagen
    th_type: tipo de umbral ('std' u 'Otsu')
    th_val: valor para umbralizar en caso que th_type='std'
    i_lo: limite inferior de intensidad (criterio para encontrar el panel)
    i_hi: limite superior de intensidad (criterio para encontrar el panel)
    '''

    img = cv2.imread(path)
    img_ = img.copy()
    img__ = img.copy()
    img___ = img.copy()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    eroded = bin_img(gray, th_type, th_val)

    # *** *** *** *** *** #

    # Proceso 1: CV
    contours, hierarchy = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #  CHAIN_APPROX_TC89_L1

    c = process_contours(img, contours, path[-15:], i_hi, nums)

    if c:
        #print(f'***La imagen {path[-15:]} contiene panel***\n')
        return True

    # *** *** *** *** *** #

    # Proceso 2: Morphology
    kernel = np.ones((5, 5), np.uint8)
    morph_ = morph(eroded, kernel, mode='open')

    contours, hierarchy = cv2.findContours(morph_, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #  CHAIN_APPROX_TC89_L1

    c = process_contours(img_, contours, path[-15:], i_hi, nums)

    if c:
        return True

    # *** *** *** *** *** #

    # Proceso 3: kmeans
    c = find_clusters(img__, K, path[-15:], i_hi, nums)

    if c:
        #print(f'***La imagen {path[-15:]} contiene panel (kmeans)***\n')
        return True

    else:
        print(f'No se encontro panel: {path[-15:]}')
        return False
