# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_disp_ini.ui'
#
# Created: Mon Apr 28 16:34:05 2014
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

class Ui_disp_ini(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(447, 195)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = dropedit(Dialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.labelDEM = QtGui.QLabel(Dialog)
        self.labelDEM.setObjectName(_fromUtf8("labelDEM"))
        self.gridLayout.addWidget(self.labelDEM, 1, 0, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.toolButtonDEM = QtGui.QToolButton(Dialog)
        self.toolButtonDEM.setObjectName(_fromUtf8("toolButtonDEM"))
        self.gridLayout.addWidget(self.toolButtonDEM, 1, 3, 1, 1)
        self.toolButton = QtGui.QToolButton(Dialog)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.gridLayout.addWidget(self.toolButton, 0, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 4)
        self.lineEditDEM = dropedit(Dialog)
        self.lineEditDEM.setObjectName(_fromUtf8("lineEditDEM"))
        self.gridLayout.addWidget(self.lineEditDEM, 1, 1, 1, 2)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.buttonGroup = QtGui.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.radioButton)
        self.gridLayout_2.addWidget(self.radioButton, 0, 0, 2, 2)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.buttonGroup.addButton(self.radioButton_2)
        self.gridLayout_2.addWidget(self.radioButton_2, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 4)
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 1)
        self.lineEdit_2 = dropedit(Dialog)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.toolButton_2 = QtGui.QToolButton(Dialog)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.gridLayout.addWidget(self.toolButton_2, 3, 3, 1, 1)

        
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Landscape Mapping - Initialization", None))
        self.labelDEM.setText(_translate("Dialog", "Input Elevation Model", None))
        self.label.setText(_translate("Dialog", "Input Picture", None))
        self.toolButtonDEM.setText(_translate("Dialog", "...", None))
        self.toolButton.setText(_translate("Dialog", "...", None))
        self.groupBox.setTitle(_translate("Dialog", "Method used for pose estimation:", None))
        self.radioButton.setText(_translate("Dialog", "Ground Control Points", None))
        self.radioButton_2.setText(_translate("Dialog", "Navigation in 3D model", None))
        self.checkBox.setText(_translate("Dialog", "Ortho-photo", None))
        self.toolButton_2.setText(_translate("Dialog", "...", None))

class dropedit(QtGui.QLineEdit):   # subclass 
    def __init__(self, parent=None):
        super(dropedit, self).__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        
        
    def dropEvent(self, event):
        self.setText("Hello")

