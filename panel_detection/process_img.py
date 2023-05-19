import sys
import cv2
import os, glob
import numpy as np
from .utils import blur, erosion, get_shape, get_intensity, bin_img, process_contours, bin_cluster


def find_clusters(img, K=5, i_lo=120, i_hi=140, name=''):

    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # img_convert = img.copy() #defining image to experiment with number of clusters

    vectorized = imgray.reshape((-1, 1))
    vectorized = np.float32(vectorized)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    attempts = 10

    # reshape array to get the long list of RGB colors and then cluster using KMeans()

    for k in range(3, K+1):
    
        ret, labels, centers = cv2.kmeans(vectorized, k, None, criteria, attempts, cv2.KMEANS_PP_CENTERS)
        centers = np.uint8(centers)

        newimage = centers[labels.flatten()]
        newimage = newimage.reshape(imgray.shape)

        #bin_cluster(img, centers)

        cv2.destroyAllWindows()

        i=0

        # if '07_4' in name:
        #     print(f'{k=}')

        for r in np.unique(labels)[1:]:

            labels_ = np.where(labels==r, r, 0)
            l = np.where(labels==r, 255, 0)
            res = centers[labels_.flatten()]

            result_image1 = res.reshape((imgray.shape))
            w = int(np.unique(result_image1)[1])
            a = cv2.inRange(result_image1, w, w)
            #ret, thresh = cv2.threshold(result_image1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            eroded = bin_img(a*imgray, 'otsu')

            #contours = None

            contours, hierarchy = cv2.findContours(a*imgray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1) # CHAIN_APPROX_SIMPLE #RETR_TREE 

            c = process_contours(img, contours, i_lo, i_hi, name)

            if c is not None:
                #print(f'k={k}')
                return True

            # cv2.imshow(f'{"path[-15:]"}, r={r}', a*imgray)#thresh*img)
            # cv2.waitKey(0)


def get_panels(path, th_type='std', th_val=127, i_lo=120, i_hi=140, K=5):

    '''
    img: imagen
    th_type: tipo de umbral ('std' u 'Otsu')
    th_val: valor para umbralizar en caso que th_type='std'
    i_lo: limite inferior de intensidad (criterio para encontrar el panel)
    i_hi: limite superior de intensidad (criterio para encontrar el panel)
    '''

    img = cv2.imread(path)
    img_ = img.copy()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    eroded = bin_img(gray, th_type, th_val)
    # if '07_4' in path:
    #     cv2.imshow(f'process cotours {path[-15:]}', eroded)
    #     cv2.waitKey(0)

    contours, hierarchy = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #  CHAIN_APPROX_TC89_L1

    c = process_contours(img, contours, i_lo=i_lo, i_hi=i_hi, name=path[-15:])

    if c:
        #print(f'***La imagen {path[-15:]} contiene panel***\n')
        return True

    c = find_clusters(img_, K, i_lo=i_lo, i_hi=i_hi, name=path[-15:])

    if c:
        #print(f'***La imagen {path[-15:]} contiene panel (kmeans)***\n')
        return True

    else:
        return False

    