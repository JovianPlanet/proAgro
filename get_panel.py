import sys
import cv2
import os, glob
import numpy as np

from panel_detection.get_red650_panel import get_red650_panel


imagePath = '/media/davidjm/Disco_Compartido/david/datasets/ProyectoAgro/AGUACATE23noviembre/BLUE/000'
imageName = glob.glob(os.path.join(imagePath,'IMG_00**_3.tif'))#[0]#IMG_0038_3

coor_blue3 = get_red650_panel(os.path.join(imagePath,'IMG_0036_3.tif'))

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