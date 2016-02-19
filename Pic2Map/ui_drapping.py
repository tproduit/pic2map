# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_drapping.ui'
#
# Created: Fri Apr 11 16:07:39 2014
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

class Ui_drapping(object):
    def setupUi(self, Ui_drapping):
        Ui_drapping.setObjectName(_fromUtf8("Ui_drapping"))
        Ui_drapping.resize(736, 630)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_drapping.sizePolicy().hasHeightForWidth())
        Ui_drapping.setSizePolicy(sizePolicy)
        Ui_drapping.setAnimated(False)
        Ui_drapping.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks)
        Ui_drapping.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(Ui_drapping)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        Ui_drapping.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Ui_drapping)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Ui_drapping.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Ui_drapping)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Ui_drapping.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(Ui_drapping)
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
        self.spinBox = QtGui.QSpinBox(self.dockWidgetContents)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setProperty("value", 10)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.verticalLayout.addWidget(self.spinBox)
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_7 = QtGui.QLabel(self.dockWidgetContents)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.frame = QtGui.QFrame(self.dockWidgetContents)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtGui.QFrame.Plain)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.saveButton = QtGui.QPushButton(self.dockWidgetContents)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.verticalLayout.addWidget(self.saveButton)
        spacerItem = QtGui.QSpacerItem(20, 260, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.dockWidget.setWidget(self.dockWidgetContents)
        Ui_drapping.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)

        self.retranslateUi(Ui_drapping)
        QtCore.QMetaObject.connectSlotsByName(Ui_drapping)

    def retranslateUi(self, Ui_drapping):
        Ui_drapping.setWindowTitle(_translate("Ui_drapping", "Drapping", None))
        self.label.setText(_translate("Ui_drapping", "Pixel size [m]", None))
        self.label_2.setText(_translate("Ui_drapping", "Bounding Box", None))
        self.label_5.setText(_translate("Ui_drapping", "TextLabel", None))
        self.label_4.setText(_translate("Ui_drapping", "TextLabel", None))
        self.label_3.setText(_translate("Ui_drapping", "TextLabel", None))
        self.label_6.setText(_translate("Ui_drapping", "TextLabel", None))
        self.label_7.setText(_translate("Ui_drapping", "Draw the bounding box \nfrom up-left to \ndown-right direction.", None))
        self.saveButton.setText(_translate("Ui_drapping", "Save raster", None))

