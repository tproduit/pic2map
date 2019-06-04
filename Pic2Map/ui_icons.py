# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U:\pic2map-master\pic2map-master\Pic2Map\ui\ui_icons.ui'
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

class Ui_iconsDialog(object):
    def setupUi(self, iconsDialog,iconSet):
        iconsDialog.setObjectName("iconsDialog")
        iconsDialog.resize(235, 270)
        self.gridLayout = QtWidgets.QGridLayout(iconsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBoxCanvas = QtWidgets.QGroupBox(iconsDialog)
        self.groupBoxCanvas.setObjectName("groupBoxCanvas")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxCanvas)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBoxCanvas)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.colorMButton = QtWidgets.QPushButton(self.groupBoxCanvas)
        self.colorMButton.setObjectName("colorMButton")
        self.colorMButton.setStyleSheet("QWidget { background-color: %s }" % iconSet.colorM.name())
        self.gridLayout_2.addWidget(self.colorMButton, 0, 2, 1, 1)
        self.spinBoxSM = QtWidgets.QSpinBox(self.groupBoxCanvas)
        self.spinBoxSM.setObjectName("spinBoxSM")
        self.spinBoxSM.setValue(iconSet.SM)
        self.gridLayout_2.addWidget(self.spinBoxSM, 0, 1, 1, 1)
        self.spinBoxWM = QtWidgets.QSpinBox(self.groupBoxCanvas)
        self.spinBoxWM.setObjectName("spinBoxWM")
        self.spinBoxWM.setValue(iconSet.WM)
        self.gridLayout_2.addWidget(self.spinBoxWM, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBoxCanvas)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBoxCanvas, 0, 0, 1, 1)
        self.groupBoxMonoplot = QtWidgets.QGroupBox(iconsDialog)
        self.groupBoxMonoplot.setObjectName("groupBoxMonoplot")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxMonoplot)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.colorCButton = QtWidgets.QPushButton(self.groupBoxMonoplot)
        self.colorCButton.setObjectName("colorCButton")
        self.colorCButton.setStyleSheet("QWidget { background-color: %s }" % iconSet.colorC.name())
        self.gridLayout_3.addWidget(self.colorCButton, 0, 2, 1, 1)
        self.spinBoxSC = QtWidgets.QSpinBox(self.groupBoxMonoplot)
        self.spinBoxSC.setObjectName("spinBoxSC")
        self.spinBoxSC.setValue(iconSet.SC)
        self.gridLayout_3.addWidget(self.spinBoxSC, 0, 1, 1, 1)
        self.spinBoxWC = QtWidgets.QSpinBox(self.groupBoxMonoplot)
        self.spinBoxWC.setObjectName("spinBoxWC")
        self.spinBoxWC.setValue(iconSet.WC)
        self.gridLayout_3.addWidget(self.spinBoxWC, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBoxMonoplot)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBoxMonoplot)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBoxMonoplot, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(iconsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(iconsDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.spinBoxS3d = QtWidgets.QSpinBox(self.groupBox)
        self.spinBoxS3d.setMaximum(1000)
        self.spinBoxS3d.setSingleStep(10)
        self.spinBoxS3d.setObjectName("spinBoxS3d")
        self.gridLayout_4.addWidget(self.spinBoxS3d, 0, 1, 1, 1)
        self.spinBoxS3d.setValue(iconSet.S3d)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)

        self.retranslateUi(iconsDialog)
        self.buttonBox.accepted.connect(iconsDialog.accept)
        self.buttonBox.rejected.connect(iconsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(iconsDialog)

    def retranslateUi(self, iconsDialog):
        iconsDialog.setWindowTitle(_translate("iconsDialog", "Icon settings", None))
        self.groupBoxCanvas.setTitle(_translate("iconsDialog", "GCP in Monoplotter", None))
        self.label.setText(_translate("iconsDialog", "Size of Icons", None))
        self.colorMButton.setText(_translate("iconsDialog", "Color", None))
        self.label_2.setText(_translate("iconsDialog", "Width of Lines", None))
        self.groupBoxMonoplot.setTitle(_translate("iconsDialog", "GCP in Canvas", None))
        self.colorCButton.setText(_translate("iconsDialog", "Color", None))
        self.label_5.setText(_translate("iconsDialog", "Size of Icons", None))
        self.label_6.setText(_translate("iconsDialog", "Width of Lines", None))
        self.groupBox.setTitle(_translate("iconsDialog", "GCP in 3D viewer", None))
        self.label_3.setText(_translate("iconsDialog", "Size of cube", None))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    iconsDialog = QtWidgets.QDialog()
    ui = Ui_iconsDialog()
    ui.setupUi(iconsDialog)
    iconsDialog.show()
    sys.exit(app.exec_())
