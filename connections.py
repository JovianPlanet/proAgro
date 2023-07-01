import os
import glob
import nibabel as nib
import numpy as np
import micasense.metadata as metadata
import exiftool

from PyQt5 import QtWidgets, QtCore
#from popups import ErrorDialog
import GUI

from panel_detection.manual import draw_panel
from panel_detection.process_img import get_panels

from panel_detection.utils import get_params

from panel_detection.calculations import get_F, get_V


class GuiConnections(QtWidgets.QMainWindow, GUI.Ui_Form):

    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pathblue = ''
        self.pathred = ''

        # Conexiones
        self.browse_blue_button.clicked.connect(self.get_panel_blue)
        self.browse_red_button.clicked.connect(self.get_panel_red)
        self.search_button.clicked.connect(self.get_reflectance)

        # Atributos
        # El cubo inicia por defecto con los valores de intensidad proporcionados por el fabricante para cada lambda
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

        self.pathblue, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")#, "Images (*.tiff *.tif)")
        self.lineEdit_blue.setText(self.pathblue)

        wc = self.pathblue[:-5] + '*' + self.pathblue[-4:]
        imageName = glob.glob(wc)

        for i, image in enumerate(imageName):
            blueMeta = metadata.Metadata(image, exiftoolPath=self.exiftoolPath)
            bandname = blueMeta.get_item("XMP:BandName")
            self.cube[bandname].append(get_panels(image))
            self.cube[bandname].append(get_params(blueMeta))

        print(f'{self.cube}')

        return

    def get_panel_red(self):

        self.pathred, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")#, "Images (*.tiff *.tif)")
        self.lineEdit_red.setText(self.pathred)
        
        wc = self.pathred[:-5] + '*' + self.pathred[-4:]
        imageName = glob.glob(wc)

        for i, image in enumerate(imageName):
            redMeta = metadata.Metadata(image, exiftoolPath=self.exiftoolPath)
            bandname = redMeta.get_item("XMP:BandName")
            self.cube[bandname].append(get_panels(image))
            self.cube[bandname].append(get_params(redMeta))
            
        print(f'{self.cube}')

        return

    def get_reflectance(self):

        # Factor de calibracion por banda
        F_lambda = get_F(self.cube)
        print(f'Factores de calibracion = {F_lambda}')

        V_lambda = get_V(self.cube)