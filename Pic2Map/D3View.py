"""
/***************************************************************************
 *                                                                         *
 *   This program is free software you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *****
 
The class D3_view is called from different part of the code. It has different behavior
depending on its use.
It can:
- be used "on screen" or offscreen (self.offscreen)
- use an orthoimage or shadowed DEM (self.useOrthoImage)
- support Framebuffer or not for offscreen rendering( self.isFramBufferSupported)
- have a picture in the background (if self.picture_name)
- Have an invisible DEM or not (self.transparency)

Characteristics for each usage:
1. Used as 3D viewer in the GCP approach
    - on screen rendering
    - use ortho-image or not
    - has not picture in the background
    - is visible
2. Used as tool of projection after pose estimation in the GCP approach
    - offscreen rendering
    - support Framebuffer or not (depending on openGL version)
    - have no picture in the background
2. Used as central widget in the Virtual 3D approach
    - on screen rendering
    - use ortho-image or not
    - has a picture in the background
    - can be visible, invisible or half transparent
    
The pose of the camera is done as following:
    self.pos contains the position of the camera (used in gluLookAt)
    self.lookat contains a point towards the camera is looking (used in gluLookAt)
    self.roll contains the vertical direction (rotation around the front axis) (used in gluLookAt)
    self.FOV contains the field of view information, equivalent to the focal information (used in gluPerspective)
"""
from __future__ import division

from builtins import zip
from past.utils import old_div
from OpenGL.GL import *
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtOpenGL import *
from OpenGL.GLU import *
from OpenGL.GL.framebufferobjects import *
from numpy import sqrt, cos, sin, arccos, arctan2, zeros, array, float32, pi, linalg, cross, dot, tan
from qgis.core import *


