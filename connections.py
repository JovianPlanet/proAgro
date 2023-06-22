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


class GuiConnections(QtWidgets.QMainWindow, GUI.Ui_Form):

    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pathblue = ''
        self.pathred = ''

        # Conexiones
        self.browse_blue_button.clicked.connect(self.get_panel_blue)
        self.browse_red_button.clicked.connect(self.get_panel_red)
        self.search_button.clicked.connect(self.find_panels)

        # Atributos
        self.cube = {'Blue-444'    : [], 'Blue'    : [], 
                     'Green-531'   : [], 'Green'   : [], 
                     'Red-650'     : [], 'Red'     : [], 
                     'Red edge-705': [], 'NIR'     : [], 
                     'Red edge-740': [], 'Red Edge': []
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

    def find_panels(self):

        if self.manual_cb.isChecked():
            r = draw_panel(self.path)
            print(f'{r}')