# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U:\pic2map-master\pic2map-master\Pic2Map\ui\ui_disp_ini.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 195)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = dropedit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.groupBox2 = QtWidgets.QGroupBox(Dialog)
        self.gridLayout3 = QtWidgets.QGridLayout(self.groupBox2)
        self.gridLayout3.setObjectName("gridLayout_3")
        self.groupBox2.setObjectName("groupBox2")
        self.lineEditDEM = dropedit(Dialog)
        self.lineEditDEM.setObjectName("lineEditDEM")
        self.gridLayout3.addWidget(self.lineEditDEM, 0, 0, 1, 3)
        self.toolButtonDEM = QtWidgets.QPushButton(Dialog)
        self.toolButtonDEM.setObjectName("toolButtonDEM")
        self.gridLayout3.addWidget(self.toolButtonDEM, 1, 2, 1, 1)
        self.pushButtonDEM = QtWidgets.QPushButton(Dialog)
        self.pushButtonDEM.setObjectName("PushButtonDEM")
        self.gridLayout3.addWidget(self.pushButtonDEM, 1, 0, 1, 1)
        self.pushButtonCurrent = QtWidgets.QPushButton(Dialog)
        self.pushButtonCurrent.setObjectName("PushButtonCurrent")
        self.pushButtonCurrent.setEnabled(False)
        self.gridLayout3.addWidget(self.pushButtonCurrent, 1,1,1,1)
        self.gridLayout.addWidget(self.groupBox2, 1, 0, 1, 4)
        
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 3, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 4)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.gridLayout_2.addWidget(self.radioButton, 0, 0, 2, 2)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.gridLayout_2.addWidget(self.radioButton_2, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 4)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 1)
        self.lineEdit_2 = dropedit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 3, 3, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Landscape Mapping - Initialization"))
        self.label.setText(_translate("Dialog", "Input Picture"))
        self.toolButtonDEM.setText(_translate("Dialog", "Import DEM"))
        self.pushButtonDEM.setText(_translate("Dialog", "Add selected DEM"))
        self.pushButtonCurrent.setText(_translate("Dialog", "Add current view"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.groupBox.setTitle(_translate("Dialog", "Method used for pose estimation:"))
        self.groupBox2.setTitle(_translate("Dialog", "Input Elevation Model"))
        self.radioButton.setText(_translate("Dialog", "GCP approach"))
        self.radioButton_2.setText(_translate("Dialog", "Virtual 3D approach"))
        self.checkBox.setText(_translate("Dialog", "Ortho-photo"))
        self.toolButton_2.setText(_translate("Dialog", "..."))


class dropedit(QtWidgets.QLineEdit):   # subclass 
    dropped = pyqtSignal()
    def __init__(self, parent=None):
        super(dropedit, self).__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        
        
    def dropEvent(self, event):
        self.setText("Hello")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
