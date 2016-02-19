# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_reportDialog.ui'
#
# Created: Mon May 19 17:15:41 2014
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

class Ui_ReportGCP(object):
    def setupUi(self, ReportGCP):
        ReportGCP.setObjectName(_fromUtf8("ReportGCP"))
        ReportGCP.resize(382, 277)
        self.gridLayout = QtGui.QGridLayout(ReportGCP)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.reportBrowser = QtGui.QTextBrowser(ReportGCP)
        self.reportBrowser.setObjectName(_fromUtf8("reportBrowser"))
        self.gridLayout.addWidget(self.reportBrowser, 0, 0, 1, 2)
        self.saveButton = QtGui.QPushButton(ReportGCP)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.gridLayout.addWidget(self.saveButton, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ReportGCP)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.retranslateUi(ReportGCP)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ReportGCP.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ReportGCP.reject)
        QtCore.QMetaObject.connectSlotsByName(ReportGCP)

    def retranslateUi(self, ReportGCP):
        ReportGCP.setWindowTitle(_translate("ReportGCP", "Dialog", None))
        self.saveButton.setText(_translate("ReportGCP", "Save Report", None))

