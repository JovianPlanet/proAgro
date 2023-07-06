import os
import glob
import numpy as np
import micasense.metadata as metadata
import exiftool

from PyQt5 import QtWidgets, QtCore
#from popups import ErrorDialog
import GUI

from panel_detection.manual import draw_panel
from panel_detection.process_img import get_panels
from panel_detection.utils import get_params, get_ImArray
from panel_detection.calculations import get_F, get_V, get_Rv, get_L, get_R, correct_im, get_In, get_L2


class GuiConnections(QtWidgets.QMainWindow, GUI.Ui_Form):

    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pathPanBlue = ''
        self.pathPanRed = ''

        # Conexiones
        self.browse_blue_button.clicked.connect(self.get_panel_blue)
        self.browse_red_button.clicked.connect(self.get_panel_red)
        self.search_button.clicked.connect(self.get_reflectance)

        # Atributos
        # El cubo inicia por defecto con los valores de intensidad proporcionados por el fabricante para cada lambda
        self.Ims = {'Blue-444'    : None, 'Blue'    : None, 
                    'Green-531'   : None, 'Green'   : None, 
                    'Red-650'     : None, 'Red'     : None, 
                    'Red edge-705': None, 'NIR'     : None, 
                    'Red edge-740': None, 'Red Edge': None
        }

        self.Pans = {'Blue-444'    : None, 'Blue'    : None, 
                     'Green-531'   : None, 'Green'   : None, 
                     'Red-650'     : None, 'Red'     : None, 
                     'Red edge-705': None, 'NIR'     : None, 
                     'Red edge-740': None, 'Red Edge': None
        }
        
        self.cube = {'Blue-444'    : [53.7], 'Blue'    : [53.7], 
                     'Green-531'   : [53.8], 'Green'   : [53.8], 
                     'Red-650'     : [53.7], 'Red'     : [53.7], 
                     'Red edge-705': [53.6], 'NIR'     : [53.6], 
                     'Red edge-740': [53.6], 'Red Edge': [53.3]
        }

        self.exiftoolPath = None
        if os.name == 'nt':
            self.exiftoolPath = os.environ.get('exiftoolpath')

    # Metodo que captura la ruta donde se encuentra la imagen
    def get_panel_blue(self):

        self.pathPanBlue, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")#, "Images (*.tiff *.tif)")
        self.lineEdit_blue.setText(self.pathPanBlue)

        wc = self.pathPanBlue[:-5] + '*' + self.pathPanBlue[-4:]
        imageName = glob.glob(wc)

        for i, image in enumerate(imageName):
            blueMeta = metadata.Metadata(image, exiftoolPath=self.exiftoolPath)
            bandname = blueMeta.get_item("XMP:BandName")

            self.cube[bandname].append(get_panels(image))
            self.cube[bandname].append(get_params(blueMeta))

            self.Pans[bandname] = get_ImArray(image)

        return

    def get_panel_red(self):

        self.pathPanRed, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")#, "Images (*.tiff *.tif)")
        self.lineEdit_red.setText(self.pathPanRed)
        
        wc = self.pathPanRed[:-5] + '*' + self.pathPanRed[-4:]
        imageName = glob.glob(wc)

        for i, image in enumerate(imageName):
            redMeta = metadata.Metadata(image, exiftoolPath=self.exiftoolPath)
            bandname = redMeta.get_item("XMP:BandName")

            self.cube[bandname].append(get_panels(image))
            self.cube[bandname].append(get_params(redMeta))

            self.Pans[bandname] = get_ImArray(image)
            
        return

    # Computes the reflectance image per wavelength (Metodo documento Word calibracion.docx)
    def get_reflectance(self):

        # Factor de calibracion por banda
        F_lambda = get_F(self.cube)
        #print(f'Factores de calibracion = {F_lambda}')

        # Polinomio de vineta
        V_lambda = get_V(self.cube)
        #print(V_lambda)

        Rv_lambda = get_Rv(self.cube)
        #print(Rv_lambda)

        # Imagen original corregida a nivel de negro
        Pc_lambda = correct_im(self.cube, self.Pans)
        #print(Pc_lambda)

        # Radiancia espectral por longitud de onda
        L_lambda = get_L(self.cube, V_lambda, Rv_lambda, Pc_lambda)

        # Reflectancia por longitud de onda
        R_lambda = get_R(F_lambda, L_lambda)


    # Computes the reflectance image per wavelength (Metodo pagina micasense)
    def get_reflectance2(self):

        # Factor de calibracion por banda
        F_lambda = get_F(self.cube)
        #print(f'Factores de calibracion = {F_lambda}')

        V_lambda = get_V(self.cube)
        #print(V_lambda)

        Rv_lambda = get_Rv(self.cube)

        Pn_lambda = get_In(self.cube, self.Pans)

        L_lambda = get_L2(self.cube, V_lambda, Rv_lambda, Pn_lambda)

        #print(Pn_lambda)


