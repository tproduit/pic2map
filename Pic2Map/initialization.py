
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
import os, tempfile
from osgeo import gdal

class Initialization_dialog(QtWidgets.QDialog):
    def __init__(self, iface):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.center()
        self.iface = iface
        self.ui.lineEdit.setText("")
        self.ui.lineEditDEM.setText("")
        #self.ui.checkBox.setChecked(False)
        #self.ui.lineEdit_2.setText("") 
        self.activeLayer = False
        self.filePathSave = os.path.dirname(os.path.abspath(__file__)) + "/config.txt"
             
        openFile = self.ui.toolButton
        openFile.clicked.connect(self.showDialog)
        openFile = self.ui.toolButtonDEM
        openFile.clicked.connect(self.showDialogDEM)
        self.ui.pushButtonDEM.clicked.connect(self.getActiveLayer)
        self.ui.pushButtonCurrent.clicked.connect(self.getCurrentView)
        
        self.ui.buttonBox.helpRequested.connect(self.helpWindow)
        #self.ui.checkBox.stateChanged[int].connect(self.orthoActivate)
        
        self.ui.lineEditDEM.dropped.connect(self.dropEvent)
        #self.openOrtho = self.ui.toolButton_2
        #self.openOrtho.clicked.connect(self.showDialogOrtho)
        #self.ui.lineEdit_2.setReadOnly(True)
        
        try : 
            projectName = QgsProject.instance().fileName()
            f = open(self.filePathSave, "r")
            oldpath = f.readline()
            if oldpath :
                self.currentPath = oldpath
            elif projectName :
                self.currentPath = os.path.dirname(projectName)
            else :
                self.currentPath = '/home'
            f.close()
        except : 
            self.currentPath = '/home'

        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, event):
        event.accept()
        
    def dropEvent(self, event):
        lineEdit =  self.childAt(event.pos().x(),event.pos().y())
        
        if lineEdit.metaObject().className() == "dropedit" :
            fileURL = event.mimeData().urls()[0].toString()
            try :
                fileName = fileURL.split('file:///')[1]
            except :
                fileName = fileURL.split('file:')[1]
            lineEdit.setText(fileName)
        
    """def orthoActivate(self, state):
        if state == 2:
            self.openOrtho.setEnabled(True)
        if state == 0:
            self.openOrtho.setEnabled(False)
            self.ui.lineEdit_2.setText('')"""
        
        
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
    
    """def showDialogOrtho(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',self.currentPath)[0]
        self.ui.lineEdit_2.setText(fname)
        if fname:
             self.currentPath = fname.rsplit("/",1)[0]"""
        
    def showDialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',self.currentPath)[0]
        if fname:
            self.ui.lineEdit.setText(fname)
            self.currentPath = fname.rsplit("/",1)[0]
            f = open(self.filePathSave, "w+")
            f.write(self.currentPath)
            f.close()
        
    def showDialogDEM(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',self.currentPath, "Images (*.tiff *.tif)")[0]
        if fname:
            self.activeLayer = False
            self.ui.lineEditDEM.setText(fname)
            self.currentPath = fname.rsplit("/",1)[0]
            f = open(self.filePathSave, "w+")
            f.write(self.currentPath)
            f.close()

    def getActiveLayer(self):

        if str(type(self.iface.activeLayer())) != "<class 'qgis._core.QgsRasterLayer'>" :
            QMessageBox.warning(self, "Layer type invalid", "Please select a Qgs Raster Layer")
            
        else:
            fname = self.iface.activeLayer().dataProvider().dataSourceUri()
            self.ui.lineEditDEM.setText(fname)
            self.currentPath = fname.rsplit("/",1)[0]
            f = open(self.filePathSave, "w+")
            f.write(self.currentPath)
            f.close()
            self.activeLayer = True
    
    def getCurrentView(self):
        rect = self.iface.mapCanvas().extent()
        proj = [rect.xMinimum(), rect.yMaximum(), rect.xMaximum(), rect.yMinimum()]
        if str(type(self.iface.activeLayer())) != "<class 'qgis._core.QgsRasterLayer'>" :
                QMessageBox.warning(self, "Layer type invalid", "Please select a Qgs Raster Layer")
        
        else:    
            fname = self.iface.activeLayer().dataProvider().dataSourceUri()
            self.currentPath = fname.rsplit("/",1)[0]
            path = tempfile.gettempdir().replace("\\","/")
            outName =  path + '/' + (fname.rsplit("/",1)[1]).split(".")[0] + "_CropToView.vrt"      
            f = open(self.filePathSave, "w+")
            f.write(self.currentPath)
            f.close()

            activeLayer = self.iface.activeLayer()
            self.iface.layerTreeView().layerTreeModel().rootGroup().findLayer(activeLayer).setItemVisibilityChecked(False)

            gdal.Translate(outName, fname, projWin=proj)

            self.ui.lineEditDEM.setText(outName)
            self.iface.addRasterLayer(outName)
            self.activeLayer = True


