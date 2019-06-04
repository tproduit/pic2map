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

from builtins import str
from past.utils import old_div
from OpenGL.GL import *
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtOpenGL import *
from OpenGL.GLU import *
from numpy import sqrt, cos, sin, array, pi, linalg, dot
from OpenGL.GL.ARB.vertex_buffer_object import *
from OpenGL.arrays import ArrayDatatype as ADT


class QGLMonoplotter(QGLWidget):
    blow = pyqtSignal(list)
    pinkCrossSignal = pyqtSignal(list)
    def __init__(self, pointBuffer, picture_name, ParamPose, parent = None):
        super(QGLMonoplotter, self).__init__(parent)
        self.pos = ParamPose[0]
        self.lookat = ParamPose[1]
        self.FOV = ParamPose[2]
        self.roll = ParamPose[3]
        self.transparency = 0
        
        self.numpy_verts = pointBuffer.numpy_verts
        self.m_indices =  pointBuffer.m_indices
        self.m_normal =  pointBuffer.m_normal
        self.useOrtho =  isinstance(self.m_normal,int)
        self.l_nord =  pointBuffer.l_nord
        self.l_est =  pointBuffer.l_est
        self.res =  pointBuffer.res
        self.picture_name = picture_name
        self.polygonActivated = False
        
        self.PointLayers = []
        self.LineLayers = []
        self.layerType = []
        self.symbolParam = []
        self.symbolGraduations = []
        self.symbolCategories = []
        self.symbolColor = []
        self.symbolSize = []
        self.lineEditBuffer = []
        self.SizeColorindices = []
        self.polygonLayers = []
        self.ini = 1
        self.paintcount = 0
        self.labelLayers = []
        self.labelSettings = [QColor(0, 0, 0),QFont(),0,0]
        self.notUpdate = True
        self.symbolParamPolygon = []
        self.colorPolygon = []
        self.setMouseTracking(True)
        self.drawPurpleCross = False
        
    def purpleCross(self,x,y,z):
        if isinstance(y,(float,int)):
            winx, winy, winz = gluProject(x,y,z,self.modelview,self.projection,self.viewport)
            if winx > 0 and winx < self.l_x and winy > 0 and winy < self.l_y and winz < 0.9999:
                z_buff = glReadPixels( winx, winy, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT)
                # Check if the reprojection is not too close (if the point is behind a mountain)
                if old_div((winz-z_buff),sqrt(1-winz)) < 0.01:
                    self.purpleX = old_div(winx,self.l_x)
                    self.purpleY = old_div(winy,self.l_y)
                else:
                    self.purpleX = -1
                    self.purpleY = -1     
            else:
               self.purpleX = -1
               self.purpleY = -1        
            self.drawPurpleCross = True   
            return
        
    def lineEditBufferAppend(self):
        self.lineEditBuffer.append((old_div(self.currentEditX,self.l_x),old_div(self.currentEditY,self.l_y)))
        
    def clearLayers(self):
        self.PointLayers = []
        self.LineLayers = []
        self.LineSizeColorIndicesLayers = []
        self.labelLayers = []
        self.polygonLayers = []
        self.symbolParamPolygon = []
        self.colorPolygon = []
        
    def getZBuffer(self):
         zBuffer = glReadPixels( 0, 0, self.viewport[2], self.viewport[3], GL_DEPTH_COMPONENT, GL_FLOAT)
         return zBuffer
        
    def defSymbology(self, layerType,symbolParam,symbolGraduations,symbolCategories,symbolColor,symbolSize):
         self.layerType = layerType
         self.symbolParam = symbolParam
         self.symbolGraduations = symbolGraduations
         self.symbolCategories = symbolCategories
         self.symbolColor = symbolColor
         self.symbolSize = symbolSize
         
    def mousePressEvent(self,event):
         self.last_pos = event.pos()
         modifiers = QApplication.keyboardModifiers()
         print('mousePress')
         if(modifiers == Qt.ControlModifier):
                 print ('if1')
                 x = event.x()
                 self.currentEditX = x
                 y = float(self.viewport[3]) -event.y()
                 self.currentEditY = y
                 z = 0.0
                 z = glReadPixels( x, y, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT)
                 result = gluUnProject( x, y, z, self.modelview, self.projection, self.viewport)
                 if z != 1.0:
                    print('if2')
                    # If the click is done out of the DEM (above horizon), z is equal to 1.0
                    self.blow.emit([-result[0],result[2], event.button()])

    def leaveEvent(self, event):
         self.pinkCrossSignal.emit([0,0,0])
         
    def enterEvent(self, event):
        self.inside = True
                    
    def mouseMoveEvent(self,event):
         x = event.x()
         self.currentEditX = x
         y = float(self.viewport[3]) -event.y()
         self.currentEditY = y
         #z = 0.0
         z = glReadPixels( x, y, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT)
         result = gluUnProject( x, y, z, self.modelview, self.projection, self.viewport)
         if z != 1.0:
            # If the click is done out of the DEM (above horizon), z is equal to 1.0
            self.pinkCrossSignal.emit([-result[0],result[2],1])
         else :
             self.pinkCrossSignal.emit([0,0,0])
                 
    
    def pointRefresh(self, pointArrayXYZ, SizeColorArray, zBuffer, attributeTest,  labels):
        # Check which points are visible
        pointArray = []
        SizeColorIndices = []
        count = -1
        labelBool = (labels != [])
        labelArray = []
        # For each layer, we test each entity
        for x,y,z in pointArrayXYZ:
            count += 1
            if x is None or y is None or z is None:
                continue
            winx, winy, winz = gluProject(x,y,z,self.modelview,self.projection,self.viewport)

            # check if the projection fall inside the viewport area and if it is not too far (winz)
            if winx > 0 and winx < self.l_x and winy > 0 and winy < self.l_y and winz < 0.9999:
                z_buff = zBuffer[int(winx),int(winy)]
                # Check if the reprojection is not too close (if the point is behind a mountain)
                if old_div((winz-z_buff),sqrt(1-winz)) < 0.01:
                        pointArray.append((old_div(winx,self.l_x), old_div(winy,self.l_y)))
                        if attributeTest:
                            # If the symbology is graduated or categorized, we need the attribute value
                            SizeColorIndices.append(SizeColorArray[count])
                        if labelBool:
                            # if the labels are enabled for this layer, we need the label text
                            labelArray.append(labels[count])
                         
        self.PointLayers.append(pointArray)
        self.LineSizeColorIndicesLayers.append(SizeColorIndices)
        self.labelLayers.append(labelArray)
        
    def line2Refresh(self, line_array, SizeColorArray, zBuffer, attributeTest, labels):
        # check which lines are visible
        segmentArrayUV = []
        SizeColorIndices = []
        count = -1
        labelBool = (labels != [])
        labelArray = []
        # check one entity after another
        for line in line_array:
            new_segmentUV = []
            last = line[-1]
            count +=1
            isLabeled = False
            # check visibility for each vertex.
            # Different parts of the line can be visible. If it is the case, we create several segments.
            for vertex in line:
                x = vertex[0]
                y = vertex[1]
                z = vertex[2]
                if x is None or y is None or z is None:
                    continue
                winx, winy, winz = gluProject(x,y,z,self.modelview,self.projection,self.viewport)
                # check if the projection of the vertex fall inside the viewport
                if winx > 0 and winx <= self.l_x and winy > 0 and winy < self.l_y:
                    z_buff = zBuffer[int(winx),int(winy)]
                    # check if the reprojection is not too close (check if the vertex is behind a mountain)
                    if old_div((winz-z_buff),sqrt(1-winz)) < 0.01:
                        new_segmentUV.append([old_div(winx,self.l_x),old_div(winy,self.l_y)])
                        if vertex == last:
                            #If it is the last vertex, we store the segment information
                            segmentArrayUV.append(new_segmentUV)
                            new_segmentUV = []
                            if attributeTest:
                                SizeColorIndices.append(SizeColorArray[count])
                            if labelBool:
                                # check if we render the labels
                                if isLabeled:
                                    #label is given only to the first segment of the line
                                    isLabeled = False
                                    labelArray.append([' '])
                                else:
                                    labelArray.append(labels[count])
                    else:
                        if new_segmentUV != []:
                        # If the vertex is not visible and the last one was visible, we store the segment for rendering
                            segmentArrayUV.append(new_segmentUV)
                            new_segmentUV = []
                            if attributeTest:
                                SizeColorIndices.append(SizeColorArray[count])
                            if labelBool :
                                if isLabeled:
                                    isLabeled = False
                                    labelArray.append([' '])
                                else:
                                    labelArray.append(labels[count])
                                
        self.LineLayers.append(segmentArrayUV)
        self.LineSizeColorIndicesLayers.append(SizeColorIndices)
        self.labelLayers.append(labelArray)

                 
                            
    def unProj(self,winx,winy,winz):
          input = [0,0,0,0]
          objectCoordinate = [0,0,0]
          input[0]=old_div((winx-self.viewport[0]),self.viewport[2])*2.0-1.0
          input[1]=old_div((winy-self.viewport[1]),self.viewport[3])*2.0-1.0
          input[2]=2.0*winz-1.0
          input[3]=1.0
          output = dot(self.m,input)
          if(output[3]==0.0):
             return [0,0,0]
          output[3]=1.0/output[3]
          objectCoordinate[0]=-output[0]*output[3]
          objectCoordinate[1]=output[1]*output[3]
          objectCoordinate[2]=output[2]*output[3]
          return objectCoordinate
                            
    def getUnProj(self):
        A = dot(self.modelview, self.projection)
        self.m = linalg.pinv(A).transpose()
            
    def paintGL(self):
         # 1. draw the picture in the background
         # 2. render the DEM and set it completely transparent (invisible)
         # 3. render features and labels
         # 4. render line for measurement
         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
         self.paintcount += 1
         self.modelview = glGetDoublev( GL_MODELVIEW_MATRIX)
         self.projection = glGetDoublev( GL_PROJECTION_MATRIX )
         self.viewport = glGetIntegerv( GL_VIEWPORT )
         
         if self.ini: 
             self.l_x0 = float(self.viewport[2])
             self.l_y0 = float(self.viewport[3])
             self.ini = 0
             
         glEnable(GL_TEXTURE_2D)

         glMatrixMode(GL_PROJECTION )
         glLoadIdentity()
         glOrtho(0,1,0,1,-1,1)
         glDisable(GL_DEPTH_TEST)
         glDisable(GL_LIGHTING)
         glDepthMask(GL_FALSE)
         glMatrixMode(GL_MODELVIEW)
         glLoadIdentity()

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
         
         glDepthMask(GL_TRUE)
         glEnable(GL_DEPTH_TEST)

         glEnable( GL_LIGHT0 )
         glColorMaterial(GL_FRONT, GL_DIFFUSE)
         glEnable(GL_COLOR_MATERIAL)
         glShadeModel( GL_SMOOTH )
         glColor(1,0,0,self.transparency/float(100))

         glEnable( GL_LIGHTING )
         glMatrixMode(GL_MODELVIEW)
         
         glFrontFace(GL_CCW)
         glCullFace(GL_FRONT)
         glEnable(GL_CULL_FACE)
         glPolygonMode(GL_FRONT, GL_FILL)
         
         glLoadIdentity()
         glLightfv( GL_LIGHT0, GL_POSITION, [0,0,1,1])
         gluLookAt( self.pos[0],  self.pos[1],  self.pos[2],
                self.lookat[0], self.lookat[1], self.lookat[2],
                 0.0, cos(old_div(self.roll*pi,180)), sin(old_div(self.roll*pi,180)))
        
         glMatrixMode(GL_PROJECTION)
         glLoadIdentity()
         gluPerspective(self.FOV , 1.0*self.l_x0/self.l_y0, self.resolution/2.0 , 10000*self.resolution/2.0)
         
         glEnableClientState( GL_VERTEX_ARRAY )
         if not self.useOrtho:
             glEnableClientState( GL_NORMAL_ARRAY )
         glBindBufferARB( GL_ELEMENT_ARRAY_BUFFER_ARB, self.m_indicebuffer)
         glBindBufferARB( GL_ARRAY_BUFFER_ARB, self.m_nVBOVertices )
         glVertexPointer(3,GL_FLOAT,0,None)
         glBindBufferARB( GL_ARRAY_BUFFER_ARB, 0 )
         
         if not self.useOrtho:
             glBindBufferARB( GL_ARRAY_BUFFER_ARB, self.m_normalbuffer )
             glNormalPointer(GL_FLOAT,0,None)
             glBindBufferARB( GL_ARRAY_BUFFER_ARB, 0 )
         
         glDrawElements(GL_TRIANGLE_STRIP,self.count,GL_UNSIGNED_INT,None)
         
         if not self.useOrtho:
             glDisableClientState( GL_NORMAL_ARRAY )
         glDisableClientState( GL_VERTEX_ARRAY )
         glEnable (GL_BLEND)
         glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
         
         self.modelview = glGetDoublev( GL_MODELVIEW_MATRIX)
         self.projection = glGetDoublev( GL_PROJECTION_MATRIX )
         self.viewport = glGetIntegerv( GL_VIEWPORT )
         self.l_x = float(self.viewport[2])
         self.l_y = float(self.viewport[3])
         
         self.getUnProj()
         if self.polygonActivated:
             if not self.notUpdate:
                 glDisable(GL_TEXTURE_2D)
                 glDisable(GL_DEPTH_TEST)
                 glDisable(GL_LIGHTING)
                 glDepthMask(GL_FALSE)
                 count = -1
                 for polygonLayer in self.polygonLayers:
                     count += 1
                     countFeature = -1
                     for feature in polygonLayer:
                         countFeature += 1
                         Color = array(self.colorPolygon[count][countFeature])/255.0
                         glColor3f(Color[0], Color[1], Color[2])
                         glBegin(GL_POLYGON)
                         for vertex in feature:
                             glVertex3f(vertex[0],vertex[1],vertex[2])
                         glEnd()
                     
         
         glEnable(GL_TEXTURE_2D)
         glMatrixMode(GL_PROJECTION )
         glLoadIdentity()
         glOrtho(0,1,0,1,-1,1)
         glDisable(GL_DEPTH_TEST)
         glDisable(GL_LIGHTING)
         glDepthMask(GL_FALSE)
         glMatrixMode(GL_MODELVIEW)
         glLoadIdentity()
         
         if not self.notUpdate:
             if self.drawPurpleCross:
                 glPointSize(10)
                 Color = array((220,120,220))/255.0
                 glColor3f(Color[0], Color[1], Color[2])
                 glBegin(GL_POINTS)
                 glVertex2f(self.purpleX,self.purpleY)
                 glEnd()
             counter = -1
             PointCounter = -1
             LineCounter = -1
             glDisable(GL_TEXTURE_2D)
             glEnable(GL_POINT_SMOOTH)
             colLabelR, colLabelG, colLabelB, alpha = array(self.labelSettings[0].getRgb())/255.0
             # Draw feature layers
             for geomType in self.layerType:
                 counter +=1
                 segment_count = -1
                 Symbol = self.symbolParam[counter]
                 ColorArray = self.symbolColor[counter]
                 SizeArray = self.symbolSize[counter]
                 GradArray = self.symbolGraduations[counter]
                 CatArary = self.symbolCategories[counter]
                 labels = self.labelLayers[counter]
    
                 try:
                     if SizeArray == []:
                         raise ValueError

                     #Point
                     elif geomType == 0:
                         PointCounter += 1
                         PointArray = self.PointLayers[PointCounter]
                         SizeColorIndices = self.LineSizeColorIndicesLayers[counter]
                         #Simple symbology
                         if Symbol==0:
                             Size = SizeArray[0]
                             glPointSize(Size*5)
                             Color = array(ColorArray[0])/255.0
                             glColor3f(Color[0], Color[1], Color[2])
                             glBegin(GL_POINTS)
                             for x, y in PointArray:
                                 glVertex2f(x,y)
                             glEnd()
                         #Graduated symbology
                         elif Symbol==1:
                             for x, y in PointArray:
                                 segment_count += 1
                                 Size = SizeArray[SizeColorIndices[segment_count]]
                                 glPointSize(Size*5)
                                 Color = array(ColorArray[SizeColorIndices[segment_count]])/255.0
                                 glColor3f(Color[0], Color[1], Color[2])
                                 glBegin(GL_POINTS)
                                 glVertex2f(x,y)
                                 glEnd()
                         #Categorized symbology
                         elif Symbol==2:
                             for x, y in PointArray:
                                 segment_count += 1
                                 Size = SizeArray[SizeColorIndices[segment_count]]
                                 glPointSize(Size*5)
                                 Color = array(ColorArray[SizeColorIndices[segment_count]])/255.0
                                 glColor3f(Color[0], Color[1], Color[2])
                                 glBegin(GL_POINTS)
                                 glVertex2f(x,y)
                                 glEnd()
                                 
                     #Line
                     elif geomType == 1:
                         LineCounter += 1
                         LineArray = self.LineLayers[LineCounter]
                         SizeColorIndices = self.LineSizeColorIndicesLayers[counter]
                         # Simple symbology
                         if Symbol==0:
                             Size = SizeArray[0]
                             glLineWidth(Size*5+1) 
                             Color = array(ColorArray[0])/255.0
                             for segment in LineArray:
                                glBegin(GL_LINE_STRIP)
                                glColor3f(Color[0], Color[1], Color[2])
                                for x, y in segment:
                                    glVertex2f(x,y)
                                glEnd()
                         #Graduated symbology
                         elif Symbol==1:
                             for segment in LineArray:
                                segment_count +=1
                                Size = SizeArray[SizeColorIndices[segment_count]]
                                glLineWidth(Size*5+1) 
                                Color = array(ColorArray[SizeColorIndices[segment_count]])/255.0
                                glColor3f(Color[0], Color[1], Color[2])
                                glBegin(GL_LINE_STRIP)
                                for x, y in segment:
                                    glVertex2f(x,y)
                                glEnd()
                         #Categorized symbology
                         elif Symbol==2:
                             for segment in LineArray:
                                segment_count +=1
                                Size = SizeArray[SizeColorIndices[segment_count]]
                                glLineWidth(Size*5+1) 
                                Color = array(ColorArray[SizeColorIndices[segment_count]])/255.0
                                glColor3f(Color[0], Color[1], Color[2])
                                glBegin(GL_LINE_STRIP)
                                for x, y in segment:
                                    glVertex2f(x,y)
                                glEnd()

                 except ValueError:
                        QMessageBox.warning(QWidget(), "Value - Error","Failed to update vector views" )
             counter = -1
             LineCounter = -1
             PointCounter = -1
             # Draw label above the features           
             for geomType in self.layerType:
                 counter +=1
                 labels = self.labelLayers[counter] 
                 if labels != []:
                     glColor3f(colLabelR,colLabelG,colLabelB)
                     labelCounter = -1
                     
                     if geomType == 0:
                         PointCounter += 1
                         PointArray = self.PointLayers[PointCounter]
                         for x,y in PointArray:
                             labelCounter += 1
                             self.renderText(x+self.labelSettings[2]/100.0, y-self.labelSettings[3]/100.0, 0.0, str(labels[labelCounter]), self.labelSettings[1])
                     elif geomType == 1:
                         LineCounter += 1
                         LineArray = self.LineLayers[LineCounter]
                         for segment in LineArray:
                             nVert = len(segment)
                             x,y = segment[int(old_div(nVert,2))]
                             labelCounter += 1
                             self.renderText(x+self.labelSettings[2]/100.0, y-self.labelSettings[3]/100.0, 0.0, str(labels[labelCounter]), self.labelSettings[1])
                               
             if len(self.lineEditBuffer) > 0:
                glColor3f(1.0, 0.0, 0.0)
                glBegin(GL_LINE_STRIP)
                for x, y in self.lineEditBuffer:
                    glVertex2f(x, y)
                glEnd()
                
         glDepthMask(GL_TRUE)
         glEnable(GL_DEPTH_TEST)
        
         glEnable( GL_LIGHT0 )

         glColorMaterial(GL_FRONT, GL_DIFFUSE)
         glEnable(GL_COLOR_MATERIAL)
         glShadeModel( GL_SMOOTH )
         glColor(1,0,0,self.transparency/float(100))

         glEnable( GL_LIGHTING )
         glMatrixMode(GL_MODELVIEW)
         
         glFrontFace(GL_CCW)
         glCullFace(GL_FRONT)
         glEnable(GL_CULL_FACE)
         glPolygonMode(GL_FRONT, GL_FILL)
         
         glLoadIdentity()
         glLightfv( GL_LIGHT0, GL_POSITION, [0,0,1,1])
         gluLookAt( self.pos[0],  self.pos[1],  self.pos[2],
                self.lookat[0], self.lookat[1], self.lookat[2],
                 0.0, cos(self.roll), sin(self.roll))
        
         glMatrixMode(GL_PROJECTION)
         glLoadIdentity()
         gluPerspective(self.FOV , 1.0*self.l_x0/self.l_y0, self.resolution/2.0 , 10000*self.resolution/2.0)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

    def initializeGL(self):
        glEnable(GL_TEXTURE_2D)
        self.textureBack = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.textureBack)
        img = QImage(self.picture_name)
        img = QGLWidget.convertToGLFormat(img)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, img.width(), img.height(),
                0, GL_RGBA, GL_UNSIGNED_BYTE, img.bits().asstring(img.byteCount()))
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
        glBindTexture(GL_TEXTURE_2D, 0)

        glEnable(GL_NORMALIZE)
        self.x_rot = 0
        self.y_rot = 0
        self.z_rot = 0
        self.resolution = self.numpy_verts[0,2]-self.numpy_verts[1,2]

        temp = glGenBuffersARB(3)
        self.m_nVBOVertices = int(temp[0])           
        self.m_indicebuffer = int(temp[1])        
        self.m_normalbuffer = int(temp[2]) 
        glBindBufferARB( GL_ARRAY_BUFFER_ARB, self.m_nVBOVertices )
        glBufferDataARB( GL_ARRAY_BUFFER_ARB, self.numpy_verts, GL_STATIC_DRAW_ARB )

        glBindBufferARB( GL_ARRAY_BUFFER_ARB, 0 )
        glBindBufferARB( GL_ELEMENT_ARRAY_BUFFER_ARB, self.m_indicebuffer)
        glBufferDataARB( GL_ELEMENT_ARRAY_BUFFER_ARB, self.m_indices, GL_STATIC_DRAW_ARB )
        glBindBufferARB( GL_ELEMENT_ARRAY_BUFFER_ARB, 0) 
        if not self.useOrtho:
            #There is the possibility to see the DEM if the shadow option was chosen (no ortho-photo)
            
            glBindBufferARB( GL_ARRAY_BUFFER_ARB, self.m_normalbuffer )
            glBufferDataARB( GL_ARRAY_BUFFER_ARB, self.m_normal, GL_STATIC_DRAW_ARB )
            glBindBufferARB( GL_ARRAY_BUFFER_ARB, 0 )
        self.count = len(self.m_indices)

        if self.pos is None:
            self.pos = [self.numpy_verts[0][0], self.numpy_verts[0][1]*1.1, self.numpy_verts[0][2]]
        if self.lookat is None:
            self.lookat = self.numpy_verts[self.count/2.0]
