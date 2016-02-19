# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_icons.ui'
#
# Created: Mon May 05 11:29:00 2014
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

class Ui_iconsDialog(object):
    def setupUi(self, iconsDialog,iconSet):
        iconsDialog.setObjectName(_fromUtf8("iconsDialog"))
        iconsDialog.resize(235, 270)
        self.gridLayout = QtGui.QGridLayout(iconsDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBoxCanvas = QtGui.QGroupBox(iconsDialog)
        self.groupBoxCanvas.setObjectName(_fromUtf8("groupBoxCanvas"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxCanvas)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.groupBoxCanvas)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.colorMButton = QtGui.QPushButton(self.groupBoxCanvas)
        self.colorMButton.setObjectName(_fromUtf8("colorMButton"))
        self.colorMButton.setStyleSheet("QWidget { background-color: %s }"
                % iconSet.colorM.name())
        self.gridLayout_2.addWidget(self.colorMButton, 0, 2, 1, 1)
        self.spinBoxSM = QtGui.QSpinBox(self.groupBoxCanvas)
        self.spinBoxSM.setObjectName(_fromUtf8("spinBoxSM"))
        self.spinBoxSM.setValue(iconSet.SM)
        self.gridLayout_2.addWidget(self.spinBoxSM, 0, 1, 1, 1)
        self.spinBoxWM = QtGui.QSpinBox(self.groupBoxCanvas)
        self.spinBoxWM.setObjectName(_fromUtf8("spinBoxWM"))
        self.spinBoxWM.setValue(iconSet.WM)
        self.gridLayout_2.addWidget(self.spinBoxWM, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBoxCanvas)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBoxCanvas, 0, 0, 1, 1)
        self.groupBoxMonoplot = QtGui.QGroupBox(iconsDialog)
        self.groupBoxMonoplot.setObjectName(_fromUtf8("groupBoxMonoplot"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBoxMonoplot)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.colorCButton = QtGui.QPushButton(self.groupBoxMonoplot)
        self.colorCButton.setObjectName(_fromUtf8("colorCButton"))
        self.colorCButton.setStyleSheet("QWidget { background-color: %s }"
                % iconSet.colorC.name())
        self.gridLayout_3.addWidget(self.colorCButton, 0, 2, 1, 1)
        self.spinBoxSC = QtGui.QSpinBox(self.groupBoxMonoplot)
        self.spinBoxSC.setObjectName(_fromUtf8("spinBoxSC"))
        self.spinBoxSC.setValue(iconSet.SC)
        self.gridLayout_3.addWidget(self.spinBoxSC, 0, 1, 1, 1)
        self.spinBoxWC = QtGui.QSpinBox(self.groupBoxMonoplot)
        self.spinBoxWC.setObjectName(_fromUtf8("spinBoxWC"))
        self.spinBoxWC.setValue(iconSet.WC)
        self.gridLayout_3.addWidget(self.spinBoxWC, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBoxMonoplot)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBoxMonoplot)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBoxMonoplot, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(iconsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(iconsDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.spinBoxS3d = QtGui.QSpinBox(self.groupBox)
        self.spinBoxS3d.setMaximum(1000)
        self.spinBoxS3d.setSingleStep(10)
        self.spinBoxS3d.setObjectName(_fromUtf8("spinBoxS3d"))
        self.gridLayout_4.addWidget(self.spinBoxS3d, 0, 1, 1, 1)
        self.spinBoxS3d.setValue(iconSet.S3d)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)

        self.retranslateUi(iconsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), iconsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), iconsDialog.reject)
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

