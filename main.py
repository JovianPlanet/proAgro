#-*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import sys
import connections


def main():

    app = QtWidgets.QApplication(sys.argv)
    form = connections.GuiConnections()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':

    main()