import cv2
import numpy as np
from .utils import get_intensity
 
def draw_panel(path):
 
    # Read image
    im = cv2.imread(path)
 
    # Select ROI # OJO: en la siguiente funcion NO usar caracteres raros como tildes en el primer parametro
    r = cv2.selectROI(f'Seleccione manualmente el panel de la imagen {path[-15:]}.', im) 

    cv2.destroyAllWindows()
 
    # # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
  
    return np.mean(imCrop)