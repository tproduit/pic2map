# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_disprast.ui'
#
# Created: Thu Feb 27 15:00:19 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
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

class Ui_disprast(object):
    def setupUi(self, disprast):
        disprast.setObjectName(_fromUtf8("disprast"))
        disprast.resize(766, 836)
        disprast.setAnimated(True)
        self.centralwidget = QtGui.QWidget(disprast)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)
        disprast.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(disprast)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        disprast.setStatusBar(self.statusbar)
        self.dockWidget_2 = QtGui.QDockWidget(disprast)
        self.dockWidget_2.setFloating(False)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableView = TableView(self.dockWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMouseTracking(False)
        self.tableView.setAutoFillBackground(False)
        self.tableView.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableView.setFrameShape(QtGui.QFrame.Box)
        self.tableView.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableView.setMidLineWidth(2)
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableView.setAutoScroll(False)
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked)
        self.tableView.setTabKeyNavigation(True)
        self.tableView.setProperty("showDropIndicator", False)
        #self.tableView.setDragDropOverwriteMode(False)
        #self.tableView.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setShowGrid(True)
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setSortingEnabled(False)
        self.tableView.setWordWrap(True)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.verticalHeader().setVisible(True)
        self.verticalLayout_2.addWidget(self.tableView)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        disprast.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_2)
        self.actionOption1_1 = QtGui.QAction(disprast)
        self.actionOption1_1.setObjectName(_fromUtf8("actionOption1_1"))
        self.actionOption1_2 = QtGui.QAction(disprast)
        self.actionOption1_2.setObjectName(_fromUtf8("actionOption1_2"))
        self.actionOption1_3_1 = QtGui.QAction(disprast)
        self.actionOption1_3_1.setObjectName(_fromUtf8("actionOption1_3_1"))
        self.actionOption1_3_2 = QtGui.QAction(disprast)
        self.actionOption1_3_2.setObjectName(_fromUtf8("actionOption1_3_2"))
        self.actionOption2_1 = QtGui.QAction(disprast)
        self.actionOption2_1.setObjectName(_fromUtf8("actionOption2_1"))

        self.retranslateUi(disprast)
        QtCore.QMetaObject.connectSlotsByName(disprast)

    def retranslateUi(self, disprast):
        disprast.setWindowTitle(_translate("disprast", "Pose estimation - GCP Approach", None))

class TableView(QtGui.QTableView):
    """
    A simple table to demonstrate the QComboBox delegate.
    """
    def __init__(self, *args, **kwargs):
        QtGui.QTableView.__init__(self, *args, **kwargs)
        self.checkValues = ['Disable', 'Enable']
        self.setItemDelegateForColumn(5,ComboBoxDelegate(self, self.checkValues))
        
        
class ComboBoxDelegate(QtGui.QItemDelegate):
 
    def __init__(self, owner, itemslist):
        QtGui.QItemDelegate.__init__(self, owner)
        self.itemslist = itemslist
        self.owner = owner
 
    def paint(self, painter, option, index):        
        # Get Item Data
        self.owner.openPersistentEditor(index)
        value = index.data(QtCore.Qt.DisplayRole)
        # fill style options with item data
        style = QtGui.QApplication.style()
        opt = QtGui.QStyleOptionComboBox()
        opt.currentText = str(self.itemslist[value])
        opt.rect = option.rect
 
        # draw item data as ComboBox
        style.drawComplexControl(QtGui.QStyle.CC_ComboBox, opt, painter)
 
    def createEditor(self, parent, option, index):
        editor = QtGui.QComboBox(parent)
        editor.addItems(self.itemslist)
        editor.setCurrentIndex(0)
        editor.installEventFilter(self)            
        return editor
 
    def setEditorData(self, editor, index):
        text = self.itemslist[index.data(QtCore.Qt.DisplayRole)]
        pos = editor.findText(text)
        if pos == -1:  
            pos = 0
        editor.setCurrentIndex(pos)
 
    def setModelData(self,editor,model,index):
        #editor.setCurrentIndex(int(index.model().data(index)))
        value = editor.currentIndex()
        model.setData(index, value)
 
    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
 
        
