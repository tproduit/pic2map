from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.core import *
from D3View import D3_view
from ui_d3_virtual import Ui_D3
from numpy import arctan, arctan2, sqrt, pi, cos, sin, array, zeros, dot, linalg, arcsin
from PyQt4 import QtXml

class Virtual3DMainWindow( QMainWindow):
    #The 
    def __init__(self, pointBuffer, picture_name,crs, pathToData):
        QMainWindow.__init__(self)
        self.ui = Ui_D3()
        self.crs = crs
        self.pathToData = pathToData
        #Used for development
        #self.D3_instance = D3_view(pointBuffer, picture_name, -1, 43, 50, [-650309.90862020943, 2912.780832190997, 142427.86760251521],[-634916.45638827677, 54.604401863910425, 150209.58691157124])
        self.D3_instance = D3_view(pointBuffer, picture_name,0,45,transparency = 50)
        self.pointBuffer = pointBuffer
        img = QImage(picture_name)
        img_name = picture_name.split("/")[-1]
        self.img_name = img_name.split(".")[0]
        self.picture_name = picture_name

        resolution = QDesktopWidget().screenGeometry()
        size = [0,0]
        size[1] = resolution.height()/2
        self.imgSize = [img.width(), img.height()]
        size[0] = int(self.imgSize[0]/float(self.imgSize[1])*size[1])
        
        self.ui.setupUi(self)
        self.setCentralWidget(self.D3_instance)
        self.setFixedHeight(size[1])
        self.setFixedWidth(size[0]+200)
        
        self.ui.horizontalSlider.valueChanged.connect(self.sliderroll)
        self.ui.horizontalSlider_2.valueChanged.connect(self.sliderFocal)
        self.ui.horizontalSlider_3.valueChanged.connect(self.sliderTransparency)
        self.ui.saveKMLButton.clicked.connect(self.savePoseInKML)
        self.ui.loadKMLButton.clicked.connect(self.readKML)
        
        #self.dotIt()
         
    
    def sliderroll(self, val):
        # Control the roll of the picture
        self.D3_instance.roll = val/100.0
        self.D3_instance.updateGL()
        
    def sliderFocal(self, val):
        # Control the focal of the picture
        self.D3_instance.FOV = val
        self.D3_instance.updateGL()
        
    def sliderTransparency(self, val):
        #Control the transparency of the DEM
        self.D3_instance.transparency = val
        self.D3_instance.updateGL()

    def closeEvent(self, event):    
        # When the window is closed, the parameters get fixed and are used for the monoplotter
        self.ParamPose = [self.D3_instance.pos, self.D3_instance.lookat, self.D3_instance.FOV, self.D3_instance.roll]
        
    def savePoseInKML(self):
        # Save the pose in KML file. It can be open in googleEarth 
        pos = self.D3_instance.pos
        roll = self.D3_instance.roll
        FOV = self.D3_instance.FOV
        lookat = self.D3_instance.lookat
        dx = pos[0]-lookat[0]
        dy = pos[2]-lookat[2]
        dz = pos[1]-lookat[1]
        heading = arctan2(dx,-dy)*180/pi
        tilt = arctan(-dz/sqrt(dx**2+dy**2))*180/pi+90
        
        crsSource = QgsCoordinateReferenceSystem(self.crs.postgisSrid())
        crsTarget = QgsCoordinateReferenceSystem(4326)
        xform = QgsCoordinateTransform(crsSource, crsTarget)
        WGSPos = xform.transform(QgsPoint(-pos[0],pos[2]))
        altitude = pos[1]
        est = WGSPos[0]
        nord = WGSPos[1]
        ratio = self.imgSize[0]/float(self.imgSize[1])
        leftFOV = -ratio*FOV/2.0
        rightFOV = ratio*FOV/2.0
        topFOV = FOV/2.0
        bottomFOV = -FOV/2.0
        near = 300.0
        self.writeKML(est, nord, altitude,  heading, tilt, roll, leftFOV, rightFOV, topFOV, bottomFOV, near)
        
    def writeKML(self, est, nord, altitude,  heading, tilt, roll, leftFOV, rightFOV, topFOV, bottomFOV, near):
       # Write the KML 
       
       #The path is the same as the one use for the initialization step
       path = self.pathToData + "/pose.kml"
       
       #Get the name of the saved KML file
       fName = QFileDialog.getSaveFileName(self,"save file dialog" ,path,"Images (*.kml)");
       if fName:
        f = open(fName, 'w')
        f.write(
"""<?xml version="1.0" encoding="utf-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<PhotoOverlay id="space-needle">
    <name>%s</name>
    <Camera>
      <longitude>%.10f</longitude>
      <latitude>%.10f</latitude>
      <altitude>%.10f</altitude>
      <heading>%.10f</heading>
      <tilt>%.10f</tilt>
      <roll>0.0</roll>
      <altitudeMode>absolute</altitudeMode>
    </Camera>
    <Style>
        <IconStyle>
            <Icon>
                <href>:/camera_mode.png</href>
            </Icon>
        </IconStyle>
        <ListStyle>
            <listItemType>check</listItemType>
            <ItemIcon>
                <state>open closed error fetching0 fetching1 fetching2</state>
                <href>http://maps.google.com/mapfiles/kml/shapes/camera-lv.png</href>
            </ItemIcon>
            <bgColor>00ffffff</bgColor>
            <maxSnippetLines>2</maxSnippetLines>
        </ListStyle>
    </Style>
    <Icon>
      <href>%s</href>
    </Icon>
    <rotation>%.10f</rotation>
    <ViewVolume>
      <leftFov>%.10f</leftFov>
      <rightFov>%.10f</rightFov>
      <bottomFov>%.10f</bottomFov>
      <topFov>%.10f</topFov>
      <near>%.10f</near>
    </ViewVolume>
    <Point>
      <altitudeMode>absolute</altitudeMode>
      <coordinates>%.10f,%.10f,%.10f</coordinates>      
    </Point>
</PhotoOverlay>
</kml>"""  % (self.img_name, est, nord, altitude, 
                      heading, tilt, self.picture_name, roll,
                      leftFOV,rightFOV,bottomFOV,topFOV,near,
                      est,nord,altitude) ) 
        f.close()
       
    def readKML(self):
        # Read a KML file created by th plugin or a KML for a picture pose in google Earth
        path = self.pathToData + "/pose.kml"
        fName = QFileDialog.getOpenFileName(self, 'Open file',path,("Kml (*.kml)"))
        if not fName:
            return
        file=QFile(fName)

        if (not file.open(QIODevice.ReadOnly | QIODevice.Text)):
            QMessageBox.warning(self, 'Application', QString('Cannot read file %1:\n%2.').arg(fname).arg(file.errorString()))
            return False
        else:
            doc = QtXml.QDomDocument("EnvironmentML");
            if(not doc.setContent(file)):
                file.close()
                QMessageBox.warning(self,"Error","Could not parse xml file.")
            file.close()
            root = doc.documentElement();
            if(root.tagName()!="kml"):
                 QMessageBox.warning(self,"Error","Could not parse xml file. Root Element must be <kml/>.")
            else:
                try:
                    longitude = float(doc.elementsByTagName('longitude').at(0).firstChild().toText().data())
                    latitude = float(doc.elementsByTagName('latitude').at(0).firstChild().toText().data())
                    altitude = float(doc.elementsByTagName('altitude').at(0).firstChild().toText().data())
                    Heading = float(doc.elementsByTagName('heading').at(0).firstChild().toText().data())
                    Tilt = float(doc.elementsByTagName('tilt').at(0).firstChild().toText().data())
                    Roll = float(doc.elementsByTagName('roll').at(0).firstChild().toText().data())
                    try:
                        altitudeMode = doc.elementsByTagName('altitudeMode').at(0).firstChild().toText().data()
                    except:
                        altitudeMode = doc.elementsByTagName('gx:altitudeMode').at(0).firstChild().toText().data()
                    leftFov = float(doc.elementsByTagName('leftFov').at(0).firstChild().toText().data())
                    rightFov = float(doc.elementsByTagName('rightFov').at(0).firstChild().toText().data())
                    bottomFov = float(doc.elementsByTagName('bottomFov').at(0).firstChild().toText().data())
                    topFov = float(doc.elementsByTagName('topFov').at(0).firstChild().toText().data())
                    try:
                        Rotation = float(doc.elementsByTagName('rotation').at(0).firstChild().toText().data())
                    except:
                        Rotation = 0
                except:
                     QMessageBox.warning(QMainWindow(),"Error","Could not use xml file. Problem parsing.")
                else:
                    #The focal has to be centered
                    if leftFov != -1*rightFov or bottomFov != -1*topFov:
                         QMessageBox.warning(QMainWindow(),"Error","Could not use xml file. Problem of field of view definition.")
                    #Only the absolute elevation is possible. The mode "above the ground" is not supported
                    if altitudeMode != 'absolute':
                         QMessageBox.warning(QMainWindow(),"Error","Could not use xml file. Problem of altitude definition.")
                    #The has to be near zero given the construction of the KML. The roll is not given by the Roll, but by Rotation
                    if Roll > 0.1:
                         QMessageBox.warning(QMainWindow(),"Error","Could not use xml file. Problem of roll definition.")
                    #Check if the latitude and longitude are valid
                    if latitude > 91 or latitude < -91 or longitude > 361 :
                         QMessageBox.warning(QMainWindow(),"Error","Could not use xml file. Problem of coordinates definition.")
                    
                    # Transform the position coordinates from wgs84 to the DEM coordinate system
                    crsTarget = QgsCoordinateReferenceSystem(self.crs.postgisSrid())
                    crsSource = QgsCoordinateReferenceSystem(4326)
                    xform = QgsCoordinateTransform(crsSource, crsTarget)
                    LocalPos = xform.transform(QgsPoint(longitude,latitude))
                    pos = array([-LocalPos[0], altitude, LocalPos[1]])
                    FOV = 2*topFov
                    heading = Heading/180.0*pi
                    roll = Rotation/180.0*pi
                    tilt = Tilt/180.0*pi
                    
                    try:
                        swing = arcsin(sin(roll)/(-sin(tilt)))
                    except ZeroDivisionError:
                        swing = 0

                    #Create a rotation matrix . the point [0,0,-1] is rotated for the openGL "lookat" function.
                    R = zeros((3,3))
                    R[0,0] = -cos(heading)*cos(swing)-sin(heading)*cos(tilt)*sin(swing)
                    R[0,1] =  sin(heading)*cos(swing)-cos(heading)*cos(tilt)*sin(swing) 
                    R[0,2] = -sin(tilt)*sin(swing)
                    R[1,0] =  cos(heading)*sin(swing)-sin(heading)*cos(tilt)*cos(swing)
                    R[1,1] = -sin(heading)*sin(swing)-cos(heading)*cos(tilt)*cos(swing) 
                    R[1,2] = -sin(tilt)*cos(swing)
                    R[2,0] = -sin(heading)*sin(tilt)
                    R[2,1] = -cos(heading)*sin(tilt)
                    R[2,2] =  cos(tilt)
                    
                    not_awesome_vector = array([0,0,-1])
                    fast_awesome_vector = dot(linalg.inv(R),not_awesome_vector)
                    awesome_vector = array(fast_awesome_vector)+array([LocalPos[0], LocalPos[1] , altitude])
                    lookat = array([-awesome_vector[0], awesome_vector[2], awesome_vector[1]])
                    
                    # Get parameters for pose in openGL
                    self.D3_instance.roll = roll
                    self.D3_instance.FOV = FOV
                    self.D3_instance.pos = pos
                    self.D3_instance.lookat = lookat
                    self.D3_instance.updateGL()
                    
    def dotIt(self):
        #This function creates funny words in your DEM
        #p0 is the start point of your word
        #For enable this function, uncomment it in the __init__ function
        p0 = (-585380.822346,600, 114670.765464)
        table = {}
        table['A'] = [(0,0),(0.5,1),(1,2),(1.5,3),(2,4),(2.5,3),(3,2),(3.5,1),(4,0),(1.5,1),(2.5,1)] #A
        table['B'] = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(2,1),(1,1.5),(1,2.5),(2,3.5),(1,4)]
        table['C'] = [(0,1),(0,2),(0,3),(1,4),(2,4),(1,0),(2,0)]
        table['D'] = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(2,0.5),(2,1.5),(1,4),(2,2.5),(2,3.5)]
        table['E'] = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(2,0),(1,2),(1,4),(2,4)]
        table['F'] = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,2),(1,4),(2,4)] #F
        table['G'] = [(0.5,0),(1,0),(2,0),(3,0.5),(3,1),(2.5,1.5),(0,1),(0,2),(0,3),(0.5,4),(1,4),(2,4)] #G
        table['H'] = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,2),(2,0),(2,1),(2,2),(2,3),(2,4)] #H
        table['I'] = [(0,0),(1,0),(2,0),(1,1),(1,2),(1,3),(1,4),(0,4),(2,4)] #I
        table['J'] = [(0,0),(0,1),(1,0),(2,0),(2,1),(2,2),(2,3),(2,4),(1,4),(0,4)]
        table['K'] = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,2),(2,1),(3,0),(2,3),(3,4)] #K
        table['L'] = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(2,0)] #L
        table['M'] = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,3.5),(2,3),(3,3.5),(4,0),(4,1),(4,2),(4,3),(4,4)]
        table['N'] = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,3),(2,2),(3,1),(4,0),(4,1),(4,2),(4,3),(4,4)] #N
        table['O'] = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,4),(2,0),(2,1),(2,2),(2,3),(2,4)] #O
        table['P'] = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,2),(1,4),(2,4),(2,3),(2,2)] #P
        table['Q'] = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,4),(2,0),(2,1),(2,2),(2,3),(2,4),(3,0)] #Q
        table['R'] = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,2),(1,4),(2,4),(2,3),(2,2),(1,1),(2,0)] #R
        table['S'] = [(0,0),(1,0),(2,1),(1,2),(0,3),(1,4),(2,4)] #S
        table['T'] = [(2,0),(2,1),(2,2),(2,3),(2,4),(0,4),(1,4),(2,4),(3,4),(4,4)] #T
        table['U'] = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(2,0),(2,1),(2,2),(2,3),(2,4)] #U
        table['V'] = [(2,0),(1.5,1),(1,2),(0.5,3),(0,4),(2.5,1),(3,2),(3.5,3),(4,4)] #V
        table['W'] = [(2,0),(1.5,1),(1,2),(0.5,3),(0,4),(2.5,1),(3,2),(3.5,1),(4,0),(4.5,1),(5,2),(5.5,3),(6,4)] #W
        table['X'] = [(0,4),(1,3),(2,2),(3,1),(4,0),(0,0),(1,1),(3,3),(4,4)] #X
        table['Y'] = [(0,4),(1,3),(2,2),(0,0),(1,1),(3,3),(4,4)] #Y
        table['Z'] = [(0,4),(1,4),(2,4),(3,4),(1,1),(2,2),(3,3),(1,0),(2,0),(3,0),(4,0)] #X
        table[' '] = []
        
        LASIG = []
        word = list('SALUT')
        letterOffset = 0
        
        for letterIndice in word:
            letter = table[letterIndice]
            x_max = 0
            for x,z in letter:
                if x > x_max:
                    x_max = int(x)
                x += letterOffset
                LASIG.append([x,z])
            letterOffset += int(x_max+2)       
        self.D3_instance.updateSheeps(LASIG, p0)

       

