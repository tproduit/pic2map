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
import qgis.core
from qgis.core import *
from qgis.gui import *
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from buffers import Buffers
from getGCPMainWindow import GetGCPMainWindow
from initialization import Initialization_dialog
from virtual3DMainWindow import Virtual3DMainWindow
from monoplotterMainWindow import MonoplotterMainWindow
from drapping import drappingMain
from ortho import viewOrtho_class
from checkOpenGLVersion import CheckVersion
s = QSettings()
import sys
# initialize Qt resources from file resouces.py

import resources
CRSERROR = 0

class Pic2Map:
  def __init__(self, iface):
    # save reference to the QGIS interface
    self.iface = iface
    self.canvas = self.iface.mapCanvas()
    
    self.u = 0
    self.v = 0
          
  def checkRequirments(self):
      #Check the openGL version
      ##ex = CheckVersion()
      ##ex.updateGL()
      ##self.isSupported = ex.isSupported
      ex = CheckVersion()
      ex.updateGL()
      # Opengl 3.0 is required for Framebuffer
      self.isFrameBufferSupported =ex.isSupported
    
      # Until now, no hard or software, apart from QGis 2.0 version, has showed problem with the plugin
      self.isSupported = 1
                            
  def initGui(self):

    # create action that will start plugin configuration
    self.action = QAction(QIcon(":/plugins/Pic2Map/icon.png"), "Pic2Map",self.iface.mainWindow())
    QObject.connect(self.action, SIGNAL("triggered()"), self.run)

    # add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&Pic2Map", self.action)

    
  def unload(self):
    # remove the plugin menu item and icon
    self.iface.removePluginMenu("&Pic2Map",self.action)
    self.iface.removeToolBarIcon(self.action)
    # disconnect form signal of the canvas

  def run(self):
      self.checkRequirments()
      if not self.isSupported:
            QMessageBox.critical(QWidget(), "Version - Error","system configuration insufficient" )
            return
      # Run the plug-in when clicked on the icon
      #Create an initialization window, where is given :
      # the landscape picture
      # the DEM
      # the ortho-image if used
      # the approach chosen for georeferencing
      self.ini = Initialization_dialog()
      self.ini.setWindowModality(Qt.ApplicationModal)
      result = self.ini.exec_()
      
      # The data are all given at the beginning
      self.picture_name = self.ini.ui.lineEdit.text()
      self.DEM_name = self.ini.ui.lineEditDEM.text()
      self.useOrtho = self.ini.ui.checkBox.isChecked()
      self.pathToData = self.ini.currentPath

      # See if OK was pressed

      if result == 1:
          try:
              img = QImage(self.picture_name)
              if img.isNull():
                  raise IOError
              a = self.DEM_name.split('.')
              if len(a) == 1:
                  raise IOError
          except IOError:
              QMessageBox.warning(QWidget(), "I/O - Error","Failed to initialize picture or DEM" )
              return
          if self.DEM_name.split('.')[1] != 'tiff' and self.DEM_name.split('.')[1] != 'tif':
              QMessageBox.warning(QWidget(), "I/O - Error","Unable to load DEM. \nDEM must be in geotiff format.\nIf you use the test data set, copy it outside the plugin folder." )
              return
          #see if orthoimage is used and load it in case it's used
          if self.useOrtho:
              #get name entered
              self.ortho_name = self.ini.ui.lineEdit_2.text()
              try:
                    #load as image for checking existence
                    img = QImage(self.ortho_name)
                    if img.isNull():
                        raise IOError
                    img = None
                    #load as raster for getting bounding box
                    fileInfo = QFileInfo(self.ortho_name)
                    baseName = fileInfo.baseName()
                    rlayer = QgsRasterLayer(self.ortho_name, baseName)
                    self.ortho_box =  [int(-rlayer.extent().xMinimum()), int(rlayer.extent().yMinimum()), int(-rlayer.extent().xMaximum()), int(rlayer.extent().yMaximum())]
              except IOError:
                   QMessageBox.warning(QWidget(), "I/O - Error","Failed to load ortho-image" )
                   return
               
          #see if orthoimage is not used and initialize
          else:
              self.ortho_name = None
              self.ortho_box = None
              
          result = self.load_dem()
          #result is 1 if dem is load correctly
          if result == 1:
              # the buffer object contains arrays used for openGL
              self.load_buffer()
              
              #Check if the GCP approach is chosen
              if self.ini.ui.radioButton.isChecked():
                  self.runGCPMainWindow(False)
                  
              #Check if the virtual 3D approach is chosen
              if self.ini.ui.radioButton_2.isChecked():
                  self.virtual3DMainWindow = Virtual3DMainWindow(self.buffers,self.picture_name, self.crs, self.pathToData)
                  self.virtual3DMainWindow.show()
                  self.virtual3DMainWindow.ui.goToMonoplotterButton.clicked.connect(self.goToMonoplotter)
                  self.virtual3DMainWindow.ui.GoToGCP.clicked.connect(self.runGCPMainWindowFromVirtual3D)

    
  
  def openOrthoWidget(self):
        # This function is called from the monoplotter for ortho-rectification.
        # It is located here because some strange behavior were observed 
        # probably because the synchronous work on 2 opengl window. 
        # They may be a more elegant solution, but it works like this...
        
        # Get the view parameters from the monoplotter
        modelview = self.monoplotter.qgl_window.modelview
        projection = self.monoplotter.qgl_window.projection
        viewport = self.monoplotter.qgl_window.viewport
        texture = self.monoplotter.texture
        
        Xmat = self.monoplotter.Xmat
        Ymat = self.monoplotter.Ymat #20150823
        
        # Create the window for ortho-rectification
        self.drappingInstance = drappingMain(self.buffers, self.picture_name,
                                          modelview,
                                          projection,
                                          viewport,
                                          texture,
                                          self.crs,
                                          self.DEM_name,
                                          self.isFrameBufferSupported,
                                          Xmat,
                                          Ymat)#20150923
        self.drappingInstance.setWindowModality(Qt.ApplicationModal)
        self.drappingInstance.show()
        
  def goToMonoplotter(self):
      # This function is called from both approach (CCP and virtual 3D)
      # It close the pose estimation window (GetGCPMainWindow or Virtual3DMainWindow)
      # and launch the monoplotter. It is not possible anymore to change the position of the view
      
      # Check if the virtual 3D approach has been used
      if hasattr(self, 'virtual3DMainWindow'):
          self.virtual3DMainWindow.close()
          self.ParamPose = self.virtual3DMainWindow.ParamPose
          
      #Check if the GCP approach has been used
      elif hasattr(self, 'gcpMainWindow'):
          self.gcpMainWindow.goToMonoplot = True

          self.gcpMainWindow.close()
          self.ParamPose = [self.gcpMainWindow.pos, self.gcpMainWindow.lookat, self.gcpMainWindow.FOV, self.gcpMainWindow.roll]
      else:
          raise  IOError
      
      # launch monoplotter
      self.monoplotter = MonoplotterMainWindow(self.iface,
                                               self.buffers,
                                               self.picture_name,
                                               self.ParamPose,
                                               self.dem_box,
                                               self.cLayer,
                                               self.pathToData,
                                               self.crs,
                                               self.DEM_name,
                                               self.isFrameBufferSupported,
                                               self.demMax, self.demMin)#
      self.monoplotter.show()
      self.monoplotter.qgl_window.updateGL()
      self.monoplotter.openOrtho.connect(self.openOrthoWidget)
      self.monoplotter.qgl_window.blow.connect(self.clickOnMonoplotter)
      self.monoplotter.ui.measureButton.clicked.connect(self.activateMeasurement)
      self.monoplotter.clearMapTool.connect(self.clearMapTool)
      self.activeFlackOnMonoplotter()

  def drawPinkCross(self, pos):
        if hasattr(self, 'pinkCross'):
            self.canvas.scene().removeItem(self.pinkCross)
        if pos[2] == 1:
            self.pinkCross = QgsVertexMarker(self.canvas)
            posi = QgsPoint(pos[0],pos[1])
            self.pinkCross.setCenter(posi)
            self.pinkCross.setColor(QColor(255, 122, 255))
            self.pinkCross.setIconSize(10)
            self.pinkCross.setIconType(QgsVertexMarker.ICON_CROSS)
            self.pinkCross.setPenWidth(10)
      

  def clearMapTool(self):
        #Call when GCP window is closed
        #Call when the tool "Measure 3D" from monoplotter is activated
        self.cTool = self.canvas.mapTool()
        self.canvas.unsetMapTool(self.cTool)
        if hasattr(self, 'monoplotter'):
            if hasattr(self.monoplotter.qgl_window, 'lineEditBuffer'):                     
                      self.monoplotter.qgl_window.lineEditBuffer = []
                      self.monoplotter.qgl_window.updateGL()

  def runGCPMainWindowFromVirtual3D(self):
        self.virtual3DMainWindow.close()
        self.ParamPose = self.virtual3DMainWindow.ParamPose
        self.runGCPMainWindow(True)
        
  def runGCPMainWindow(self, fromVirtual3D):
        # this QGIS tool emits as QgsPoint after each click on the map canvas
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        self.canvas.setMapTool(self.clickTool)
        # create main window
        self.gcpMainWindow = GetGCPMainWindow(self.iface, self.buffers, self.picture_name,self.pathToData,self.isFrameBufferSupported, self.crs)
        # show the Main Window
        self.gcpMainWindow.show()
        # load the picture in the central widget
        self.load_picture(self.picture_name)
        # get DEM reference layer
        self.gcpMainWindow.cLayer = self.cLayer
        # connect events between getGCPmainWindow and Qgis canvas
        self.gcpMainWindow.ui.tableView.selectionModel().currentRowChanged.connect(self.resetClickTool) 
        self.gcpMainWindow.resetToolSignal.connect(self.resetClickTool)
        self.gcpMainWindow.setCanvasExtentSignal.connect(self.setCanvasExtent)
        self.clickTool.canvasClicked.connect(self.newCanvasGCP)
        self.gcpMainWindow.GoToMonoplotterButton.triggered.connect(self.goToMonoplotter)
        self.gcpMainWindow.clearMapTool2.connect(self.clearMapTool)
        
        if fromVirtual3D:
            self.gcpMainWindow.pos = self.ParamPose[0]
            self.gcpMainWindow.lookat = self.ParamPose[1]
            self.gcpMainWindow.FOV = self.ParamPose[2]
            self.gcpMainWindow.roll = self.ParamPose[3] 
        
  def load_dem(self):
      try:
          #load dem for info and extent
          fileName = self.DEM_name
          fileInfo = QFileInfo(fileName)
          baseName = fileInfo.baseName()
          rlayer2 = QgsRasterLayer(fileName, baseName)
          self.dem_box = rlayer2.extent()
          
          provider = rlayer2.dataProvider()
          stats = provider.bandStatistics(1, QgsRasterBandStats.All,self.dem_box, 0)
          self.demMin = stats.minimumValue
          self.demMax = stats.maximumValue
          
         
          # Get coordinate system
          self.crs = rlayer2.crs()
         
          # check if the map units are meter
          if self.crs.mapUnits() != 0:
              raise CRSERROR
          self.iface.addRasterLayer(self.DEM_name)
          
          if not rlayer2.isValid():
              QMessageBox.warning(QWidget(), "IO - Error",
                "Raster failed to load")
              return 0
          # DEM is set such that altitude request will be done on it
          self.cLayer = rlayer2
          return 1
      except CRSERROR:
          QMessageBox.warning(QWidget(), "CRS - Error",
                "DEM must be in projected coordinates, meter units")
          return 0

  def load_picture(self, picName):
      ##s.setValue( "/Projections/defaultBehaviour", "UseProject" )
      fileName = picName
      fileInfo = QFileInfo(fileName)
      baseName = fileInfo.baseName()
      rlayer = QgsRasterLayer(fileName, baseName)
      resolution = QDesktopWidget().screenGeometry()
      size = [0,0]
      size[1] = resolution.height()/2
      size[0] = int(float(float(rlayer.width())/float(rlayer.height()))*size[1])

      if not rlayer.isValid():
            QMessageBox.warning(QWidget(), "IO - Error",
                "Picture failed to load!")
            return
      # Load the image inside the graphicsview
      self.gcpMainWindow.setImage(fileName, size)
      # Set the zoom such the picture is almost in full view in the height directon
      factor = float(self.gcpMainWindow.ui.graphicsView.size().height())/rlayer.height()
      self.gcpMainWindow.ui.graphicsView.scale(factor, factor)
      
  def resetClickTool(self):
      # This function is used for GCP digitalization.
      # It resets the click tool for getting altitude on the DEm layer (self.clayer)
      self.canvas.setMapTool(self.clickTool)
      QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"),self.newCanvasGCP)
      
  def newCanvasGCP(self,point):
      # This function is used for GCP digitalization.
      # a new GCP is created on canvas
      self.gcpMainWindow.selectCanvasPoint(point)
      self.gcpMainWindow.refreshCanvasGCP()
        
  def load_buffer(self):
        # This function is used at initialization.
        # Arrays are created here for openGL. The normal calculation can take some time (ca. 1sec for 100'000 pixels)
        self.buffers = Buffers(self.DEM_name, self.dem_box, self.useOrtho, self.ortho_name, self.ortho_box)
        self.buffers.getBuffer()
        self.buffers.close()
        
  def clickOnMonoplotter(self,customEvent):
      # This function is called when digitalization or measurement on monoplotter
      x = customEvent[0]
      y = customEvent[1]
      button = customEvent[2]
      self.monoplotter.qgl_window.notUpdate = False
      self.cTool = self.canvas.mapTool()
      
      # check if a layer is edited
      if self.cTool != None: 
          currentLayer = self.iface.activeLayer()   
          if currentLayer.type() == 0 and currentLayer.isEditable() and currentLayer.geometryType() < 3:
              if self.cTool.isEditTool():
                  if self.iface.actionAddFeature().isEnabled():
                      u,v = self.WorldToPixelOfCanvasCoordinates(x,y)
                      p = QPoint()
                      p.setX(u)
                      p.setY(v)
                      event = QMouseEvent(QEvent.MouseButtonRelease,p,button,button,Qt.NoModifier)
                      event2 = QgsMapMouseEvent(self.canvas, event)####
                      self.cTool.canvasReleaseEvent(event2)
                  # check if the edited layer is a point layer
                  if currentLayer.geometryType() == 0:
                      # Since the feature has been added in the layer, it is sufficient to refresh
                      #the monoplotter for displaying the new point
                      self.monoplotter.refreshLayers(boolSymbology = True)#True)
                  # check if the edited layer is a line layer    
                  if currentLayer.geometryType() == 1:
                      # a new point is added if the left button is clicked
                      if button == Qt.LeftButton:
                          self.monoplotter.qgl_window.lineEditBufferAppend()
                          self.monoplotter.qgl_window.updateGL()
                      # The line edition ends if the right button is clicked
                      elif button == Qt.RightButton:
                          self.monoplotter.qgl_window.lineEditBuffer = []
                          self.monoplotter.refreshLayers(boolSymbology = False)
                          
                          
                  if currentLayer.geometryType() == 2:
                      # a new point is added if the left button is clicked
                      if button == Qt.LeftButton:
                          self.monoplotter.qgl_window.lineEditBufferAppend()
                          self.monoplotter.qgl_window.updateGL()
                      # The line edition ends if the right button is clicked
                      elif button == Qt.RightButton:
                          self.monoplotter.qgl_window.lineEditBuffer = []
                          self.monoplotter.refreshLayers(boolSymbology = False)
          # check if the measuring tool is being used             
          if self.cTool.action() == self.iface.actionMeasure():
              # measurement is done if left button is clicked
              if button == Qt.LeftButton:
                  #self.cTool.activate()
                  # get the position in canvas coordinates
                  u_previous = self.u
                  v_previous = self.v
                  self.u,self.v = self.WorldToPixelOfCanvasCoordinates(x,y)
    
                  # create a mouse click at the projected location on canvas
    
                  # create a line on the monoplotter
                  
                  if u_previous != self.u or v_previous != self.v:
                     p = QPoint()
                     p.setX(self.u)
                     p.setY(self.v)
                     event = QMouseEvent(QEvent.MouseButtonRelease,p,button,button,Qt.NoModifier)
                     event2 = QgsMapMouseEvent(self.canvas, event)
                     
                     self.cTool.canvasReleaseEvent(event2)
                     self.monoplotter.qgl_window.lineEditBufferAppend()
                     self.monoplotter.qgl_window.updateGL()
                     self.cTool.activate()
                     
                  # update window
              # the line is cleared if the right button is clicked
              elif button == Qt.RightButton:
                  self.monoplotter.qgl_window.lineEditBuffer = []
                  self.monoplotter.qgl_window.updateGL()
      else:
         if self.monoplotter.isMeasuring3D:
             if button == Qt.LeftButton:
                 self.monoplotter.qgl_window.lineEditBufferAppend()
                 self.monoplotter.qgl_window.updateGL()
                 self.monoplotter.dlgMeasure3D.addPoint(x,y)
             if button == Qt.RightButton:
                 self.monoplotter.qgl_window.lineEditBuffer = []
                 self.monoplotter.qgl_window.updateGL()
                 self.monoplotter.dlgMeasure3D.removePath()
  
  def activateMeasurement(self):
      # This function is used for calling the measuring tool from the monoplotter
      self.iface.actionMeasure().trigger()
      self.monoplotter.stopMeasure3D()
      
  def disactiveFlackOnMonoplotter(self):
      self.canvas.mapTool().canvasMoveEvent = None
      self.canvas.mapTool().deactivate()
      self.canvas.unsetMapTool(self.canvas.mapTool())


  def activeFlackOnMonoplotter(self):
      self.clickTool2 = QgsMapToolEmitPoint(self.canvas)
      self.canvas.setMapTool(self.clickTool2)
      self.canvas.mapTool().canvasMoveEvent = self.test3
      self.monoplotter.qgl_window.pinkCrossSignal.connect(self.drawPinkCross)
      self.monoplotter.closingMonoplot.connect(self.disactiveFlackOnMonoplotter)
    
  def test3(self, ev):
      x,y = self.CanvastoWorldCoordinates(ev.x(), ev.y())
      self.monoplotter.preparePurpleCross(x,y)


  def WorldToPixelOfCanvasCoordinates(self,x,y):
      # This function is called in "clickOnMonoplotter".
      # It convert CSR coordinates (world) into the screen coordinates for a given point in the canvas.
      canvasExtent =  self.canvas.extent()
      canvasBox =  [canvasExtent.xMinimum(), canvasExtent.yMinimum(), canvasExtent.xMaximum(), canvasExtent.yMaximum()]
      UPP = self.canvas.mapUnitsPerPixel()
      u = int((x-canvasBox[0])/UPP)
      v = int((canvasBox[3]-y)/UPP)
      return (u,v)
  
  def CanvastoWorldCoordinates(self,u,v):
      # This function is called in "clickOnMonoplotter".
      # It convert CSR coordinates (world) into the screen coordinates for a given point in the canvas.
      canvasExtent =  self.canvas.extent()
      canvasBox =  [canvasExtent.xMinimum(), canvasExtent.yMinimum(), canvasExtent.xMaximum(), canvasExtent.yMaximum()]
      UPP = self.canvas.mapUnitsPerPixel()
      x = int(u*UPP+canvasBox[0])
      y = int(-v*UPP+canvasBox[3])
      return (x,y)
  
  def setCanvasExtent(self, pos):
      # This function is used for GCP digitalization.
      # It zoom on the canvas depending on which GCp is selected. 
      # The zoom extent is set with referenced to the size of the DEM
      offset = (self.dem_box.xMinimum()-self.dem_box.xMaximum())/50
      zoomRectangle = QgsRectangle(pos[0]-offset, pos[1]-offset,pos[0]+offset,pos[1]+offset)
      self.canvas.setExtent(zoomRectangle)
      self.canvas.refresh()

class CRSERROR(Exception):
    # Error which is raised when inadequate CRS is used
    def __init__(self, value = 0):
       self.value = value
    def __str__(self):
        return repr(self.value)

        

             
