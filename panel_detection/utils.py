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

def get_shape(approx):
    n_vertices = len(approx)
    if n_vertices == 4:
        # compute the bounding box of the contour and use the
        # bounding box to compute the aspect ratio
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        # a square will have an aspect ratio that is approximately
        # equal to one, otherwise, the shape is a rectangle
        shape = "square" if ar >= 0.9 and ar <= 1.1 else "rectangle"

        return shape

def get_intensity(img, region):
    # Create blank image
    blank_image = np.zeros(img.shape, np.uint8)

    # Draw contour in the mask
    cv2.drawContours(blank_image, [region], -1, (255, 255, 255), -1)

    # Create a mask to select pixels inside the figure
    mask_contour = blank_image == 255

    # Calculate the intensity from the grayscale image
    # filtering out the pixels where in the blank_image their value is not 255
    intensity = np.mean(img[mask_contour])

    return intensity

def plot_outliers(im):
    cv2.imshow(f'Imagen {image[-15:]}', im)
    cv2.waitKey(0)

