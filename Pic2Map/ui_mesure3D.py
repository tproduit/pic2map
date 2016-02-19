# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mesure3D.ui'
#
# Created: Wed May 14 15:05:24 2014
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

class Ui_Mesure3D(object):
    def setupUi(self, Mesure3D):
        Mesure3D.setObjectName(_fromUtf8("Mesure3D"))
        Mesure3D.resize(432, 239)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Mesure3D.sizePolicy().hasHeightForWidth())
        Mesure3D.setSizePolicy(sizePolicy)
        self.textBrowser_2 = QtGui.QTextBrowser(Mesure3D)
        self.textBrowser_2.setGeometry(QtCore.QRect(110, 180, 311, 25))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.textBrowser_2.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.textBrowser = QtGui.QTextBrowser(Mesure3D)
        self.textBrowser.setGeometry(QtCore.QRect(20, 30, 401, 137))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label = QtGui.QLabel(Mesure3D)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Mesure3D)
        self.label_2.setGeometry(QtCore.QRect(60, 180, 41, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.buttonBox = QtGui.QDialogButtonBox(Mesure3D)
        self.buttonBox.setGeometry(QtCore.QRect(340, 210, 75, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(Mesure3D)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Mesure3D.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Mesure3D.reject)
        QtCore.QMetaObject.connectSlotsByName(Mesure3D)

    def retranslateUi(self, Mesure3D):
        Mesure3D.setWindowTitle(_translate("Mesure3D", "Mesure 3D", None))
        self.textBrowser_2.setHtml(_translate("Mesure3D", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.label.setText(_translate("Mesure3D", "Segments [meters]", None))
        self.label_2.setText(_translate("Mesure3D", "Total:", None))

