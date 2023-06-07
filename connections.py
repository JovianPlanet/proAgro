import os
import glob
import nibabel as nib
import numpy as np
from PyQt5 import QtWidgets, QtCore
#from popups import ErrorDialog
import GUI

from panel_detection.manual import draw_panel
from panel_detection.process_img import get_panels


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
        self.panels_blue = {'Blue444': [], 'Green531': [], 'Red650': [], 'RedEdge705': [], 'RedEdge740': []}
        self.bkeys = list(self.panels_blue.keys())
        self.panels_red = {'Blue': [], 'Green': [], 'Red': [], 'NIR': [], 'RedEdge': []}
        self.rkeys = list(self.panels_red.keys())


    # Metodo que captura la ruta donde se encuentra la imagen
    def get_panel_blue(self):

        self.pathblue, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "Images (*.tiff *.tif)")
        self.lineEdit_blue.setText(self.pathblue)

        wc = self.pathblue[:-5] + '*' + self.pathblue[-4:]
        imageName = glob.glob(wc)

        for i, image in enumerate(imageName):
            self.panels_blue[self.bkeys[i]] = get_panels(image)
            print(f'Intensidad de la banda {self.bkeys[i]}, sufijo ({i+1}) = {self.panels_blue[self.bkeys[i]]}')

        return

    def get_panel_red(self):

        self.pathred, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "Images (*.tiff *.tif)")
        self.lineEdit_red.setText(self.pathred)
        wc = self.pathred[:-5] + '*' + self.pathred[-4:]
        imageName = glob.glob(wc)

        for i, image in enumerate(imageName):
            self.panels_red[self.rkeys[i]] = get_panels(image)
            print(f'Intensidad de la banda {self.rkeys[i]}, sufijo ({i+1}) = {self.panels_red[self.rkeys[i]]}')

        return

    def find_panels(self):

        if self.manual_cb.isChecked():
            r = draw_panel(self.path)
            print(f'{r}')