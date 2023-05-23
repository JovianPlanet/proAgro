import numpy as np
import cv2

from .utils import process_contours, bin_img

def find_clusters(img, K=5, name='', i_hi=165, nums=[]):

    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    vectorized = imgray.reshape((-1, 1))
    vectorized = np.float32(vectorized)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    attempts = 10

    # reshape array to get the long list of RGB colors and then cluster using KMeans()

    for k in range(3, K+1):
    
        ret, labels, centers = cv2.kmeans(vectorized, k, None, criteria, attempts, cv2.KMEANS_PP_CENTERS)
        centers = np.uint8(centers)

        cv2.destroyAllWindows()

        for r in np.unique(labels)[1:]:

            labels_ = np.where(labels==r, r, 0)
            l = np.where(labels==r, 255, 0)
            res = centers[labels_.flatten()]

            result_image1 = res.reshape((imgray.shape))
            w = int(np.unique(result_image1)[1])
            a = cv2.inRange(result_image1, w, w)
            #ret, thresh = cv2.threshold(result_image1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            eroded = bin_img(a*imgray, 'otsu')

            contours, hierarchy = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1) # CHAIN_APPROX_SIMPLE #RETR_TREE 

            c = process_contours(img, contours, name, i_hi, nums)

            if c is not None:
                return True