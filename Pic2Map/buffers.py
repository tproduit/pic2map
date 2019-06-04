"""
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 """
from __future__ import division
from __future__ import print_function
from builtins import map
from builtins import range
from past.utils import old_div
from OpenGL.GL import *
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from numpy import array, zeros, size, repeat, float32, uint32, max, min
from osgeo import gdal
from .ui_buffering import Ui_Form
import operator

class Buffers(QtWidgets.QWidget):
    def __init__(self, DEM_name, dem_box, use_ortho, ortho_name, ortho_box, parent = None):
        super(Buffers, self).__init__(parent)
        self.numpy_verts = 0     
        self.m_indices = 0
        self.m_normal = 0 
        self.l_nord = 0
        self.l_est = 0
        self.res = 0
        self.DEM_name = DEM_name
        self.temp_dem_box = dem_box
        
        self.ortho_name = ortho_name
        self.ortho_box = ortho_box
        self.use_ortho = use_ortho
        
    def getBuffer(self):
            box = [self.temp_dem_box.xMinimum(), self.temp_dem_box.yMinimum(), self.temp_dem_box.xMaximum(), self.temp_dem_box.yMaximum()]
            bar = progress_bar()
            bar.show()
            bar.progressBar = bar.ui_progbar.progressBar
            bar.progressBar.setValue(1)
            QApplication.processEvents()
    
            #opening tif DEM
            tif = gdal.Open(self.DEM_name)
            imarray = array(tif.ReadAsArray())
            #closing tif raster
            tif = None
            ############
            l_est = size(imarray,1)
            l_nord = size(imarray,0)
            resolution1 = round((box[2]-box[0])/float(l_est))
            resolution2 = round((box[3]-box[1])/float(l_nord))
            if resolution1 != resolution2:
                print('unsuported ressolution type')
                print(resolution1)
                print(resolution2)
                raise ValueError
            
            self.dem_box = [box[0]+old_div(resolution1,2), box[1]+old_div(resolution1,2), box[2]-old_div(resolution1,2), box[3]-old_div(resolution1,2)]
            self.demMax = max(imarray)
            self.demMin = min(imarray)
            
            res = resolution1
            self.res = res
    
            self.verts = zeros((l_est*l_nord,3))
            col1 = repeat(list(range(l_est)),l_nord)
            col2 = imarray.T.flatten()
            col3 = list(range(l_nord))*l_est

            self.verts[:,0] = -1*(array(col1)*res + float(self.dem_box[0]))
            self.verts[:,1] = col2
            self.verts[:,2] = -1*array(col3)*res + float(self.dem_box[3])
            bar.progressBar.setValue(10)
            QApplication.processEvents()
            self.numpy_verts = array(self.verts, dtype=float32)
            if not self.use_ortho:
                self.normal = []
                bar.progressBar.setValue(20)
                QApplication.processEvents()
                vect1 =  self.verts[0:(l_est*l_nord-l_nord),:]
                vect2 =  self.verts[1:(l_est*l_nord-l_nord+1),:]
                vect3 =  self.verts[l_nord:(l_est*l_nord),:]
                bar.progressBar.setValue(30)
                QApplication.processEvents()
                v1 = list(map(operator.sub, vect1, vect2))
                bar.progressBar.setValue(40)
                QApplication.processEvents()
                v2 = list(map(operator.sub, vect1, vect3))
                bar.progressBar.setValue(50)
                QApplication.processEvents()
                v3 = list(map(lambda x,y:[x[1]*y[2] - x[2]*y[1], 
                                     x[2]*y[0] - x[0]*y[2], 
                                     x[0]*y[1] - x[1]*y[0]], v1, v2))                   
                bar.progressBar.setValue(80)
                QApplication.processEvents()
                self.m_normal = array(v3, dtype=float32)
            
            self.m_indices = []
            bar.progressBar.setValue(90)
            QApplication.processEvents()
            for z in range(l_est-2):
                for x in range(l_nord):
                    i = (z * l_nord + x);
                    self.m_indices.append(i)
                    self.m_indices.append(i + l_nord);
                    if (x == (l_nord-1)):
                        1
                        self.m_indices.append(i+l_nord)
                        self.m_indices.append(i+1);
            self.m_indices= array(self.m_indices,dtype=uint32)
            self.l_est = l_est
            self.l_nord = l_nord
            bar.progressBar.setValue(100)
            QApplication.processEvents()
        
class progress_bar(QtWidgets.QWidget):
        def __init__(self):
            QtWidgets.QDialog.__init__(self)
            self.ui_progbar = Ui_Form()
            self.ui_progbar.setupUi(self)
