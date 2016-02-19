
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

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from ui_disp_ini import Ui_disp_ini
import webbrowser
import os

class Initialization_dialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_disp_ini()
        self.ui.setupUi(self)
        self.center()
        
        self.ui.lineEdit.setText("")
        self.ui.lineEditDEM.setText("")
        self.ui.checkBox.setChecked(False)
        self.ui.lineEdit_2.setText("") 
             
        openFile = self.ui.toolButton
        QtCore.QObject.connect(openFile, QtCore.SIGNAL('clicked()'),self.showDialog)
        openFile = self.ui.toolButtonDEM
        QtCore.QObject.connect(openFile, QtCore.SIGNAL('clicked()'),self.showDialogDEM)
        
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL('helpRequested()'),self.helpWindow)
        QtCore.QObject.connect(self.ui.checkBox, QtCore.SIGNAL('stateChanged(int)'),self.orthoActivate)
        
        QtCore.QObject.connect(self.ui.lineEditDEM, QtCore.SIGNAL("dropped"), self.dropEvent)
        self.openOrtho = self.ui.toolButton_2
        QtCore.QObject.connect(self.openOrtho, QtCore.SIGNAL('clicked()'),self.showDialogOrtho)
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
        name = os.path.realpath(__file__)
        name = name.rsplit('\\', 3)
        url = name[0]+str("/plugins/Pic2Map/help/build/html/index.html")
        url.replace("\\","/")
        webbrowser.open(url,new=2)
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def showDialogOrtho(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',self.currentPath)
        self.ui.lineEdit_2.setText(fname)
        if fname:
             self.currentPath = fname.rsplit("/",1)[0]
        
    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',self.currentPath)
        self.ui.lineEdit.setText(fname)
        if fname:
             self.currentPath = fname.rsplit("/",1)[0]
        
    def showDialogDEM(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',self.currentPath, "Images (*.tiff *.tif)")
        self.ui.lineEditDEM.setText(fname)
        if fname:
             self.currentPath = fname.rsplit("/",1)[0]