class D3_view(QOpenGLWidget):
    getGCPIn3DviewSignal = pyqtSignal()
    fixPositionSignal = pyqtSignal(tuple)
    def __init__(self, pointBuffer, picture_name = None, roll = 0, FOV = 30, 
                 transparency = 100, pos = None, lookat = None, upWorld = None, offscreen = False, offscreenSize = [None, None]
                 ,isFramBufferSupported = False, parent = None):
        super(D3_view, self).__init__(parent)
        self.pos = pos
        self.upWorld = upWorld
        self.lookat = lookat
        self.roll = roll
        self.FOV = FOV
        self.transparency = transparency
        self.offscreen = offscreen
        self.size0 = offscreenSize[0]
        self.size1 = offscreenSize[1]
        self.isFramBufferSupported = isFramBufferSupported
        
        self.numpy_verts = pointBuffer.numpy_verts
        self.m_indices =  pointBuffer.m_indices
        self.m_normal =  pointBuffer.m_normal
        self.l_nord =  pointBuffer.l_nord
        self.l_est =  pointBuffer.l_est
        self.res =  pointBuffer.res
        self.picture_name = picture_name
        self.useOrthoImage = bool(pointBuffer.ortho_name)
        self.ortho_name = pointBuffer.ortho_name
        self.ortho_box = pointBuffer.ortho_box
        
        # sheeps, sheepsSize, cube and colorSheep is used for drawing GCP in the 3D viewer
        self.sheeps = []
        self.sheepsSize = 100
        self.cube = array([[[1,-1,-1],[1,-1,1],[-1,-1,1],[-1,-1,-1]],[[-1,-1,-1],[-1,1,-1],[1,1,-1],[1,-1,-1]], [[1,-1,1],[1,1,1],[-1,1,1],[-1,-1,1]],[[1,-1,-1],[1,1,-1],[1,1,1],[1,-1,1]],[[-1,-1,1],[-1,1,1],[-1,1,-1],[-1,-1,-1]],[[1,1,1],[1,1,-1],[-1,1,-1],[-1,1,1]]], dtype =float32)
        self.colorSheep = [(1.0,0.0,1.0),(1.0,1.0,0.0),(0.0,1.0,1.0),(1.0,0.5,1.0),(1.0,0.0,0.0),(0.0,1.0,0.0)]
        
    def updateSheeps(self, data, p0):
        # Used from the doIt function in Virtual 3D approach
        for x,z in data:
            self.sheeps.append([p0[0]-x*2*self.sheepsSize,p0[1]+1200+z*2*self.sheepsSize,p0[2]])
        
    def wheelEvent(self,event):
        # translate the view position in the front direction
        self.last_pos = event.pos()
        delta = old_div(event.angleDelta().y()*self.res,5)
        xk = self.pos[0]-self.lookat[0]
        yk = self.pos[1]-self.lookat[1]
        zk = self.pos[2]-self.lookat[2]
        n = sqrt((xk)**2+(yk)**2+(zk)**2)
        vect = array([xk,yk,zk])
        vect = old_div(vect,linalg.norm(vect))
        deltax =  vect[0]*delta
        deltay =  vect[1]*delta
        deltaz =  vect[2]*delta
        self.pos = [self.pos[0]+deltax, self.pos[1]+deltay,self.pos[2]+deltaz]
        self.lookat = [self.lookat[0]+deltax, self.lookat[1]+deltay,self.lookat[2]+deltaz]
        self.update()
        
    def mousePressEvent(self,event):
        # When clicked on the window...
         self.last_pos = event.pos()
         modifiers = QtWidgets.QApplication.keyboardModifiers()
         if(event.buttons() & Qt.LeftButton and modifiers == Qt.ControlModifier):
                 #... if ctrl is pressed
                 x = event.x()
                 y = float(self.viewport[3]) -event.y()
                 z = 0.0
                 z = glReadPixels( x, y, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT)
                 # used for :GCP digitalization (GCP approach)
                 self.result = gluUnProject( x, y, z, self.modelview, self.projection, self.viewport)
                 # emit signal to the GCP model when clicked in 3D viewer
                 self.getGCPIn3DviewSignal.emit()

         if(event.buttons() & Qt.LeftButton and modifiers == Qt.AltModifier):
                 #... if ctrl is pressed
                 x = event.x()
                 y = float(self.viewport[3]) -event.y()
                 z = 0.0
                 z = glReadPixels( x, y, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT)
                 # used for fixing position of camera in 3D viewer (GCP approach)
                 self.result = gluUnProject( x, y, z, self.modelview, self.projection, self.viewport)
                 # emit signal for fixing position (self.pos of getGCPMainWindow)
                 self.fixPositionSignal.emit(self.result)

        
    def mouseMoveEvent(self,event):
        # Translate or rotate the view position in axis x and y (side and vertical direction)
        dx = event.x() - self.last_pos.x()
        dy = event.y() - self.last_pos.y()
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if (event.buttons() & Qt.RightButton):
            # Rotate the view in axis x and y (side and vertical direction)
            self.rotateBy(dy*2, 0, 0)
            self.rotateBy(0, 0, 2*dx)
        elif (event.buttons() & Qt.LeftButton & (modifiers!= Qt.ControlModifier)):

            # translate the view in axis x and y (side and vertical direction)
            self.PanBy(dx*2, 0, 0)
            self.PanBy(0, 0, 2*dy)
        elif (event.buttons() & Qt.MidButton):
            # translate the view in front direction (finer than wheelEvent)
            self.PanByMid(dy*2)
        self.last_pos = event.pos()
        self.update()
        
    def PanByMid(self,delta): 
        # translate the view in front direction (finer than wheelEvent)
        xk = self.pos[0]-self.lookat[0]
        yk = self.pos[1]-self.lookat[1]
        zk = self.pos[2]-self.lookat[2]
        n = sqrt((xk)**2+(yk)**2+(zk)**2)
        vect = array([xk,yk,zk])
        vect = old_div(vect,linalg.norm(vect))
        deltax =  vect[0]*delta
        deltay =  vect[1]*delta
        deltaz =  vect[2]*delta
        self.pos = [self.pos[0]+deltax, self.pos[1]+deltay,self.pos[2]+deltaz]
        self.lookat = [self.lookat[0]+deltax, self.lookat[1]+deltay,self.lookat[2]+deltaz]
        self.update()
        
    def PanBy(self, x, y, z): 
        # translate the view in axis x and y (side and vertical direction)
        xk = self.pos[0]-self.lookat[0]
        yk = self.pos[1]-self.lookat[1]
        zk = self.pos[2]-self.lookat[2]
        n = sqrt((xk)**2+(yk)**2+(zk)**2)
        vectPlan = cross(array([0,1,0]),array([xk,yk,zk]))
        vectPlan = old_div(vectPlan,linalg.norm(vectPlan))
        vectZ= cross(vectPlan,array([xk,yk,zk]))
        vectZ = old_div(vectZ,linalg.norm(vectZ))
        deltax = old_div(x * vectPlan[0]*self.res,5)
        deltay = old_div(z * vectZ[1]*self.res,5)
        deltaz = old_div(x * vectPlan[2]*self.res,5)
        
        self.pos = [self.pos[0]+deltax, self.pos[1]+deltay, self.pos[2]+deltaz]
        self.lookat = [self.lookat[0]+deltax, self.lookat[1]+deltay,self.lookat[2]+deltaz]
               
    def rotateBy(self, x, y, z):
        # Rotate the view in axis x and y (side and vertical direction)
        xk = self.lookat[0]-self.pos[0]
        zk = self.lookat[2]-self.pos[2]
        yk = self.lookat[1]-self.pos[1]
        n = sqrt(((xk)**2+(yk)**2+(zk)**2))
        theta = arccos(old_div(yk,n))
        phi = arctan2(zk,xk)
        theta += (x/1000.0)
        phi += (z/1000.0)
        xnew = n * sin(theta)*cos(phi)
        znew = n * sin(theta)*sin(phi)
        ynew = n * cos(theta)

        self.lookat[0] = self.pos[0]+xnew
        self.lookat[1] = self.pos[1]+ynew
        self.lookat[2] = self.pos[2]+znew

        
    def paintGL(self):
        # Render the different object, fix the view pose, perspective, viewport, etc. 
        # No object are creating here !
         if self.offscreen:
              # if offscreen is activated, we render in a frame buffer
              if self.isFramBufferSupported:
                  glBindFramebuffer(GL_DRAW_FRAMEBUFFER, self.fbo)
         self.projection = []
         self.viewport = []
         self.modelview = glGetDoublev( GL_MODELVIEW_MATRIX)
         self.projection = glGetDoublev( GL_PROJECTION_MATRIX )
         self.viewport = glGetIntegerv( GL_VIEWPORT )
         if self.viewport[3] != 0:
             glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
             
             # Render the background image if needed (see comments at the beginning of the file)
             glMatrixMode(GL_PROJECTION )
             glLoadIdentity()
             glOrtho(0,1,0,1,-1,1)
             glDisable(GL_DEPTH_TEST)
             glDepthMask(GL_FALSE)
             glMatrixMode(GL_MODELVIEW)
             glLoadIdentity()
             if self.picture_name:
                 glBindTexture(GL_TEXTURE_2D, self.textureBack)
                 
                 glMatrixMode(GL_PROJECTION)
                 glLoadIdentity()
                 glOrtho(0,1,1,0,-1,1)
            
                 glColor3f(1.0, 1.0, 1.0)
                 glBegin(GL_QUADS)
                 glTexCoord2f(0,1)
                 glVertex2f(0,0)
        
                 glTexCoord2f(1,1)
                 glVertex2f(1,0)
        
                 glTexCoord2f(1,0)
                 glVertex2f(1,1)
        
                 glTexCoord2f(0,0)
                 glVertex2f(0,1)
                 glEnd()
                 glBindTexture(GL_TEXTURE_2D, 0)
             
             glDepthMask(GL_TRUE)
             glEnable(GL_DEPTH_TEST)
             glEnable( GL_LIGHT0 )
             glColorMaterial(GL_FRONT, GL_DIFFUSE)
             glEnable(GL_COLOR_MATERIAL)
    
             ###################
             # Render the DEM, either with shadow and light, either with a drapped ortho-image
             glColor(1,1,1,self.transparency/float(100))
    
             if not self.useOrthoImage:
                 glEnable( GL_LIGHTING )
             glMatrixMode(GL_MODELVIEW)
             
             glPolygonMode(GL_FRONT, GL_FILL)
             glLoadIdentity()
             glLightfv( GL_LIGHT0, GL_POSITION, [0,0,1,1])
             gluLookAt( self.pos[0],  self.pos[1],  self.pos[2],
                    self.lookat[0], self.lookat[1], self.lookat[2],
                    self.upWorld[0], self.upWorld[1], self.upWorld[2])
                     #0.0, cos(self.roll), sin(self.roll))
            
             glMatrixMode(GL_PROJECTION)
             glLoadIdentity()
             gluPerspective(self.FOV , 1.0*self.viewport[2]/self.viewport[3], self.resolution , 10000*self.resolution)
             #top = self.resolution*tan(self.FOV/2*pi/180)
             #bottom = -top+0.1
             #right = self.resolution*tan(self.FOV/2*pi/180)*self.viewport[2]/self.viewport[3]
             #left = -right+0.1
             #glFrustum(left, right, bottom, top, self.resolution , 10000*self.resolution)
             glEnableClientState( GL_VERTEX_ARRAY )
             if self.useOrthoImage:
                 glEnableClientState(GL_TEXTURE_COORD_ARRAY)
                 glBindTexture(GL_TEXTURE_2D, self.textures)
             else:
                 glEnableClientState( GL_NORMAL_ARRAY )
             
             
             glBindBuffer( GL_ELEMENT_ARRAY_BUFFER, self.m_indicebuffer)
             glBindBuffer( GL_ARRAY_BUFFER, self.m_nVBOVertices )
             glVertexPointer(3,GL_FLOAT,0,None)
             glBindBuffer( GL_ARRAY_BUFFER, 0 )
             
             glBindBuffer( GL_ARRAY_BUFFER, self.m_normalbuffer )
             if self.useOrthoImage:
                glTexCoordPointer(2, GL_FLOAT, 0, None)
             else:
                  glNormalPointer(GL_FLOAT,0,None)
             glBindBuffer( GL_ARRAY_BUFFER, 0 )
             
             glDrawElements(GL_TRIANGLE_STRIP,self.count,GL_UNSIGNED_INT,None)
             
             glBindBuffer( GL_ELEMENT_ARRAY_BUFFER, 0 )
             if self.useOrthoImage:
                 glBindTexture(GL_TEXTURE_2D, 0)
             else:
                 glDisableClientState( GL_NORMAL_ARRAY )
                 
             glDisableClientState( GL_VERTEX_ARRAY )
             
             #################
             glDisable( GL_LIGHTING )
             glEnable (GL_BLEND)
             glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)   
             glColor3f(   1.0,  1.0, 1.0 )
             
             for x0,y0,z0 in self.sheeps:
                 distance = sqrt((x0-self.pos[0])**2+(y0-self.pos[1])**2+(z0-self.pos[2])**2)
                 sizeCube = self.sheepsSize+(distance/float(self.distanceMax))*2.0*self.sheepsSize
                 cube = sizeCube*self.cube
                 indice = 0
                 for table in cube:
                     a= self.colorSheep[indice]
                     glBegin(GL_POLYGON)
                     glColor3fv(a)
                     indice +=1
                     for x,y,z in table:
                         glVertex3f(  x+x0, y+y0, z+z0)
                     glEnd()
    
             glColor3f(1.0,  1.0, 1.0 )
             
             self.modelview = []
             self.projection = []
             self.viewport = []
             self.modelview = glGetDoublev( GL_MODELVIEW_MATRIX)
             self.projection = glGetDoublev( GL_PROJECTION_MATRIX )

             self.viewport = glGetIntegerv( GL_VIEWPORT )
         
    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

    def initializeGL(self):
        # Create object for rendering in paintGL
        # No rendering here !
        if self.offscreen:
            if self.isFramBufferSupported:
                self.fbo = glGenFramebuffers(1)
                self.render_buf = glGenRenderbuffers(1)
                glBindRenderbuffer(GL_RENDERBUFFER, self.render_buf)
                glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH_COMPONENT, self.size0 , self.size1)
                glBindFramebuffer(GL_FRAMEBUFFER, self.fbo)
                glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_RENDERBUFFER, self.render_buf)
                #glBindFramebuffer(GL_FRAMEBUFFER, 0)
            
        glClearColor(1.0,1.0,1.0,1.0)
        if self.picture_name:
            glEnable(GL_TEXTURE_2D)
            self.textureBack = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, self.textureBack)
            img = QtGui.QImage(self.picture_name)

            img = QGLWidget.convertToGLFormat(img)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width(), img.height(),
                    0, GL_RGBA, GL_UNSIGNED_BYTE, img.bits().asstring(img.numBytes()))
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
            glBindTexture(GL_TEXTURE_2D, 0)
        else:
            glDisable(GL_TEXTURE_2D)
        
        glEnable(GL_NORMALIZE)
        self.resolution = self.numpy_verts[0,2]-self.numpy_verts[1,2]
        self.distanceMax = float(self.resolution*self.l_est)
        if self.useOrthoImage:

            glEnable(GL_TEXTURE_2D)
            self.textures = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, self.textures)
            
            ortho_box =  self.ortho_box
            img = QtGui.QImage(self.ortho_name)

            img = img.convertToFormat(QtGui.QImage.Format_RGB888)

            img = QGLWidget.convertToGLFormat(img)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.width(), img.height(),
                    0, GL_RGBA, GL_UNSIGNED_BYTE, img.bits().asstring(img.numBytes()))
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER)
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER)
            glBindTexture(GL_TEXTURE_2D, 0)
            
            self.texture = zeros((self.l_est*self.l_nord,2))
            self.texture[:,0] = old_div((ortho_box[0]-self.numpy_verts[:,0]),(ortho_box[0]-ortho_box[2]))
            self.texture[:,1] = old_div((ortho_box[1]-self.numpy_verts[:,2]),(ortho_box[1]-ortho_box[3]))
            self.numpy_texture = array(self.texture, dtype=float32)


        temp = glGenBuffers(3)
        self.m_nVBOVertices = int(temp[0])           
        self.m_indicebuffer = int(temp[1])
        self.m_normalbuffer = int(temp[2]) 
        glBindBuffer( GL_ARRAY_BUFFER, self.m_nVBOVertices )
        glBufferData( GL_ARRAY_BUFFER, self.numpy_verts, GL_STATIC_DRAW )

        glBindBuffer( GL_ARRAY_BUFFER, 0 )
        glBindBuffer( GL_ELEMENT_ARRAY_BUFFER, self.m_indicebuffer)
        glBufferData( GL_ELEMENT_ARRAY_BUFFER, self.m_indices, GL_STATIC_DRAW )
        glBindBuffer( GL_ELEMENT_ARRAY_BUFFER, 0) 
        
        if self.useOrthoImage:
            glBindBuffer( GL_ARRAY_BUFFER, self.m_normalbuffer)
            glBufferData( GL_ARRAY_BUFFER, self.numpy_texture, GL_STATIC_DRAW )
            glBindBuffer( GL_ARRAY_BUFFER, 0 )
        
        if not self.useOrthoImage:
            glBindBuffer( GL_ARRAY_BUFFER, self.m_normalbuffer )
            glBufferData( GL_ARRAY_BUFFER, self.m_normal, GL_STATIC_DRAW )
            glBindBuffer( GL_ARRAY_BUFFER, 0 )
            
        self.count = len(self.m_indices)

        if self.pos is None:
            self.pos = [self.numpy_verts[old_div(self.count,4)][0], self.numpy_verts[old_div(self.count,4)][1]*1.5, self.numpy_verts[old_div(self.count,4)][2]]
        if self.lookat is None:
            self.lookat = self.numpy_verts[old_div(self.count,2)]
        if self.upWorld is None:
            self.upWorld = self.numpy_verts[old_div(self.count,2)]
        
    def getErrorOnGCP(self, uvtable, XYZTable):
        result = []
        reproj = []
        self.getUnProj()
        for uv,xyz in zip(uvtable, XYZTable):
            u = uv[0]
            v = uv[1]
            x = xyz[0]
            y = xyz[1]
            z = xyz[2]
            winz = glReadPixels(u, v, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT)
            if winz == 1.0:
                result.append(-1)
            else:
                xyzUnProj = self.unProj(u, v, winz)
                errorDistance = sqrt((xyzUnProj[0]-x)**2+(xyzUnProj[2]-y)**2+(xyzUnProj[1]-z)**2)
                result.append(errorDistance)
                reproj.append(xyzUnProj)
        return result, reproj
    
    def proj(self,XYZTable):
        result = []
        for XYZ in XYZTable:
            winx, winy, winz = gluProject(-XYZ[0], XYZ[2], XYZ[1], self.modelview, self.projection, self.viewport)
            result.append((winx,winy))
        return result
    
    def getUnProj(self):
        A = dot(self.modelview, self.projection)
        self.m = linalg.pinv(A).transpose()
        
    def unProj(self,winx,winy,winz):
          input = [0,0,0,0]
          objectCoordinate = [0,0,0]
          input[0]=old_div((winx-self.viewport[0]),self.viewport[2])*2.0-1.0
          input[1]=old_div((winy-self.viewport[1]),self.viewport[3])*2.0-1.0
          input[2]=2.0*winz-1.0
          input[3]=1.0
          output = dot(self.m,input)
          if(output[3]==0.0):
             return -1
          output[3]=1.0/output[3]
          objectCoordinate[0]=-output[0]*output[3]
          objectCoordinate[1]=output[1]*output[3]
          objectCoordinate[2]=output[2]*output[3]
          return objectCoordinate
    
