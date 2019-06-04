#!/usr/bin/env python
# Copyright (c) 2007-8 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

from builtins import str
from builtins import range
from builtins import object
import platform
import csv

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
PCI, PCJ, LOCX, LOCY, LOCZ, CHECK, ERROR, PIXERROR = list(range(8))
MAGIC_NUMBER = 0x570C4
FILE_VERSION = 1


class GCP(object):
    def __init__(self, picture_i=0., picture_j=0., local_x=0., local_y=0., local_z=0., check = 1, error = 0, pixerror = 0):

        self.picture_i = picture_i
        self.picture_j = picture_j
        self.local_x = local_x
        self.local_y = local_y
        self.local_z = local_z
        self.check = check
        self.error = error
        self.pixerror = pixerror


class GCPTableModel(QAbstractTableModel):

    def __init__(self, filename=""):
        super(GCPTableModel, self).__init__()
        self.filename = filename
        self.dirty = False
        self.GCPs = []
        self.pictures_i = set()
        self.pictures_j = set()
        self.locals_x = set()
        self.locals_y = set()
        self.locals_z = set()
        self.checks = set()
        self.errors = set()
        self.pixerrors = set()
        
    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index)|
                            Qt.ItemIsEditable)


    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or \
           not (0 <= index.row() < len(self.GCPs)):
            return 
        GCP = self.GCPs[index.row()]
        column = index.column()
        if role == Qt.DisplayRole:
            if column == PCI:
                return  GCP.picture_i
            elif column == PCJ:
                return  GCP.picture_j
            elif column == LOCX:
                return  GCP.local_x
            elif column == LOCY:
                return  GCP.local_y
            elif column == LOCZ:
                return  GCP.local_z
            elif column == CHECK:
                return  GCP.check
            elif column == ERROR:
                return  GCP.error
            elif column == PIXERROR:
                return  GCP.pixerror
        elif role == Qt.TextAlignmentRole:
            return  int(Qt.AlignLeft|Qt.AlignVCenter)
        elif role == Qt.BackgroundColorRole:
                return  QColor(210, 230, 230)
        return


    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return  int(Qt.AlignLeft|Qt.AlignVCenter)
            return  int(Qt.AlignRight|Qt.AlignVCenter)
        if role != Qt.DisplayRole:
            return  
        if orientation == Qt.Horizontal:
            if section == PCI:
                return  "Picture u"
            elif section == PCJ:
                return  "Picture v"
            elif section == LOCX:
                return  "World x"
            elif section == LOCY:
                return  "World y"
            elif section == LOCZ:
                return  "World z"
            elif section == CHECK:
                return  "Use as GCP"
            elif section == ERROR:
                return  "3D error [m]"
            elif section == PIXERROR:
                return  "Pixel error"
        return  int(section + 1)


    def rowCount(self, index=QModelIndex()):
        return len(self.GCPs)


    def columnCount(self, index=QModelIndex()):
        return 8


    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and 0 <= index.row() < len(self.GCPs):
            GCP = self.GCPs[index.row()]
            column = index.column()
            if type(value) == str:
                try:
                    value = float(value)
                except:
                    value = 0
            if column == PCI:
                GCP.picture_i = value
            elif column == PCJ:
                GCP.picture_j = value
            elif column == LOCX:
                GCP.local_x = value
            elif column == LOCY:
                GCP.local_y = value
            elif column == LOCZ:
                GCP.local_z = value
            elif column == CHECK:
                GCP.check = value
            elif column == ERROR:
                GCP.error = value
            elif column == PIXERROR:
                GCP.pixerror = value
            self.dirty = True
            self.dataChanged.emit(index, index, [Qt.EditRole])
            return True
        return False


    def insertRows(self, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position,position + rows - 1)
        for row in range(rows):
            self.GCPs.insert(position + row,GCP())
        self.endInsertRows()
        self.dirty = True
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position,
                             position + rows - 1)
        self.GCPs = self.GCPs[:position] + \
                     self.GCPs[position + rows:]
        self.endRemoveRows()
        self.dirty = True
        return True


    def load(self, filename, delete):

        exception = None
        fh = None
        
        self.filename = filename####
        if delete == QMessageBox.Yes:
            self.GCPs = []
        
        try:
            if not filename:
                raise IOError("no filename specified for loading")
            
            elif filename.find('.dat') != -1:
                fh = QFile(filename)
                if not fh.open(QIODevice.ReadOnly):
                    raise IOError(str(fh.errorString()))
                stream = QDataStream(fh)
                magic = stream.readInt32()
                if magic != MAGIC_NUMBER:
                    raise IOError("unrecognized file type")
                fileVersion = stream.readInt16()
                if fileVersion != FILE_VERSION:
                    raise IOError("unrecognized file type version")
                while not stream.atEnd():
                    picture_i = stream.readQVariant()
                    picture_j = stream.readQVariant()
                    local_x = stream.readQVariant()
                    local_y = stream.readQVariant()
                    local_z  = stream.readQVariant()
                    self.GCPs.append(GCP(picture_i,picture_j,local_x,local_y,local_z))
                    self.pictures_i.add(picture_i)
                    self.pictures_j.add(picture_j)
                    self.locals_x.add(local_x)
                    self.locals_y.add(local_y)
                    self.locals_z.add(local_z)
                self.dirty = False
                
            elif filename.find('.csv') != -1:
                f = open(filename, 'r')
                try:
                    gcpReader = csv.reader(f)
                    
                    i= 0
                    for row in gcpReader:
                        if i!=0:
                            picture_i = float(row[0])
                            picture_j = float(row[1])
                            local_x = float(row[2])
                            local_y = float(row[3])
                            local_z  = float(row[4])
                            
                            self.GCPs.append(GCP(picture_i,picture_j,local_x,local_y,local_z))
                            self.pictures_i.add(picture_i)
                            self.pictures_j.add(picture_j)
                            self.locals_x.add(local_x)
                            self.locals_y.add(local_y)
                            self.locals_z.add(local_z)
                        i+=1
                finally:
                    f.close()
                
        except IOError as e:
            exception = e
        finally:
            if fh is not None:
                fh.close()
            if exception is not None:
                raise exception

    def save(self, filename):
        
        self.filename = filename##########
        exception = None
        fh = None
        try:
            if not filename:
                raise IOError("no filename specified for saving")
            if filename.find('.dat')==-1:
                filename = filename+'.dat'
            
            fh = QFile(filename)
            if not fh.open(QIODevice.WriteOnly):
                raise IOError(str(fh.errorString()))
            stream = QDataStream(fh)
            stream.writeInt32(MAGIC_NUMBER)
            stream.writeInt16(FILE_VERSION)
            if hasattr(QDataStream,'Qt_4_8'):
                stream.setVersion(QDataStream.Qt_4_8)
            for GCP in self.GCPs:
                stream.writeQVariant(GCP.picture_i)
                stream.writeQVariant(GCP.picture_j)
                stream.writeQVariant(GCP.local_x)
                stream.writeQVariant(GCP.local_y)
                stream.writeQVariant(GCP.local_z)
            self.dirty = False
        except IOError as e:
            exception = e
        finally:
            if fh is not None:
                fh.close()
            if exception is not None:
                raise exception
                
        #Save as CSV
        ############
        filename = filename.replace('.dat','.csv')
        if filename.find('.csv')==-1:
            filename = filename+'.csv'
            
        f = open(filename, 'w')
        try:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerow( ('line', 'column', 'X', 'Y', 'Z') )
            for GCP in self.GCPs:
                writer.writerow( (GCP.picture_i, GCP.picture_j, GCP.local_x, GCP.local_y, GCP.local_z) )
        finally:
            f.close()
        

    def checkValid(self,rowIndex):
        valid = 1
        for i in range(0,8):
            index = self.index(rowIndex, i)
            dat = self.data(index)
            if not isinstance(dat, (int, float)):
                valid = 0
        return valid

