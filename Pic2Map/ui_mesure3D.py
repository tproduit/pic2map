# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U:\pic2map-master\pic2map-master\Pic2Map\ui\ui_mesure3D.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mesure3DDialog(object):
    def setupUi(self, Mesure3DDialog):
        Mesure3DDialog.setObjectName("Mesure3DDialog")
        Mesure3DDialog.resize(432, 239)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Mesure3DDialog.sizePolicy().hasHeightForWidth())
        Mesure3DDialog.setSizePolicy(sizePolicy)
        self.textBrowser_2 = QtWidgets.QTextBrowser(Mesure3DDialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(110, 180, 311, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser_2.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser = QtWidgets.QTextBrowser(Mesure3DDialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 30, 401, 137))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Mesure3DDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Mesure3DDialog)
        self.label_2.setGeometry(QtCore.QRect(60, 180, 41, 21))
        self.label_2.setObjectName("label_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(Mesure3DDialog)
        self.buttonBox.setGeometry(QtCore.QRect(340, 210, 75, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Mesure3DDialog)
        self.buttonBox.accepted.connect(Mesure3DDialog.accept)
        self.buttonBox.rejected.connect(Mesure3DDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Mesure3DDialog)

    def retranslateUi(self, Mesure3DDialog):
        _translate = QtCore.QCoreApplication.translate
        Mesure3DDialog.setWindowTitle(_translate("Mesure3DDialog", "Mesure 3D"))
        self.textBrowser_2.setHtml(_translate("Mesure3DDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("Mesure3DDialog", "Segments [mètres]"))
        self.label_2.setText(_translate("Mesure3DDialog", "Total:"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mesure3DDialog = QtWidgets.QDialog()
    ui = Ui_Mesure3DDialog()
    ui.setupUi(Mesure3DDialog)
    Mesure3DDialog.show()
    sys.exit(app.exec_())
