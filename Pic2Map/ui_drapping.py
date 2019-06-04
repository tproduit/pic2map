# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U:\pic2map-master\pic2map-master\Pic2Map\ui\ui_drapping.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_drapping(object):
    def setupUi(self, Ui_drapping):
        Ui_drapping.setObjectName("Ui_drapping")
        Ui_drapping.resize(736, 630)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_drapping.sizePolicy().hasHeightForWidth())
        Ui_drapping.setSizePolicy(sizePolicy)
        Ui_drapping.setAnimated(False)
        Ui_drapping.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks)
        Ui_drapping.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(Ui_drapping)
        self.centralwidget.setObjectName("centralwidget")
        Ui_drapping.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_drapping)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 21))
        self.menubar.setObjectName("menubar")
        Ui_drapping.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ui_drapping)
        self.statusbar.setObjectName("statusbar")
        Ui_drapping.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(Ui_drapping)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
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
        self.spinBox = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setProperty("value", 10)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.spinBox)
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.frame = QtWidgets.QFrame(self.dockWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.saveButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)
        spacerItem = QtWidgets.QSpacerItem(20, 260, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.dockWidget.setWidget(self.dockWidgetContents)
        Ui_drapping.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)

        self.retranslateUi(Ui_drapping)
        QtCore.QMetaObject.connectSlotsByName(Ui_drapping)

    def retranslateUi(self, Ui_drapping):
        _translate = QtCore.QCoreApplication.translate
        Ui_drapping.setWindowTitle(_translate("Ui_drapping", "MainWindow"))
        self.label.setText(_translate("Ui_drapping", "Pixel size [m]"))
        self.label_2.setText(_translate("Ui_drapping", "Bounding Box"))
        self.label_5.setText(_translate("Ui_drapping", "TextLabel"))
        self.label_4.setText(_translate("Ui_drapping", "TextLabel"))
        self.label_3.setText(_translate("Ui_drapping", "TextLabel"))
        self.label_6.setText(_translate("Ui_drapping", "TextLabel"))
        self.saveButton.setText(_translate("Ui_drapping", "Save raster"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_drapping = QtWidgets.QMainWindow()
    ui = Ui_drapping()
    ui.setupUi(Ui_drapping)
    Ui_drapping.show()
    sys.exit(app.exec_())
