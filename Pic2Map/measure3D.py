
from builtins import str
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from qgis.core import *
from qgis.gui import *
from math import  sqrt
from .ui_mesure3D import Ui_Mesure3DDialog

class mesure3DDialog(QtWidgets.QDialog):
    closeSignal= pyqtSignal()
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        # create the interface
        self.ui = Ui_Mesure3DDialog()
        self.ui.setupUi(self)
        #self.path contains the path in picture coordinates. It is only used for drawing
        self.path = []
        #self.total contains the total length of the path in meter (3D distance)
        self.total = 0
        
    def closeEvent(self, event):
        # toggle the button when the window is closed
        self.closeSignal.emit()
        
    def addPoint(self,x,y):
        #Add a point to the path
        self.path.append([x,y])
        if len(self.path)>1:
            x = self.path[-2][0]-self.path[-1][0]
            y = self.path[-2][1]-self.path[-1][1]
            distance = round(sqrt(x**2+y**2),2)
            self.ui.textBrowser.append(str(distance))
            self.total += distance
        self.ui.textBrowser_2.setText(str(self.total))
        
    def removePath(self):
        # Clear the measurement buffer and the window
        self.path = []
        self.total = 0
        self.ui.textBrowser.clear()
        self.ui.textBrowser_2.clear()

        
                    
