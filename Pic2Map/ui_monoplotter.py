# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_monoplotter.ui'
#
# Created: Wed May 14 14:45:19 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)

class Ui_Monoplotter(object):
    def setupUi(self, Monoplotter, useOrthoImage):
        Monoplotter.setObjectName("Monoplotter")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Monoplotter.sizePolicy().hasHeightForWidth())
        Monoplotter.setSizePolicy(sizePolicy)
        Monoplotter.setAnimated(False)
        Monoplotter.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks)
        Monoplotter.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(Monoplotter)
        self.centralwidget.setObjectName("centralwidget")
        Monoplotter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Monoplotter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 21))
        self.menubar.setObjectName("menubar")
        Monoplotter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Monoplotter)
        self.statusbar.setObjectName("statusbar")
        Monoplotter.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(Monoplotter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setFixedWidth(200)
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QDoubleSpinBox(self.dockWidgetContents)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum (4096)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.verticalLayout.addWidget(self.spinBox)
        
        #Measure 2D button
        self.measureButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.measureButton.setObjectName("measureButton")
        self.verticalLayout.addWidget(self.measureButton)
        
        #Measure 3D button
        self.measure3D = QtWidgets.QPushButton(self.dockWidgetContents)
        self.measure3D.setObjectName("measure3D")
        self.verticalLayout.addWidget(self.measure3D)
        
        #Orthorectification
        self.pushButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        
        #Save image button
        self.saveButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)
        
        #Refresh button
        self.refreshButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.refreshButton.setObjectName("refreshButton")
        self.verticalLayout.addWidget(self.refreshButton)
        
        #
        self.buttonLabel = QtWidgets.QPushButton(self.dockWidgetContents)
        self.buttonLabel.setObjectName("buttonLabel")
        self.verticalLayout.addWidget(self.buttonLabel)
        
        #
        #self.activatePolygon = QtGui.QPushButton(self.dockWidgetContents)
        #self.activatePolygon.setObjectName(_fromUtf8("activatePolygon"))
        #self.verticalLayout.addWidget(self.activatePolygon)
        
        #Save XYZ button
        self.saveXYZmatrix = QtWidgets.QPushButton(self.dockWidgetContents)
        self.saveXYZmatrix.setObjectName("saveXYZmatrix")
        self.verticalLayout.addWidget(self.saveXYZmatrix)
        
        #Interception angle and surface analysis button
        self.analysis = QtWidgets.QPushButton(self.dockWidgetContents)
        self.saveXYZmatrix.setObjectName("analysis")
        self.verticalLayout.addWidget(self.analysis)
        
        #Footprint and mask
        self.footprint = QtWidgets.QPushButton(self.dockWidgetContents)
        self.footprint.setObjectName("footprint")
        self.verticalLayout.addWidget(self.footprint)

        self.simplifyFootprint = QtWidgets.QCheckBox(self.dockWidgetContents)
        self.simplifyFootprint.setObjectName("simplifyFootprint")
        self.simplifyFootprint.setText("Simplify footprint")
        self.simplifyFootprint.setCheckable(True)
        self.simplifyFootprint.setChecked(False)
        self.verticalLayout.addWidget(self.simplifyFootprint)

        self.retour = QtWidgets.QPushButton(self.dockWidgetContents)
        self.retour.setObjectName("retour")
        self.verticalLayout.insertSpacing(-1, 30)
        self.verticalLayout.addWidget(self.retour)
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        
        self.groupBoxColor = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.groupBoxColor.setGeometry(QtCore.QRect(20, 550, 161, 51))
        self.groupBoxColor.setObjectName("groupBoxColor")
        self.widgetWhite = QtWidgets.QWidget(self.groupBoxColor)
        self.widgetWhite.setGeometry(QtCore.QRect(10, 25, 21, 21))
        self.widgetWhite.setStyleSheet("background-color : rgba(255, 255, 255, 100);")
        self.widgetWhite.setObjectName("widgetWhite")
        self.widgetRed = QtWidgets.QWidget(self.groupBoxColor)
        self.widgetRed.setGeometry(QtCore.QRect(40, 25, 21, 21))
        self.widgetRed.setStyleSheet("background-color : rgba(255, 0, 0, 255);")
        self.widgetRed.setObjectName("widgetRed")
        self.widgetYellow = QtWidgets.QWidget(self.groupBoxColor)
        self.widgetYellow.setGeometry(QtCore.QRect(70, 25, 21, 21))
        self.widgetYellow.setStyleSheet("background-color : rgba(255, 255, 0, 255);")
        self.widgetYellow.setObjectName("widgetYellow")
        self.widgetGreen = QtWidgets.QWidget(self.groupBoxColor)
        self.widgetGreen.setGeometry(QtCore.QRect(100, 25, 21, 21))
        self.widgetGreen.setStyleSheet("background-color: rgba(0, 255, 0, 255);")
        self.widgetGreen.setObjectName("widgetGreen")
        self.widgetCyan = QtWidgets.QWidget(self.groupBoxColor)
        self.widgetCyan.setGeometry(QtCore.QRect(130, 25, 21, 21))
        self.widgetCyan.setStyleSheet("background-color : rgba(0, 255, 255, 255);")
        self.widgetCyan.setObjectName("widgetCyan")
        
        if not useOrthoImage:
            self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
            self.label_2.setObjectName("label_2")
            self.verticalLayout.addWidget(self.label_2)
            self.horizontalSlider = QtWidgets.QSlider(self.dockWidgetContents)
            self.horizontalSlider.setMaximum(5)
            self.horizontalSlider.setSingleStep(1)
            self.horizontalSlider.setPageStep(1)
            self.horizontalSlider.setValue(0)
            self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
            self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
            self.horizontalSlider.setObjectName("horizontalSlider")
            self.verticalLayout.addWidget(self.horizontalSlider)
            

        
        
        
        self.dockWidget.setWidget(self.dockWidgetContents)
        Monoplotter.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        
        self.measure3D.setCheckable(True)

        self.retranslateUi(Monoplotter, useOrthoImage)
        QtCore.QMetaObject.connectSlotsByName(Monoplotter)

    def retranslateUi(self, Monoplotter, useOrthoImage):
        Monoplotter.setWindowTitle(_translate("Monoplotter", "Monoplotter", None))
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
        
        self.footprint.setText(_translate("Monoplotter", "Compute footprint", None))
        self.retour.setText(_translate("Monoplotter", "Back to GCPWindow", None))
        self.groupBoxColor.setTitle(_translate("Monoplotter", "DEM Color", None))
        
        if not useOrthoImage:
            self.label_2.setText(_translate("Monoplotter", "DEM transparency", None))

