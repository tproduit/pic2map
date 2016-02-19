# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_label_settings.ui'
#
# Created: Thu May 01 17:30:56 2014
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

class Ui_LabelSetting(object):
    def setupUi(self, LabelSetting, labelSet):
        LabelSetting.setObjectName(_fromUtf8("LabelSetting"))
        LabelSetting.resize(174, 204)
        self.gridLayout = QtGui.QGridLayout(LabelSetting)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(LabelSetting)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.colorButton = QtGui.QPushButton(LabelSetting)
        self.colorButton.setText(_fromUtf8(""))
        self.colorButton.setObjectName(_fromUtf8("colorButton"))
        self.colorButton.setStyleSheet("QWidget { background-color: %s }"
                % labelSet[0].name())
        self.gridLayout.addWidget(self.colorButton, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(LabelSetting)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(LabelSetting)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(LabelSetting)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.gridLayout.addWidget(self.doubleSpinBox, 2, 1, 1, 1)
        self.doubleSpinBox.setMinimum(-100)
        self.doubleSpinBox.setMaximum(100)
        self.label_4 = QtGui.QLabel(LabelSetting)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(LabelSetting)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.gridLayout.addWidget(self.doubleSpinBox_2, 3, 1, 1, 1)
        self.doubleSpinBox_2.setMinimum(-100)
        self.doubleSpinBox_2.setMaximum(100)
        self.buttonBox = QtGui.QDialogButtonBox(LabelSetting)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)
        self.fontButton = QtGui.QPushButton(LabelSetting)
        self.fontButton.setObjectName(_fromUtf8("fontButton"))
        self.gridLayout.addWidget(self.fontButton, 1, 1, 1, 1)

        self.retranslateUi(LabelSetting)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), LabelSetting.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), LabelSetting.reject)
        QtCore.QMetaObject.connectSlotsByName(LabelSetting)

    def retranslateUi(self, LabelSetting):
        LabelSetting.setWindowTitle(_translate("LabelSetting", "Label Settings", None))
        self.label.setText(_translate("LabelSetting", "Color", None))
        self.label_2.setText(_translate("LabelSetting", "Font", None))
        self.label_3.setText(_translate("LabelSetting", "offset X", None))
        self.label_4.setText(_translate("LabelSetting", "offset Y", None))
        self.fontButton.setText(_translate("LabelSetting", "Set Font", None))

