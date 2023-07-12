import cv2
import csv
from .utils import get_shape, get_intensity


def process_contours(n, contours, L, name='', i_hi=168, nums=[]):

    for contour in contours:

        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        
        if area > 18000 and len(contour) < 1000 and perimeter < 900:

            cv2.destroyAllWindows()

            epsilon = 0.09 * perimeter
            approx = cv2.approxPolyDP(contour, epsilon, True)

            intensity = get_intensity(L, approx)

            shape = get_shape(approx)

            box  = cv2.boxPoints(cv2.minAreaRect(contour))
            area_box = cv2.contourArea(box)
            area_ratio = area / area_box

            if shape == 'square' and intensity < i_hi and area_ratio > 0.75: #i_lo < intensity < i_hi and shape == 'square':

                # with open('areas.csv','a') as fd:
                #     writer = csv.writer(fd)
                #     writer.writerow([name, str(area), str(perimeter), str(intensity), str(area_box), str(area_ratio)])

                # plot_ctr(n, contour, name)
                # plot_panel(n.shape, approx, name)

                return intensity 

    return None