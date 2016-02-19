from OpenGL.GL import *
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from OpenGL.GLU import *
import sys

class CheckVersion(QGLWidget):
    # create an openGL context for checking the version
    def __init__(self, parent = None):
        super(CheckVersion, self).__init__(parent)
        self.isSupported= 0
        
    def initializeGL(self):
        #Get the current version of openGL
        #Need to do it in initializeGL because a openGL context is needed
        
        versionString = glGetString(GL_VERSION)
        versionString = versionString.split('.');
        versionString = ''.join(versionString)
        try:
            versionInt = int(versionString)
            if(versionInt>=310):
              self.isSupported = 1
            else:
                self.isSupported = 0 
        except ValueError: 
           self.isSupported = 0 
            

        
        #Need version 3.1.0 or above

    
    
