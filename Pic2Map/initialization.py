
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

from builtins import str
import qgis.core
from qgis.core import *
from qgis.gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .ui_disp_ini import Ui_Dialog
import webbrowser
import os

class Initialization_dialog(QtWidgets.QDialog):
    def __init__(self, iface):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.center()
        self.iface = iface
        self.ui.lineEdit.setText("")
        self.ui.lineEditDEM.setText("")
        self.ui.checkBox.setChecked(False)
        self.ui.lineEdit_2.setText("") 
        self.activeLayer = False
             
        openFile = self.ui.toolButton
        openFile.clicked.connect(self.showDialog)
        openFile = self.ui.toolButtonDEM
        openFile.clicked.connect(self.showDialogDEM)
        self.ui.pushButtonDEM.clicked.connect(self.getActiveLayer)
        
        self.ui.buttonBox.helpRequested.connect(self.helpWindow)
        self.ui.checkBox.stateChanged[int].connect(self.orthoActivate)
        
        self.ui.lineEditDEM.dropped.connect(self.dropEvent)
        self.openOrtho = self.ui.toolButton_2
        self.openOrtho.clicked.connect(self.showDialogOrtho)
        self.ui.lineEdit_2.setReadOnly(True)
        self.currentPath = '/home'
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, event):
        event.accept()
        
    def dropEvent(self, event):
        lineEdit =  self.childAt(event.pos().x(),event.pos().y());
        fileURL = event.mimeData().urls()[0].toString()
        fileName = fileURL.split('file:///')[1]
        lineEdit.setText(fileName)
        
    def orthoActivate(self, state):
        if state == 2:
            self.openOrtho.setEnabled(True)
        if state == 0:
            self.openOrtho.setEnabled(False)
            self.ui.lineEdit_2.setText('')
        
        
    def helpWindow(self):
        name = os.path.dirname(os.path.abspath(__file__))
        url = name + "/help/build/html/index.html"
        url.replace("\\","/")
        webbrowser.open(url,new=2)
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def showDialogOrtho(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',self.currentPath)[0]
        self.ui.lineEdit_2.setText(fname)
        if fname:
             self.currentPath = fname.rsplit("/",1)[0]
        
    def showDialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',self.currentPath)[0]
        self.ui.lineEdit.setText(fname)
        if fname:
             self.currentPath = fname.rsplit("/",1)[0]
        
    def showDialogDEM(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',self.currentPath, "Images (*.tiff *.tif)")[0]
        self.ui.lineEditDEM.setText(fname)
        if fname:
             self.currentPath = fname.rsplit("/",1)[0]

    def getActiveLayer(self):
        try :
            fname = self.iface.activeLayer().dataProvider().dataSourceUri()
        except :
            return
        self.ui.lineEditDEM.setText(fname)
        self.currentPath = fname.rsplit("/",1)[0]
        self.activeLayer = True
