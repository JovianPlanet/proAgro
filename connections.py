import os
import glob
import numpy as np
import micasense.metadata as metadata
import exiftool

from PyQt5 import QtWidgets, QtCore
#from popups import ErrorDialog
import GUI

from panel_detection.utils import get_params, get_ImArray
from panel_detection.calculations import get_F, get_L, get_R


class GuiConnections(QtWidgets.QMainWindow, GUI.Ui_Form):

    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pathPanBlue = ''
        self.pathPanRed = ''

        self.browse_blueimg_button.setEnabled(False)
        self.browse_redimg_button.setEnabled(False)

        # Conexiones
        self.browse_bluepanel_button.clicked.connect(self.get_panel_blue)
        self.browse_blueimg_button.clicked.connect(self.get_img_blue)
        self.browse_redpanel_button.clicked.connect(self.get_panel_red)
        self.browse_redimg_button.clicked.connect(self.get_img_red)
        self.compute_button.clicked.connect(self.get_reflectance)

        # Atributos
        self.blue_stack = ''
        self.red_stack = ''

        self.Ims = {'Blue-444'    : None, 'Blue'    : None, 
                    'Green-531'   : None, 'Green'   : None, 
                    'Red-650'     : None, 'Red'     : None, 
                    'Red edge-705': None, 'NIR'     : None, 
                    'Red edge-740': None, 'Red Edge': None
        }

        # El cubo inicia por defecto con los valores de calibracion proporcionados por el fabricante para cada lambda
        self.img_cube = {'Blue-444'    : [53.7], 'Blue'    : [53.7], 
                         'Green-531'   : [53.8], 'Green'   : [53.8], 
                         'Red-650'     : [53.7], 'Red'     : [53.7], 
                         'Red edge-705': [53.6], 'NIR'     : [53.6], 
                         'Red edge-740': [53.6], 'Red Edge': [53.3]
        }

        self.Pans = {'Blue-444'    : None, 'Blue'    : None, 
                     'Green-531'   : None, 'Green'   : None, 
                     'Red-650'     : None, 'Red'     : None, 
                     'Red edge-705': None, 'NIR'     : None, 
                     'Red edge-740': None, 'Red Edge': None
        }
        
        self.panel_cube = {'Blue-444'    : [53.7], 'Blue'    : [53.7], 
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
        self.lineEdit_bluepanel.setText(self.pathPanBlue)

        wc = self.pathPanBlue[:-5] + '*' + self.pathPanBlue[-4:]
        imageName = glob.glob(wc)

        for i, image in enumerate(imageName):
            blueMeta = metadata.Metadata(image, exiftoolPath=self.exiftoolPath)
            bandname = blueMeta.get_item("XMP:BandName")

            self.panel_cube[bandname].append(get_params(blueMeta))
            self.panel_cube[bandname].append(image)

            self.Pans[bandname] = get_ImArray(image)

        self.browse_blueimg_button.setEnabled(True)

        return

    def get_img_blue(self):

        self.pathImgBlue, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")#, "Images (*.tiff *.tif)")
        self.lineEdit_blueimg.setText(self.pathImgBlue)

        wc = self.pathImgBlue[:-5] + '*' + self.pathImgBlue[-4:]
        imageName = glob.glob(wc)
        self.blue_stack = self.pathImgBlue[-10:-6]

        for i, image in enumerate(imageName):
            blueMeta = metadata.Metadata(image, exiftoolPath=self.exiftoolPath)
            bandname = blueMeta.get_item("XMP:BandName")

            self.img_cube[bandname].append(get_params(blueMeta))
            self.img_cube[bandname].append(image)

            self.Ims[bandname] = get_ImArray(image)

        self.browse_blueimg_button.setEnabled(False)

        return


    def get_panel_red(self):

        self.pathPanRed, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")#, "Images (*.tiff *.tif)")
        self.lineEdit_redpanel.setText(self.pathPanRed)
        
        wc = self.pathPanRed[:-5] + '*' + self.pathPanRed[-4:]
        imageName = glob.glob(wc)

        for i, image in enumerate(imageName):
            redMeta = metadata.Metadata(image, exiftoolPath=self.exiftoolPath)
            bandname = redMeta.get_item("XMP:BandName")

            self.panel_cube[bandname].append(get_params(redMeta))
            self.panel_cube[bandname].append(image)

            self.Pans[bandname] = get_ImArray(image)

        self.browse_redimg_button.setEnabled(True)
            
        return

    def get_img_red(self):

        self.pathImgRed, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")#, "Images (*.tiff *.tif)")
        self.lineEdit_redimg.setText(self.pathImgRed)

        wc = self.pathImgRed[:-5] + '*' + self.pathImgRed[-4:]
        imageName = glob.glob(wc)
        self.red_stack = self.pathImgRed[-10:-6]

        for i, image in enumerate(imageName):
            redMeta = metadata.Metadata(image, exiftoolPath=self.exiftoolPath)
            bandname = redMeta.get_item("XMP:BandName")

            self.img_cube[bandname].append(get_params(redMeta))
            self.img_cube[bandname].append(image)

            self.Ims[bandname] = get_ImArray(image)

        self.browse_redimg_button.setEnabled(False)

        return

    def get_reflectance(self):

        fn = 'IMG_B' + self.blue_stack + '_R' + self.red_stack + '.tif'

        # Radiancia espectral por longitud de onda de los paneles
        Lp_lambda = get_L(self.panel_cube, self.Pans) # V_lambda, Rv_lambda, Pc_lambda)
        # Radiancia espectral por longitud de onda de las imagenes
        Li_lambda = get_L(self.img_cube, self.Ims)

        # Factor de calibracion del panel
        Fp_lambda = get_F(self.panel_cube, Lp_lambda)

        # Reflectancia por longitud de onda
        # Rp_lambda = get_R(Lp_lambda, Fp_lambda)
        Ri_lambda = get_R(Li_lambda, Fp_lambda, fn)

        return




