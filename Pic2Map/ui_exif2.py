# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U:\pic2map-master\pic2map-master\Pic2Map\ui\ui_exif2.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Exif2(object):
    def setupUi(self, Exif2):
        Exif2.setObjectName("Exif2")
        Exif2.resize(481, 570)
        self.buttonBox = QtWidgets.QDialogButtonBox(Exif2)
        self.buttonBox.setGeometry(QtCore.QRect(390, 540, 75, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textBrowser = QtWidgets.QTextBrowser(Exif2)
        self.textBrowser.setGeometry(QtCore.QRect(9, 9, 461, 301))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox = QtWidgets.QGroupBox(Exif2)
        self.groupBox.setGeometry(QtCore.QRect(10, 320, 461, 211))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lineDiagSensor = QtWidgets.QLineEdit(self.groupBox)
        self.lineDiagSensor.setObjectName("lineDiagSensor")
        self.gridLayout.addWidget(self.lineDiagSensor, 2, 0, 1, 1)
        self.textBrowserFocal = QtWidgets.QTextBrowser(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowserFocal.sizePolicy().hasHeightForWidth())
        self.textBrowserFocal.setSizePolicy(sizePolicy)
        self.textBrowserFocal.setObjectName("textBrowserFocal")
        self.gridLayout.addWidget(self.textBrowserFocal, 0, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.lineFocalPixel = QtWidgets.QLineEdit(self.groupBox)
        self.lineFocalPixel.setReadOnly(True)
        self.lineFocalPixel.setObjectName("lineFocalPixel")
        self.gridLayout.addWidget(self.lineFocalPixel, 2, 1, 1, 1)
        self.importXYButton = QtWidgets.QPushButton(Exif2)
        self.importXYButton.setEnabled(False)
        self.importXYButton.setGeometry(QtCore.QRect(20, 540, 111, 23))
        self.importXYButton.setObjectName("importXYButton")
        self.saveXYButton = QtWidgets.QPushButton(Exif2)
        self.saveXYButton.setEnabled(False)
        self.saveXYButton.setGeometry(QtCore.QRect(150, 540, 111, 23))
        self.saveXYButton.setObjectName("saveXYButton")

        self.retranslateUi(Exif2)
        self.buttonBox.accepted.connect(Exif2.accept)
        self.buttonBox.rejected.connect(Exif2.reject)
        QtCore.QMetaObject.connectSlotsByName(Exif2)

    def retranslateUi(self, Exif2):
        _translate = QtCore.QCoreApplication.translate
        Exif2.setWindowTitle(_translate("Exif2", "EXIF Information"))
        self.groupBox.setTitle(_translate("Exif2", "Focal"))
        self.textBrowserFocal.setHtml(_translate("Exif2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Part of the focal information is found in the EXIF File. You need to enter the size of the sensor diagonal in [mm]. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1. Check the website http://www.digicamdb.com/</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2. Find the diagonal length in [mm] of your sensor</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3. Enter it in the line below</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">4. Read the focal length on the right down line and use it in the pose estimation</span></p></body></html>"))
        self.pushButton.setText(_translate("Exif2", "Get Focal"))
        self.label.setText(_translate("Exif2", "Diagonal Length of Sensor [mm]"))
        self.label_2.setText(_translate("Exif2", "Focal [pixel unit]"))
        self.importXYButton.setText(_translate("Exif2", "Import Coordinate "))
        self.saveXYButton.setText(_translate("Exif2", "Save Coordinate "))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Exif2 = QtWidgets.QDialog()
    ui = Ui_Exif2()
    ui.setupUi(Exif2)
    Exif2.show()
    sys.exit(app.exec_())
