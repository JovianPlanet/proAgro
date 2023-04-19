import sys
import cv2 #openCV
import exiftool
import os, glob
import numpy as np
import pyzbar.pyzbar as pyzbar
import matplotlib.pyplot as plt
#import mapboxgl
from micasense.image import Image

def erosion(img):
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5, 5), np.uint8)
  
    # The first parameter is the original image,
    # kernel is the matrix with which image is
    # convolved and third parameter is the number
    # of iterations, which will determine how much
    # you want to erode/dilate a given image.
    img_erosion = cv2.erode(img, kernel, iterations=1)
    img_dilation = cv2.dilate(img, kernel, iterations=1)

    return img_erosion

#imagePath = os.path.join('.','data','0000SET','000')
imagePath = '/media/davidjm/Disco_Compartido/david/datasets/ProyectoAgro/AGUACATE23noviembre/BLUE/000'
imageName = glob.glob(os.path.join(imagePath,'IMG_003*_3.tif'))#[0]#IMG_0038_3
print(len(imageName))
for image in imageName[8:9]:

    img = cv2.imread(image)#(os.path.join(imagePath,'IMG_0038_3.tif'))
    if img is None:
        sys.exit(f"Could not read the image. {image}")
    # cv2.imshow("Display window", img)
    # k = cv2.waitKey(0)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgray = gray.copy()
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    edged = cv2.Canny(blurred, 30, 200)
    # cv2.imshow('Canny Edges Before Contouring', edged)
    # cv2.waitKey(0)

    ret, thresh = cv2.threshold(blurred, 127, 255, 0)
    img_erosion = erosion(thresh)
    cv2.imshow('Thresholded', thresh)
    cv2.imshow('Eroded', img_erosion)
    cv2.waitKey(0)
    # cv2.imshow('Thresholded', gray*thresh)
    # cv2.waitKey(0)
    contours, hierarchy = cv2.findContours(img_erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.imshow('Canny Edges After Contouring', edged)
    # cv2.waitKey(0)


    i = 0
    for contour in contours:

        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        
        if area > 10000 and len(contour) < 1000:

            n = img.copy()
            
            print(f'area = {area}, perimetro = {perimeter}, Num points = {len(contour)}')
            cv2.drawContours(n, contour, -1, (0, 255 - i*50, 0), 3)
            cv2.imshow(str(area), n)
            cv2.waitKey(0)

            cv2.destroyAllWindows()

            epsilon = 0.08 * perimeter
            approx = cv2.approxPolyDP(contour, epsilon, True)
            print(approx)

            # Create blank image
            blank_image = np.zeros(gray.shape, np.uint8)

            # Draw contour in the mask
            cv2.drawContours(blank_image, [approx], -1, (255, 255, 255), -1)

            # Create a mask to select pixels inside the figure
            mask_contour = blank_image == 255

            # Calculate the intensity from the grayscale image
            # filtering out the pixels where in the blank_image their value is not 255
            intensity = np.mean(n[mask_contour])
            print(f'{intensity=}')

            cv2.imshow("Image", blank_image)
            cv2.waitKey(0)

            i += 1

# cv2.drawContours(img, contours, -1, (0,255,0), 3)
# cv2.imshow('Contours', img)
# cv2.waitKey(0)
# img = Image(imageName)
# img.plot_raw(figsize=(8.73,8.73))

# from micasense.panel import Panel
# panel = Panel(img, panelCorners=[[10, 10], [200, 10], [10, 200], [200, 200]])
# if not panel.panel_detected():
#     raise IOError("Panel Not Detected! Check your installation of pyzbar")
# else:
#     panel.plot(figsize=(8,8))
#     panel.plot_image()

# print('Success! Now you are ready for Part 1 of the tutorial.')


'''
find the corners in the image
'''
#gray = np.float32(gray)
#dst = cv2.cornerHarris(gray, 2, 3, 0.04)
#result is dilated for marking the corners, not important
#dst = cv2.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.
#img[dst>0.01*dst.max()]=[0,0,255]
# cv2.imshow('dst',img)
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()



# corners = cv2.goodFeaturesToTrack(canny,4,0.5,50)

# for corner in corners:
#     x,y = corner.ravel()
#     cv2.circle(image,(x,y),5,(36,255,12),-1)

# cv2.imshow('canny', canny)
# cv2.imshow('image', image)
# cv2.waitKey()