# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U:\pic2map-master\pic2map-master\Pic2Map\ui\ui_label_settings.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
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

class Ui_LabelSetting(object):
    def setupUi(self, LabelSetting, labelSet):
        LabelSetting.setObjectName("LabelSetting")
        LabelSetting.resize(174, 204)
        self.gridLayout = QtWidgets.QGridLayout(LabelSetting)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(LabelSetting)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.colorButton = QtWidgets.QPushButton(LabelSetting)
        self.colorButton.setText("")
        self.colorButton.setObjectName("colorButton")
        self.colorButton.setStyleSheet("QWidget { background-color: %s }" % labelSet[0].name())
        self.gridLayout.addWidget(self.colorButton, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(LabelSetting)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(LabelSetting)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(LabelSetting)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 2, 1, 1, 1)
        self.doubleSpinBox.setMinimum(-100)
        self.doubleSpinBox.setMaximum(100)
        self.label_4 = QtWidgets.QLabel(LabelSetting)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(LabelSetting)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 3, 1, 1, 1)
        self.doubleSpinBox_2.setMinimum(-100)
        self.doubleSpinBox_2.setMaximum(100)
        self.buttonBox = QtWidgets.QDialogButtonBox(LabelSetting)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)
        self.fontButton = QtWidgets.QPushButton(LabelSetting)
        self.fontButton.setObjectName("fontButton")
        self.gridLayout.addWidget(self.fontButton, 1, 1, 1, 1)

        self.retranslateUi(LabelSetting)
        self.buttonBox.accepted.connect(LabelSetting.accept)
        self.buttonBox.rejected.connect(LabelSetting.reject)
        QtCore.QMetaObject.connectSlotsByName(LabelSetting)

    def retranslateUi(self, LabelSetting):
        LabelSetting.setWindowTitle(_translate("LabelSetting", "Label Settings", None))
        self.label.setText(_translate("LabelSetting", "Color", None))
        self.label_2.setText(_translate("LabelSetting", "Font", None))
        self.label_3.setText(_translate("LabelSetting", "offset X", None))
        self.label_4.setText(_translate("LabelSetting", "offset Y", None))
        self.fontButton.setText(_translate("LabelSetting", "Set Font", None))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabelSetting = QtWidgets.QDialog()
    ui = Ui_LabelSetting()
    ui.setupUi(LabelSetting)
    LabelSetting.show()
    sys.exit(app.exec_())
