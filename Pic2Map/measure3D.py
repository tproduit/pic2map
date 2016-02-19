
 

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.core import *
from qgis.gui import *
from math import  sqrt
from ui_mesure3D import Ui_Mesure3D

class mesure3DDialog(QtGui.QDialog):
    closeSignal= pyqtSignal()
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # create the interface
        self.ui = Ui_Mesure3D()
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

        
                    