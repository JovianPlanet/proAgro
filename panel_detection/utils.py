import cv2
import numpy as np

def blur(img, canny=True):
    filtered = cv2.GaussianBlur(img, (3, 3), 0)

    if canny:
        filtered = cv2.Canny(filtered, 30, 200)

    return filtered

def erosion(img):
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5, 5), np.uint8)
  
    # The first parameter is the original image, kernel is the matrix with which image is
    # convolved and third parameter is the number of iterations, which will determine how much
    # you want to erode/dilate a given image.
    img_erosion = cv2.erode(img, kernel, iterations=1)
    #img_dilation = cv2.dilate(img, kernel, iterations=1)

    return img_erosion

def plot_outliers(im):
    cv2.imshow(f'Imagen {image[-15:]}', im)
    cv2.waitKey(0)