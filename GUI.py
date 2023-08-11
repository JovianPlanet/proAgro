# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(471, 609)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 451, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/ITMLabels/img/new_itm_logo_rec_small.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.blue_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.blue_label.setFont(font)
        self.blue_label.setAlignment(QtCore.Qt.AlignCenter)
        self.blue_label.setObjectName("blue_label")
        self.verticalLayout_3.addWidget(self.blue_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_bluepanel = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_bluepanel.setInputMask("")
        self.lineEdit_bluepanel.setText("")
        self.lineEdit_bluepanel.setObjectName("lineEdit_bluepanel")
        self.horizontalLayout_2.addWidget(self.lineEdit_bluepanel)
        self.browse_bluepanel_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browse_bluepanel_button.setObjectName("browse_bluepanel_button")
        self.horizontalLayout_2.addWidget(self.browse_bluepanel_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_blueimg = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_blueimg.setObjectName("lineEdit_blueimg")
        self.horizontalLayout_5.addWidget(self.lineEdit_blueimg)
        self.browse_blueimg_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browse_blueimg_button.setObjectName("browse_blueimg_button")
        self.horizontalLayout_5.addWidget(self.browse_blueimg_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.blueok_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.blueok_label.setPalette(palette)
        self.blueok_label.setText("")
        self.blueok_label.setAlignment(QtCore.Qt.AlignCenter)
        self.blueok_label.setObjectName("blueok_label")
        self.verticalLayout_3.addWidget(self.blueok_label)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.red_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.red_label.setFont(font)
        self.red_label.setAlignment(QtCore.Qt.AlignCenter)
        self.red_label.setObjectName("red_label")
        self.verticalLayout_2.addWidget(self.red_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_redpanel = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_redpanel.setText("")
        self.lineEdit_redpanel.setMaxLength(32767)
        self.lineEdit_redpanel.setObjectName("lineEdit_redpanel")
        self.horizontalLayout.addWidget(self.lineEdit_redpanel)
        self.browse_redpanel_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browse_redpanel_button.setObjectName("browse_redpanel_button")
        self.horizontalLayout.addWidget(self.browse_redpanel_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_redimg = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_redimg.setInputMask("")
        self.lineEdit_redimg.setText("")
        self.lineEdit_redimg.setObjectName("lineEdit_redimg")
        self.horizontalLayout_6.addWidget(self.lineEdit_redimg)
        self.browse_redimg_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browse_redimg_button.setObjectName("browse_redimg_button")
        self.horizontalLayout_6.addWidget(self.browse_redimg_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.redok_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.redok_label.setText("")
        self.redok_label.setAlignment(QtCore.Qt.AlignCenter)
        self.redok_label.setObjectName("redok_label")
        self.verticalLayout_2.addWidget(self.redok_label)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.compute_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.compute_button.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.compute_button.setFont(font)
        self.compute_button.setObjectName("compute_button")
        self.horizontalLayout_3.addWidget(self.compute_button)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Micasense Dualsystem - Deteccion de panel"))
        self.label_4.setText(_translate("Form", "Detección de Paneles\n"
"para Cámara\n"
"MicaSense Dualsystem"))
        self.blue_label.setText(_translate("Form", "BLUE"))
        self.lineEdit_bluepanel.setPlaceholderText(_translate("Form", "Ingrese la ruta de panel BLUE..."))
        self.browse_bluepanel_button.setText(_translate("Form", "Panel"))
        self.lineEdit_blueimg.setPlaceholderText(_translate("Form", "Ingrese la ruta de la imagen BLUE..."))
        self.browse_blueimg_button.setText(_translate("Form", "Imagen"))
        self.red_label.setText(_translate("Form", "RED"))
        self.lineEdit_redpanel.setPlaceholderText(_translate("Form", "Ingrese la ruta del panel RED..."))
        self.browse_redpanel_button.setText(_translate("Form", "Panel"))
        self.lineEdit_redimg.setPlaceholderText(_translate("Form", "Ingrese la ruta de la imagen RED..."))
        self.browse_redimg_button.setText(_translate("Form", "Imagen"))
        self.compute_button.setText(_translate("Form", "Generar\n"
"TIFF"))
import resources_rc
