# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_Pose(object):
    def setupUi(self, PoseDialog):
        PoseDialog.setObjectName(_fromUtf8("PoseDialog"))
        PoseDialog.resize(648, 383)
        self.gridLayout = QtWidgets.QGridLayout(PoseDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtWidgets.QDialogButtonBox(PoseDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 4, 1, 1)
        self.frame_2 = QtWidgets.QFrame(PoseDialog)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 318))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        

        self.XPosFree = QtWidgets.QRadioButton(self.frame_2)
        self.XPosFree.setObjectName(_fromUtf8("XPosFree"))
        self.XPosFixed = QtWidgets.QRadioButton(self.frame_2)
        self.XPosFixed.setObjectName(_fromUtf8("XPosFixed"))
        self.XPosIni = QtWidgets.QRadioButton(self.frame_2)
        self.XPosIni.setObjectName(_fromUtf8("XPosIni"))
        self.XPosGroup = QtWidgets.QButtonGroup(PoseDialog)
        self.XPosGroup.setObjectName(_fromUtf8("XPosGroup"))
        self.XPosGroup.addButton(self.XPosFixed)
        self.XPosGroup.addButton(self.XPosFree)
        self.XPosGroup.addButton(self.XPosIni)
        self.gridLayout_2.addWidget(self.XPosFree, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.XPosFixed, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.XPosIni, 0, 3, 1, 1)
        
        self.YPosFree = QtWidgets.QRadioButton(self.frame_2)
        self.YPosFree.setObjectName(_fromUtf8("YPosFree"))
        self.YPosFixed = QtWidgets.QRadioButton(self.frame_2)
        self.YPosFixed.setObjectName(_fromUtf8("YPosFixed"))
        self.YPosIni = QtWidgets.QRadioButton(self.frame_2)
        self.YPosIni.setObjectName(_fromUtf8("YPosIni"))
        self.YPosGroup = QtWidgets.QButtonGroup(PoseDialog)
        self.YPosGroup.setObjectName(_fromUtf8("YPosGroup"))
        self.YPosGroup.addButton(self.YPosFree)
        self.YPosGroup.addButton(self.YPosFixed)
        self.YPosGroup.addButton(self.YPosIni)
        self.gridLayout_2.addWidget(self.YPosFree, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.YPosFixed, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.YPosIni, 1, 3, 1, 1)


        self.ZPosFree = QtWidgets.QRadioButton(self.frame_2)
        self.ZPosFree.setObjectName(_fromUtf8("ZPosFree"))
        self.ZPosFixed = QtWidgets.QRadioButton(self.frame_2)
        self.ZPosFixed.setObjectName(_fromUtf8("ZPosFixed"))
        self.ZPosIni = QtWidgets.QRadioButton(self.frame_2)
        self.ZPosIni.setObjectName(_fromUtf8("ZPosIni"))
        self.ZPoseGroup = QtWidgets.QButtonGroup(PoseDialog)
        self.ZPoseGroup.setObjectName(_fromUtf8("ZPoseGroup"))
        self.ZPoseGroup.addButton(self.ZPosFixed)
        self.ZPoseGroup.addButton(self.ZPosFree)
        self.ZPoseGroup.addButton(self.ZPosIni)
        self.gridLayout_2.addWidget(self.ZPosFree, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.ZPosFixed, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(self.ZPosIni, 2, 3, 1, 1)
        
        self.tiltFree = QtWidgets.QRadioButton(self.frame_2)
        self.tiltFree.setObjectName(_fromUtf8("tiltFree"))
        self.tiltFixed = QtWidgets.QRadioButton(self.frame_2)
        self.tiltFixed.setObjectName(_fromUtf8("tiltFixed"))
        self.tiltIni = QtWidgets.QRadioButton(self.frame_2)
        self.tiltIni.setObjectName(_fromUtf8("tiltIni"))
        self.tiltgroup = QtWidgets.QButtonGroup(PoseDialog)
        self.tiltgroup.setObjectName(_fromUtf8("tiltgroup"))
        self.tiltgroup.addButton(self.tiltFree)
        self.tiltgroup.addButton(self.tiltFixed)
        self.tiltgroup.addButton(self.tiltIni)
        self.gridLayout_2.addWidget(self.tiltFree, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.tiltFixed, 3, 2, 1, 1)
        self.gridLayout_2.addWidget(self.tiltIni, 3, 3, 1, 1)
        
        self.headingFree = QtWidgets.QRadioButton(self.frame_2)
        self.headingFree.setObjectName(_fromUtf8("headingFree"))
        self.headingFixed = QtWidgets.QRadioButton(self.frame_2)
        self.headingFixed.setObjectName(_fromUtf8("headingFixed"))
        self.headingIni = QtWidgets.QRadioButton(self.frame_2)
        self.headingIni.setObjectName(_fromUtf8("headingIni"))
        self.headinggroup = QtWidgets.QButtonGroup(PoseDialog)
        self.headinggroup.setObjectName(_fromUtf8("headinggroup"))
        self.headinggroup.addButton(self.headingFree)
        self.headinggroup.addButton(self.headingFixed)
        self.headinggroup.addButton(self.headingIni)
        self.gridLayout_2.addWidget(self.headingFree, 4, 1, 1, 1)
        self.gridLayout_2.addWidget(self.headingFixed, 4, 2, 1, 1)
        self.gridLayout_2.addWidget(self.headingIni, 4, 3, 1, 1)
        
        self.swingFree = QtWidgets.QRadioButton(self.frame_2)
        self.swingFree.setObjectName(_fromUtf8("swingFree"))
        self.swingFixed = QtWidgets.QRadioButton(self.frame_2)
        self.swingFixed.setObjectName(_fromUtf8("swingFixed"))
        self.swingIni = QtWidgets.QRadioButton(self.frame_2)
        self.swingIni.setObjectName(_fromUtf8("swingIni"))
        self.swinggroup = QtWidgets.QButtonGroup(PoseDialog)
        self.swinggroup.setObjectName(_fromUtf8("swinggroup"))
        self.swinggroup.addButton(self.swingFree)
        self.swinggroup.addButton(self.swingFixed)
        self.swinggroup.addButton(self.swingIni)
        self.gridLayout_2.addWidget(self.swingFree, 5, 1, 1, 1)
        self.gridLayout_2.addWidget(self.swingFixed, 5, 2, 1, 1)
        self.gridLayout_2.addWidget(self.swingIni, 5, 3, 1, 1)
        
        self.focalFree = QtWidgets.QRadioButton(self.frame_2)
        self.focalFree.setObjectName(_fromUtf8("focalFree"))
        self.focalFixed = QtWidgets.QRadioButton(self.frame_2)
        self.focalFixed.setObjectName(_fromUtf8("focalFixed"))
        self.focalIni = QtWidgets.QRadioButton(self.frame_2)
        self.focalIni.setObjectName(_fromUtf8("focalIni"))
        self.focalgroup = QtWidgets.QButtonGroup(PoseDialog)
        self.focalgroup.setObjectName(_fromUtf8("focalgroup"))
        self.focalgroup.addButton(self.focalFixed)
        self.focalgroup.addButton(self.focalFree)
        self.focalgroup.addButton(self.focalIni)
        self.gridLayout_2.addWidget(self.focalFree, 6, 1, 1, 1)
        self.gridLayout_2.addWidget(self.focalFixed, 6, 2, 1, 1)
        self.gridLayout_2.addWidget(self.focalIni, 6, 3, 1, 1)

        self.XPosLine = QtWidgets.QLineEdit(self.frame_2)
        self.XPosLine.setObjectName(_fromUtf8("XPosLine"))
        self.gridLayout_2.addWidget(self.XPosLine, 0, 4, 1, 1)
        
        self.YPosLine = QtWidgets.QLineEdit(self.frame_2)
        self.YPosLine.setObjectName(_fromUtf8("YPosLine"))
        self.gridLayout_2.addWidget(self.YPosLine, 1, 4, 1, 1)
        
        self.ZPosLine = QtWidgets.QLineEdit(self.frame_2)
        self.ZPosLine.setObjectName(_fromUtf8("ZPosLine"))
        self.gridLayout_2.addWidget(self.ZPosLine, 2, 4, 1, 1)
        
        self.tiltLine = QtWidgets.QLineEdit(self.frame_2)
        self.tiltLine.setObjectName(_fromUtf8("tiltLine"))
        self.gridLayout_2.addWidget(self.tiltLine, 3, 4, 1, 1)
        
        self.headingLine = QtWidgets.QLineEdit(self.frame_2)
        self.headingLine.setObjectName(_fromUtf8("headingLine"))
        self.gridLayout_2.addWidget(self.headingLine, 4, 4, 1, 1)
        
        self.swingLine = QtWidgets.QLineEdit(self.frame_2)
        self.swingLine.setObjectName(_fromUtf8("swingLine"))
        self.gridLayout_2.addWidget(self.swingLine, 5, 4, 1, 1)
        
        self.focalLine = QtWidgets.QLineEdit(self.frame_2)
        self.focalLine.setObjectName(_fromUtf8("focalLine"))
        self.gridLayout_2.addWidget(self.focalLine, 6, 4, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)
   
        self.gridLayout.addWidget(self.frame_2, 1, 1, 1, 4)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(PoseDialog)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.gridLayout.addWidget(self.commandLinkButton, 2, 1, 1, 1)
        self.XPosFree.setChecked(True)
        self.YPosFree.setChecked(True)
        self.ZPosFree.setChecked(True)
        self.tiltFree.setChecked(True)
        self.headingFree.setChecked(True)
        self.swingFree.setChecked(True)
        self.focalFree.setChecked(True)
        
        self.reportButton = QtWidgets.QPushButton(PoseDialog)
        self.reportButton.setObjectName(_fromUtf8("reportButton"))
        self.gridLayout.addWidget(self.reportButton, 2, 2, 1, 1)
        
        self.cameraPositionButton = QtWidgets.QPushButton(PoseDialog)
        self.cameraPositionButton.setObjectName(_fromUtf8("cameraPositionButton"))
        self.gridLayout.addWidget(self.cameraPositionButton, 2, 3, 1, 1)
        self.cameraPositionButton.setEnabled(False)

        self.retranslateUi(PoseDialog)
        self.buttonBox.accepted.connect(PoseDialog.accept)
        self.buttonBox.rejected.connect(PoseDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PoseDialog)
        
        self.XPosLine.setReadOnly(True)
        self.XPosFixed.toggled.connect(self.XPosFixedclicked)
        self.XPosFree.toggled.connect(self.XPosFreeclicked)
        self.XPosIni.toggled.connect(self.XPosIniclicked)
        
        self.YPosLine.setReadOnly(True)
        self.YPosFixed.toggled.connect(self.YPosFixedclicked)
        self.YPosFree.toggled.connect(self.YPosFreeclicked)
        self.YPosIni.toggled.connect(self.YPosIniclicked)
        
        self.ZPosLine.setReadOnly(True)
        self.ZPosFixed.toggled.connect(self.ZPosFixedclicked)
        self.ZPosFree.toggled.connect(self.ZPosFreeclicked)
        self.ZPosIni.toggled.connect(self.ZPosIniclicked)
        
        self.headingLine.setReadOnly(True)
        self.headingFixed.toggled.connect(self.headingFixedclicked)
        self.headingFree.toggled.connect(self.headingFreeclicked)
        self.headingIni.toggled.connect(self.headingIniclicked)
        
        self.tiltLine.setReadOnly(True)
        self.tiltFixed.toggled.connect(self.tiltFixedclicked)
        self.tiltFree.toggled.connect(self.tiltFreeclicked)
        self.tiltIni.toggled.connect(self.tiltIniclicked)
        
        self.swingLine.setReadOnly(True)
        self.swingFixed.toggled.connect(self.swingFixedclicked)
        self.swingFree.toggled.connect(self.swingFreeclicked)
        self.swingIni.toggled.connect(self.swingIniclicked)
        
        self.focalLine.setReadOnly(True)
        self.focalFixed.toggled.connect(self.focalFixedclicked)
        self.focalFree.toggled.connect(self.focalFreeclicked)
        self.focalIni.toggled.connect(self.focalIniclicked)


    def focalFixedclicked(self):
        if self.focalFixed.isChecked():
            self.focalLine.setReadOnly(False) 
    def focalFreeclicked(self):
        if self.focalFree.isChecked():
            self.focalLine.setText('')
            self.focalLine.setReadOnly(True)
    def focalIniclicked(self):
        if self.focalIni.isChecked():
            self.focalLine.setReadOnly(False)
            
    def swingFixedclicked(self):
        if self.swingFixed.isChecked():
            self.swingLine.setReadOnly(False) 
    def swingFreeclicked(self):
        if self.swingFree.isChecked():
            self.swingLine.setText('')
            self.swingLine.setReadOnly(True)
    def swingIniclicked(self):
        if self.swingIni.isChecked():
            self.swingLine.setReadOnly(False)
            
    def tiltFixedclicked(self):
        if self.tiltFixed.isChecked():
            self.tiltLine.setReadOnly(False) 
    def tiltFreeclicked(self):
        if self.tiltFree.isChecked():
            self.tiltLine.setText('')
            self.tiltLine.setReadOnly(True)
    def tiltIniclicked(self):
        if self.tiltIni.isChecked():
            self.tiltLine.setReadOnly(False)
            
    def headingFixedclicked(self):
        if self.headingFixed.isChecked():
            self.headingLine.setReadOnly(False) 
    def headingFreeclicked(self):
        if self.headingFree.isChecked():
            self.headingLine.setText('')
            self.headingLine.setReadOnly(True)
    def headingIniclicked(self):
        if self.headingIni.isChecked():
            self.headingLine.setReadOnly(False)
            
    def ZPosFixedclicked(self):
        if self.ZPosFixed.isChecked():
            self.ZPosLine.setReadOnly(False) 
    def ZPosFreeclicked(self):
        if self.ZPosFree.isChecked():
            self.ZPosLine.setText('')
            self.ZPosLine.setReadOnly(True)
    def ZPosIniclicked(self):
        if self.ZPosIni.isChecked():
            self.ZPosLine.setReadOnly(False)
            
    def YPosFixedclicked(self):
        if self.YPosFixed.isChecked():
            self.YPosLine.setReadOnly(False) 
    def YPosFreeclicked(self):
        if self.YPosFree.isChecked():
            self.YPosLine.setText('')
            self.YPosLine.setReadOnly(True)
    def YPosIniclicked(self):
        if self.YPosIni.isChecked():
            self.YPosLine.setReadOnly(False)
            
    def XPosFixedclicked(self):
        if self.XPosFixed.isChecked():
            self.XPosLine.setReadOnly(False)
    def XPosFreeclicked(self):
        if self.XPosFree.isChecked():
            self.XPosLine.setText('')
            self.XPosLine.setReadOnly(True)
    def XPosIniclicked(self):
        if self.XPosIni.isChecked():
            self.XPosLine.setReadOnly(False)
            
            
    def retranslateUi(self, PoseDialog):
        PoseDialog.setWindowTitle(_translate("PoseDialog", "Pose estimation", None))
        
        self.XPosFree.setText(_translate("PoseDialog", "Free", None))
        self.XPosFixed.setText(_translate("PoseDialog", "Fixed", None))
        self.XPosIni.setText(_translate("PoseDialog", "Apriori", None))
        
        self.YPosFree.setText(_translate("PoseDialog", "Free", None))
        self.YPosFixed.setText(_translate("PoseDialog", "Fixed", None))
        self.YPosIni.setText(_translate("PoseDialog", "Apriori", None))
        
        self.ZPosFree.setText(_translate("PoseDialog", "Free", None))
        self.ZPosFixed.setText(_translate("PoseDialog", "Fixed", None))
        self.ZPosIni.setText(_translate("PoseDialog", "Apriori", None))
        
        self.tiltFree.setText(_translate("PoseDialog", "Free", None))
        self.tiltFixed.setText(_translate("PoseDialog", "Fixed", None))
        self.tiltIni.setText(_translate("PoseDialog", "Apriori", None))
        
        self.headingFree.setText(_translate("PoseDialog", "Free", None))
        self.headingFixed.setText(_translate("PoseDialog", "Fixed", None))
        self.headingIni.setText(_translate("PoseDialog", "Apriori", None))
        
        self.swingFree.setText(_translate("PoseDialog", "Free", None))
        self.swingFixed.setText(_translate("PoseDialog", "Fixed", None))
        self.swingIni.setText(_translate("PoseDialog", "Apriori", None))
        
        self.focalFree.setText(_translate("PoseDialog", "Free", None))
        self.focalFixed.setText(_translate("PoseDialog", "Fixed", None))
        self.focalIni.setText(_translate("PoseDialog", "Apriori", None))

        self.label_2.setText(_translate("PoseDialog", "X Position [m]", None))
        self.label_3.setText(_translate("PoseDialog", "Y Position [m]", None))
        self.label_4.setText(_translate("PoseDialog", "Z Position [m]", None))
        self.label_5.setText(_translate("PoseDialog", "tilt [°]", None))
        self.label_6.setText(_translate("PoseDialog", "heading [°]", None))
        self.label_7.setText(_translate("PoseDialog", "swing [°]", None))
        self.label_8.setText(_translate("PoseDialog", "focal [pixel]", None))
        self.reportButton.setText(_translate("PoseDialog", "Report on GCPs", None))
        self.cameraPositionButton.setText(_translate("PoseDialog" , "Export camera position", None))

        self.commandLinkButton.setText(_translate("PoseDialog", "Pose Estimation", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PoseDialog = QtWidgets.QDialog()
    ui = Ui_PoseDialog()
    ui.setupUi(PoseDialog)
    PoseDialog.show()
    sys.exit(app.exec_())

