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


from builtins import str
from past.utils import old_div
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PIL import Image
from PIL.ExifTags import TAGS
from .ui_exif2 import Ui_Exif2
from qgis.core import *
from qgis.gui import *
from numpy import sqrt
import string

class ExifInfo(QDialog):
    fixFocalSignal = pyqtSignal(float)
    def __init__(self, imageName, crs):
        QDialog.__init__(self)
        self.ui_exif_info = Ui_Exif2()
        self.ui_exif_info.setupUi(self)
        self.FocalLength = None
        img = Image.open(imageName)
        if hasattr(img,'_getexif'):
            raw = img._getexif()
        else:
            QMessageBox.warning(QMainWindow(),"Error","Image has no EXIF")
            return
        
        sizePicture = img.size
        self.diag = sqrt(sizePicture[0]**2+sizePicture[1]**2)
        if raw != None and any(raw):
            dict = None
            for (k,v) in raw.items():
                if TAGS.get(k) == 'GPSInfo':
                    dict = v
                if TAGS.get(k) == 'FocalLength':
                    self.FocalLength = v
            text = ''
            if dict != None:
                Nord = dict[2][0][0]+dict[2][1][0]/float(dict[2][1][1])/60.0
                Est = dict[4][0][0]+dict[4][1][0]/float(dict[4][1][1])/60.0
                crsTarget = QgsCoordinateReferenceSystem(crs.postgisSrid())
                crsSource = QgsCoordinateReferenceSystem(4326)
                xform = QgsCoordinateTransform(crsSource, crsTarget, QgsProject.instance())
                LocalPos = xform.transform(QgsPointXY(Est,Nord))
                text += 'Nord: ' + str(LocalPos[0])
                text += '\nEst: ' +str(LocalPos[1])
                text += '\n\n'
 
            text += '============================\n'
            text += 'Raw EXIF data:'
            for (k,v) in raw.items():
                test = True
                if isinstance(v, (int, float, complex, bool)):
                    text += "\n  " + str(TAGS.get(k)) + ": " + str(v)
                else:
                    for c in str(v):
                        if isinstance(c, str) and c not in string.ascii_letters and c not in string.digits and c not in string.whitespace and c not in('.',',','(',')',':'):
                            test = False
                    if test:
                        text += "\n  " + str(TAGS.get(k)) + ": " + str(v)

            self.ui_exif_info.textBrowser.setText(text)
        else:
            raise IOError
        
        self.ui_exif_info.pushButton.clicked.connect(self.getFocal)
    
    def getFocal(self):
        if self.FocalLength != None:
            sensorDiagString = self.ui_exif_info.lineDiagSensor.text()
            try:
                sensorDiagFloat = float(sensorDiagString)
            except ValueError:
                QMessageBox.warning(QMainWindow(),"Error","Float format not valid")
            else:
                FocalLengthMM = old_div(self.FocalLength[0],self.FocalLength[1])
                focalPixel = round(old_div(FocalLengthMM,sensorDiagFloat)*self.diag,2)
                self.ui_exif_info.lineFocalPixel.setText(str(focalPixel))
                self.fixFocalSignal.emit(focalPixel)
        else: 
            QMessageBox.warning(QMainWindow(),"Error","Focal information not found in EXIF")
    
