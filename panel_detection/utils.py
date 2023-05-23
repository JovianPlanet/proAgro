import cv2
import numpy as np
import csv

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

def bin_img(gray, th_type='std', th_val=127):

    # Performs Gaussian blur + threshold

    blurred = blur(gray, canny=False)

    ret, thresh = [], []
    if th_type == 'std':
        ret, thresh = cv2.threshold(blurred, th_val, 255, 0)

    elif th_type == 'otsu':
        ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    elif th_type == 'adapt':
        thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)

    eroded = erosion(thresh)

    return eroded

def process_contours(n, contours, name='', i_hi=165, nums=[]):

    for contour in contours:

        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        
        if area > 18000 and len(contour) < 1000 and perimeter < 900:

            cv2.destroyAllWindows()

            epsilon = 0.09 * perimeter
            approx = cv2.approxPolyDP(contour, epsilon, True)

            intensity = get_intensity(n, approx)

            shape = get_shape(approx)

            if shape == 'square' and intensity < i_hi: #i_lo < intensity < i_hi and shape == 'square':

                if name[7:-4] in nums:
                    pass
                    print(f'Area {name} = {area}')
                    print(f'Perimetro {name} = {perimeter}')
                    print(f'Intensidad {name} = {intensity}')
                    # cv2.drawContours(n, contour, -1, (0, 255 - 50, 0), 3)
                    # cv2.imshow(f'{name}', n)
                    # cv2.waitKey(0)
                else:
                    with open('areas.csv','a') as fd:
                        writer = csv.writer(fd)
                        writer.writerow([name, str(area), str(perimeter), str(intensity)])


                # Graficar el contorno
                # cv2.drawContours(n, contour, -1, (0, 255 - 50, 0), 3)
                # cv2.imshow(f'{name}', n)
                # cv2.waitKey(0)

                # #Graficar el panel segmentado (binarizado)
                # temp = np.zeros(n.shape, np.uint8)
                # cv2.drawContours(temp, [approx], -1, (255, 255, 255), -1)
                # cv2.imshow(f"{name}", temp)
                # cv2.waitKey(0)

                return True #approx, intensity 

    return None

def morph(img, kernel, mode='open'):
    if mode is 'open':
        m = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    elif mode is 'close':
        m = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    return m

def bin_cluster(img, centers):

    for center in centers:
        # select color and create mask
        #print(center)
        layer = img.copy()
        mask = cv2.inRange(layer, center, center)

        # apply mask to layer 
        layer[mask == 0] = [0]#,0,0]
        cv2.imshow('layer', layer)
        cv2.waitKey(0)


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