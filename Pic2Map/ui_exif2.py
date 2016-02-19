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

class Ui_Exif2(object):
    def setupUi(self, Exif2):
        Exif2.setObjectName(_fromUtf8("Exif2"))
        Exif2.resize(481, 570)
        self.buttonBox = QtGui.QDialogButtonBox(Exif2)
        self.buttonBox.setGeometry(QtCore.QRect(390, 540, 75, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.textBrowser = QtGui.QTextBrowser(Exif2)
        self.textBrowser.setGeometry(QtCore.QRect(9, 9, 461, 301))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.groupBox = QtGui.QGroupBox(Exif2)
        self.groupBox.setGeometry(QtCore.QRect(10, 320, 461, 211))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineDiagSensor = QtGui.QLineEdit(self.groupBox)
        self.lineDiagSensor.setObjectName(_fromUtf8("lineDiagSensor"))
        self.gridLayout.addWidget(self.lineDiagSensor, 2, 0, 1, 1)
        self.textBrowserFocal = QtGui.QTextBrowser(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowserFocal.sizePolicy().hasHeightForWidth())
        self.textBrowserFocal.setSizePolicy(sizePolicy)
        self.textBrowserFocal.setObjectName(_fromUtf8("textBrowserFocal"))
        self.gridLayout.addWidget(self.textBrowserFocal, 0, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.lineFocalPixel = QtGui.QLineEdit(self.groupBox)
        self.lineFocalPixel.setReadOnly(True)
        self.lineFocalPixel.setObjectName(_fromUtf8("lineFocalPixel"))
        self.gridLayout.addWidget(self.lineFocalPixel, 2, 1, 1, 1)

        self.retranslateUi(Exif2)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Exif2.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Exif2.reject)
        QtCore.QMetaObject.connectSlotsByName(Exif2)

    def retranslateUi(self, Exif2):
        Exif2.setWindowTitle(_translate("Exif2", "EXIF Information", None))
        self.groupBox.setTitle(_translate("Exif2", "Focal", None))
        self.textBrowserFocal.setHtml(_translate("Exif2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Part of the focal information is found in the EXIF File. You need to enter the size of the sensor diagonal in [mm]. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1. Check the website http://www.digicamdb.com/</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2. Find the diagonal length in [mm] of your sensor</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3. Enter it in the line below</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">4. Read the focal length on the right down line and use it in the pose estimation</span></p></body></html>", None))
        self.pushButton.setText(_translate("Exif2", "Get Focal", None))
        self.label.setText(_translate("Exif2", "Diagonal Length of Sensor [mm]", None))
        self.label_2.setText(_translate("Exif2", "Focal [pixel unit]", None))

