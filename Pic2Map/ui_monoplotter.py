# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_monoplotter.ui'
#
# Created: Wed May 14 14:45:19 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Monoplotter(object):
    def setupUi(self, Monoplotter, useOrthoImage):
        Monoplotter.setObjectName(_fromUtf8("Monoplotter"))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Monoplotter.sizePolicy().hasHeightForWidth())
        Monoplotter.setSizePolicy(sizePolicy)
        Monoplotter.setAnimated(False)
        Monoplotter.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks)
        Monoplotter.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(Monoplotter)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        Monoplotter.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Monoplotter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Monoplotter.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Monoplotter)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Monoplotter.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(Monoplotter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setFixedWidth(200)
        self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.spinBox = QtGui.QDoubleSpinBox(self.dockWidgetContents)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.setMaximum (2000)
        self.spinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.verticalLayout.addWidget(self.spinBox)
        
        #Measure 2D button
        self.measureButton = QtGui.QPushButton(self.dockWidgetContents)
        self.measureButton.setObjectName(_fromUtf8("measureButton"))
        self.verticalLayout.addWidget(self.measureButton)
        
        #Measure 3D button
        self.measure3D = QtGui.QPushButton(self.dockWidgetContents)
        self.measure3D.setObjectName(_fromUtf8("measure3D"))
        self.verticalLayout.addWidget(self.measure3D)
        
        #Orthorectification
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        
        #Save image button
        self.saveButton = QtGui.QPushButton(self.dockWidgetContents)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.verticalLayout.addWidget(self.saveButton)
        
        #Refresh button
        self.refreshButton = QtGui.QPushButton(self.dockWidgetContents)
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        self.verticalLayout.addWidget(self.refreshButton)
        
        #
        self.buttonLabel = QtGui.QPushButton(self.dockWidgetContents)
        self.buttonLabel.setObjectName(_fromUtf8("buttonLabel"))
        self.verticalLayout.addWidget(self.buttonLabel)
        
        #
        #self.activatePolygon = QtGui.QPushButton(self.dockWidgetContents)
        #self.activatePolygon.setObjectName(_fromUtf8("activatePolygon"))
        #self.verticalLayout.addWidget(self.activatePolygon)
        
        #Save XYZ button
        self.saveXYZmatrix = QtGui.QPushButton(self.dockWidgetContents)
        self.saveXYZmatrix.setObjectName(_fromUtf8("saveXYZmatrix"))
        self.verticalLayout.addWidget(self.saveXYZmatrix)
        
        #Interception angle and surface analysis button
        self.analysis = QtGui.QPushButton(self.dockWidgetContents)
        self.saveXYZmatrix.setObjectName(_fromUtf8("analysis"))
        self.verticalLayout.addWidget(self.analysis)
        
        #Footprint and mask
        self.footprint = QtGui.QPushButton(self.dockWidgetContents)
        self.footprint.setObjectName(_fromUtf8("footprint"))
        self.verticalLayout.addWidget(self.footprint)
        
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        if not useOrthoImage:
            self.label_2 = QtGui.QLabel(self.dockWidgetContents)
            self.label_2.setObjectName(_fromUtf8("label_2"))
            self.verticalLayout.addWidget(self.label_2)
            self.horizontalSlider = QtGui.QSlider(self.dockWidgetContents)
            self.horizontalSlider.setMaximum(2)
            self.horizontalSlider.setSingleStep(1)
            self.horizontalSlider.setPageStep(1)
            self.horizontalSlider.setValue(0)
            self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
            self.horizontalSlider.setTickPosition(QtGui.QSlider.TicksAbove)
            self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
            self.verticalLayout.addWidget(self.horizontalSlider)
            

        self.dockWidget.setWidget(self.dockWidgetContents)
        Monoplotter.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        
        self.measure3D.setCheckable(True)

        self.retranslateUi(Monoplotter, useOrthoImage)
        QtCore.QMetaObject.connectSlotsByName(Monoplotter)

    def retranslateUi(self, Monoplotter, useOrthoImage):
        Monoplotter.setWindowTitle(_translate("Monoplotter", "MainWindow", None))
        self.label.setText(_translate("Monoplotter", "Window Size:", None))
        self.measureButton.setText(_translate("Monoplotter", "Measure on plane", None))
        self.measure3D.setText(_translate("Monoplotter", "Measure 3D", None))
        self.pushButton.setText(_translate("Monoplotter", "Orthorectification", None))
        self.saveButton.setText(_translate("Monoplotter", "Save Image", None))
        self.refreshButton.setText(_translate("Monoplotter", "Refresh Layers", None))
        self.buttonLabel.setText(_translate("Monoplotter", "Labels Settings", None))
        #self.activatePolygon.setText(_translate("Monoplotter", "Enable Polygons", None))
        
        self.saveXYZmatrix.setText(_translate("Monoplotter", "Save XYZ matrix", None))#
        
        self.analysis.setText(_translate("Monoplotter", "Geometry analysis", None))
        
        self.footprint.setText(_translate("Monoplotter", "Footprint", None))
        
        if not useOrthoImage:
            self.label_2.setText(_translate("Monoplotter", "DEM transparency", None))

