"""
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .ui_icons import Ui_iconsDialog
from functools import partial

class icons_dialog(QtWidgets.QDialog):
    def __init__(self, iconSet):
        QtWidgets.QDialog.__init__(self)
        self.uiIcons = Ui_iconsDialog()
        self.uiIcons.setupUi(self,iconSet)
        self.center()

        self.uiIcons.colorMButton.clicked.connect(partial(self.showColor, self.uiIcons.colorMButton))
        self.uiIcons.colorCButton.clicked.connect(partial(self.showColor, self.uiIcons.colorCButton))
                
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def showColor(self, frame):
        col = QtWidgets.QColorDialog.getColor()
        if col.isValid():
            frame.setStyleSheet("QWidget { background-color: %s }" % col.name())

    
