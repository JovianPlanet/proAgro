#-*- coding: utf-8 -*-
import os
import sys
from PyQt5 import QtWidgets
import connections


def main():

    app = QtWidgets.QApplication(sys.argv)
    form = connections.GuiConnections()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':

    # os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")
    main()