
"""
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
This file contains the algorithm of pose estimation. It is therefore the
most computational and the only one with non-trivial mathematical
expressions.

Part of this file has been written by Marcos Duarte - duartexyz@gmail.com.
More precisely, Marcos has written the functions DLTcalibration and Normalization.
"""
from __future__ import division
from __future__ import print_function

from builtins import str
from builtins import range
from past.utils import old_div
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .ui_pose import Ui_Pose
from copy import copy
from numpy import any, zeros, array, sin, cos, dot, linalg, pi, asarray, mean, shape, sqrt, flipud, std, concatenate, ones, arccos, arcsin, arctan,arctan2, size, abs, matrix, diag, nonzero
from .reportDialog import ReportDialog
from osgeo import ogr, osr
from qgis.core import *
from qgis.gui import *
import os

class Pose_dialog(QtWidgets.QDialog):
    update = pyqtSignal()
    def __init__(self, model, paramPosIni, positionFixed, sizePicture, whoIsChecked,pathToData,picture_name, iface,crs):
        #QtGui.QDialog.__init__(self)
        QtWidgets.QDialog.__init__(self)
        self.uiPose = Ui_Pose()
        self.uiPose.setupUi(self)
        #self.center()
        self.done = False
        self.sizePicture = sizePicture
        self.model = model
        self.whoIsChecked = whoIsChecked
        self.pathToData = pathToData
        self.xyzUnProjected = None
        self.picture_name = picture_name
        self.paramPosIni = paramPosIni
        self.iface = iface
        self.crs = crs
                
        self.uiPose.commandLinkButton.clicked.connect(self.estimatePose)
        self.uiPose.reportButton.clicked.connect(self.showReportOnGCP)
        self.uiPose.cameraPositionButton.clicked.connect(self.savePositionCamera)
        
        #Set previous estimated value to text boxes
        indice = 0
        for line in self.findChildren(QtWidgets.QLineEdit):
                value = self.paramPosIni[indice]
                if indice == 0:
                    value *= -1
                if indice > 2 and indice < 6:
                    value *= old_div(180,pi)
                if indice == 7:
                    value -= old_div(self.sizePicture[0],2)
                if indice == 8:
                    value -= old_div(self.sizePicture[1],2)
                line.setText(str(round(value,3)))
                indice +=1
        
        indice = 0
        for radio in self.findChildren(QtWidgets.QRadioButton):
            radio.setChecked(self.whoIsChecked[indice])
            indice +=1
                
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def reportOnGCPs(self):
        self.report = ReportDialog(self.model, self.Qxx, self.parameter_bool, self.result, self.pathToData, self.xyzUnProjected)
        
    def showReportOnGCP(self):
        if hasattr(self, 'report'):
            self.report.setWindowModality(Qt.ApplicationModal)
            self.report.show()
            result = self.report.exec_()
        else:
            QMessageBox.warning(self, "Estimation - Error",
                    "There is currently no estimation of position done with GCPs")
        
    def estimatePose(self):
        
        #Function called when the user press "Estimate Pose"
        """
        Read the model (table) and get all the values from the 5th first columns
    
        In the least square (which is opposed to the total least square), a relation
        is found between ordinates (x) and observationservations (y). The least square 
        algorithms gives an error probability on observationservations but consider
        true ordinates.
        Column 1 and 2 are seen has observationservations.
        Columns 3,4,5 form the ordinate on which the observationservation in done.
        """
        model = self.model
        rowCount = model.rowCount()
        rowCountEnable = 0
        for row in range(0,rowCount):
            if model.data(model.index(row,5)) == 1:
                rowCountEnable +=1

        xyz = zeros((rowCountEnable, 3))
        uv1 = zeros((rowCountEnable,2))
        indice = 0
        for row in range(0,rowCount):
                if model.checkValid(row)==0:
                    continue
                if model.data(model.index(row,5)) == 0:
                    continue
                index = model.index(row, 0)
                uv1[indice,0] = model.data(index)
                index = model.index(row,1)
                uv1[indice,1] = model.data(index)
                index = model.index(row,2)
                xyz[indice,0] = -model.data(index)
                index = model.index(row,3)
                xyz[indice,1] = model.data(index)
                index = model.index(row,4)
                xyz[indice,2] = model.data(index)
                indice +=1
                
        # self.xyzUsed are GCP which have 6th column enabled 
        self.xyzUsed = array([-1*xyz[:,0],xyz[:,1],xyz[:,2]]).T
        
        table = self.findChildren(QtWidgets.QLineEdit)
        parameter_bool = zeros((9))
        parameter_list = []
        indice = 0
        """
        Read the list of Parameter of camera
        0. X Position 
        1. Y Position
        2. Z Position
        3. Tilt
        4. heading
        5. swing
        6. focal
        Parameters 7 and 8 are the central point. It is fixed to the center of image for convenience with openGL
        parameter_bool is an array with 0 if the parameter is fixed, or 1 if the parameter is free
        """
        
        #For each radio button (Free, Fixed, Apriori) for each parameters
        for radioButton in self.findChildren(QtWidgets.QRadioButton):
            
            
            if (radioButton.text() == "Free"):
                if radioButton.isChecked():

                    parameter_bool[indice] = int(1) # The parameters is free
                    parameter_list.append(0)
                     
            elif (radioButton.text() == "Fixed"):
                if radioButton.isChecked():

                    parameter_bool[indice] = int(0) #The parameters is fixed

                    value = float(table[indice].text())
                    if indice == 0:
                        value = -value
                    if indice > 2 and indice < 6:
                        value *=  old_div(pi,180)  #angle are displayed in degree
                    if indice == 7:
                        value += self.sizePicture[0]/2.0 #central point is displayed in reference to the center of image
                    if indice == 8:
                        value += self.sizePicture[1]/2.0  #central point is displayed in reference to the center of image
                    parameter_list.append(value)
                    
            elif (radioButton.text() == "Apriori"): #Apriori
            

                
                if radioButton.isChecked():

                    parameter_bool[indice] = int(2) #The parameters is aprior
                    
                    value = float(table[indice].text())
                    if indice == 0:
                        value = -value
                    if indice > 2 and indice < 6:
                        value *=  old_div(pi,180)  #angle are displayed in degree
                    if indice == 7:
                        value += self.sizePicture[0]/2.0 #central point is displayed in reference to the center of image
                    if indice == 8:
                        value += self.sizePicture[1]/2.0  #central point is displayed in reference to the center of image
                    parameter_list.append(value)
                
                #Incrementation of the indice of the parameters (each 3 button)
                indice += 1
            

            
                
        # We fix anyway the central point. Future work can take it into account. It is therefore used here as parameter.
        #U0
        parameter_bool[7] = 0
        parameter_list.append(old_div(self.sizePicture[0],2))
        #V0
        parameter_bool[8] = 0
        parameter_list.append(old_div(self.sizePicture[1],2))

        try:
            #Check if consistency of inputs
            if uv1.shape[0] != xyz.shape[0]:
                raise ValueError
                
            #Check if there is at least 4 GCP
            elif (uv1.shape[0] < 4):
                raise IOError("There are only %d GCP and no apriori values. A solution can not be computed. You can either provide 4 GCP and apriori values (solved with least-square) or 6 GCP (solved with DLT)" % (uv1.shape[0]))
                
            #Check if there is at least 4 GCP
            elif (uv1.shape[0] < 6) and any(parameter_bool[0:7]==1):
                raise IOError("There are only %d GCP and no apriori values. A solution can not be computed. You can either provide apriori values (solved with least-square) or 6 GCP (solved with DLT)" % (uv1.shape[0]))
                

            #Check if there is at least 6 GCP
            #if (uv1.shape[0] < 6) and any(parameter_bool[0:7]==1):
            #    raise nCorrError2
                
        except IOError as x:

            QMessageBox.warning(self, "GCP error", str(x))
            self.done = False
            
        except ValueError:
            QMessageBox.warning(self, "GCP - Error",
                    'xyz (%d points) and uv (%d points) have different number of points.' %(xyz.shape[0], uv.shape[0]))
            self.done = False
            
        else:
          
            
            if (xyz.shape[0] >= 6):
                
                if any(parameter_bool[0:7]==1):
                    #There are free values a DLT is performed
                    print ('Position is fixed but orientation is unknown')
                    print ('The orientation is initialized with DLT')
                    
                    resultInitialization, L, v, up = self.DLTMain(xyz,uv1)
                else:
                    #There is only fixed or apriori values LS is performed
                    print ('There is only fixed or apriori values LS is performed')
                    resultInitialization = parameter_list
                    

            else:
                print ('There are less than 6 GCP: every parameter must be fixed or apriori, LS is performed')
                resultInitialization = parameter_list

            
            """
            The least square works well only if the initial guess is not too far from the optimal solution
            The DLT algorithm provides good estimates of parameters.
            However, it is not possible to fix some parameter with the DLT.
            For this last task, a least square has been constructed with variable number of parameter.
            
            After the initial DLT, we get an estimate for all parameters. 
            We take the fixed parameters from the dialog box and give the initial
            guess from the DLT to free parameters. 
            """
            resultLS, Lproj, vect, up = self.LS(xyz,uv1,parameter_bool,parameter_list,resultInitialization)
            
            k = 0

            result = [0]*9
            # Length of resultLS is [9 - length of parameter_list]
            # We reconstruct the "result" vector which contains the output parameters
            for i in range(9):
                if (parameter_bool[i]==1) or (parameter_bool[i]==2):
                    result[i] = resultLS[k]
                    k +=1
                else:
                    result[i]=parameter_list[i]

            indice = 0
            
            # Set result in the dialog box
            for line in self.findChildren(QtWidgets.QLineEdit):
                value = result[indice]
                if indice == 0:
                    value *= -1
                if indice > 2 and indice < 6:
                    value *= old_div(180,pi)
                if indice == 7:
                    value-=self.sizePicture[0]/2.0
                if indice == 8:
                    value-=self.sizePicture[1]/2.0
                line.setText(str(round(value,3)))
                indice +=1
            
            #Set the variable for next computation and for openGL pose
            self.parameter_bool = parameter_bool
            self.parameter_list = parameter_list
            self.done = True
            self.result = result
            self.LProj = Lproj
            self.lookat = vect
            self.upWorld = up
            self.pos = result[0:3]
            # The focal, here calculate in pixel, has to be translated in term of vertical field of view for openGL
            self.FOV = old_div((2*arctan(float(self.sizePicture[1]/2.0)/result[6]))*180,pi) 
            self.roll = arcsin(-sin(result[3])*sin(result[5]))
            
            indice = 0
            for radio in self.findChildren(QtWidgets.QRadioButton):
                self.whoIsChecked[indice] = radio.isChecked()
                indice +=1
        
            # Update projected and reprojected points for drawing
            self.update.emit()
            # Create the report on GCP
            self.reportOnGCPs()
            self.uiPose.cameraPositionButton.setEnabled(True)

    def LS(self,abscissa,observations,PARAM,x_fix,x_ini):
        # The initial parameters are the ones from DLT but where the radio button is set as free
        x = []
        for i in range(9):
            if (PARAM[i]==1) or (PARAM[i]==2):
                #Free or apriori values
                x.append(x_ini[i])
        x = array(x)

        
        # 2D coordinates are understood as observations
        observations = array(observations)
        # 3D coordinates are understood as the abscissas
        abscissa = array(abscissa)
        npoints = size(observations[:,1])
        
        l_x = size(x)#9-size(nonzero(PARAM==0)[0])#int(sum(PARAM))#Number of free parameters
        sigmaobservationservation = 1
        Kl =  zeros(shape=(2*npoints,2*npoints))
        
        # A error of "sigmaobservationservation" pixels is a priori set
        for i in range (npoints):
            Kl[2*i-1,2*i-1]=sigmaobservationservation**2
            Kl[2*i,2*i]=sigmaobservationservation**2
        
        # The P matrix is a weight matrix, useless if equal to identity (but can be used in some special cases)    
        P=linalg.pinv(Kl);
        # A is the Jacobian matrix
        A = zeros(shape=(2*npoints,l_x))
        # H is the hessian matrix
        H = zeros(shape=(l_x,l_x))
        # b is a transition matrix
        b = zeros(shape=(l_x))
        # v contains the residual errors between observations and predictions
        v = zeros(shape=(2*npoints))
        # v_test contain the residual errors between observations and predictions after an update of H
        v_test = zeros(shape=(2*npoints))
        # x_test is the updated parameters after an update of H
        x_test = zeros(shape=(l_x))
        # dx is the update vector of x and x_test
        dx = array([0.]*l_x)
        
        
        it=-1;            
        maxit=1000;     
        # At least one iteration, dx > inc
        dx[0]=1
        # Lambda is the weightage parameter in Levenberg-marquart between the gradient and the gauss-newton parts.
        Lambda = 0.01
        # increment used for Jacobian and for convergence criterium
        inc = 0.001
        while (max(abs(dx))> inc) & (it<maxit):
            #new iteration, parameters updates are greater than the convergence criterium
            it=it+1;
            # For each observations, we compute the derivative with respect to each parameter
            # We form therefore the Jacobian matrix
            for i in range(npoints):
                #ubul and vbul are the prediction with current parameters
                ubul, vbul = self.dircal(x, abscissa[i,:], x_fix, PARAM)
                # The difference between the observation and prediction is used for parameters update
                v[2*i-1]=observations[i,0]-ubul
                v[2*i]=observations[i,1]-vbul
                for j in range(l_x):
                    x_temp = copy(x);
                    x_temp[j] = x[j]+inc
                    u2, v2 = self.dircal(x_temp,abscissa[i,:],x_fix,PARAM)
                    A[2*i-1,j]= old_div((u2-ubul),inc)
                    A[2*i,j]= old_div((v2-vbul),inc)
            # The sum of the square of residual (S0) must be as little as possible.        
            # That's why we speak of "least square"... tadadam !
            S0 = sum(v**2);
            H = dot(dot(matrix.transpose(A),P),A);
            b = dot(dot(matrix.transpose(A),P),v);
            try:
                dx = dot(linalg.pinv(H+Lambda*diag(diag(H))),b);
                x_test = x+dx;
            except:
                # The matrix is not always reversal.
                # In this case, we don't accept the update and go for another iteration 
                S2 = S0
            else:
                for i in range(npoints):
                    # We check that the update has brought some good stuff in the pocket
                    # In other words, we check that the sum of square of less than before (better least square!)
                    utest, vtest = self.dircal(x_test,abscissa[i,:],x_fix,PARAM);
                    v_test[2*i-1]=observations[i,0]-utest;
                    v_test[2*i]=observations[i,1]-vtest; 
                    S2 = sum(v_test**2);
            # Check if sum of square is less
            if S2<S0:
                Lambda = old_div(Lambda,10)
                x = x + dx
            else:
                Lambda = Lambda*10
        
        # Covariance matrix of parameters
        self.Qxx = sqrt(diag(linalg.inv(dot(dot(matrix.transpose(A),P),A))))
        
        p = zeros(shape=(len(PARAM)))
        m = 0
        #n = 0
        for k in range(len(PARAM)):
            if (PARAM[k]==1) or (PARAM[k]==2):
                p[k] = x[m]
                m = m+1
            else:
                p[k] = x_fix[k]
                #n = n+1
                
        L1p = self.CoeftoMatrixProjection(p)
        
        x0 = p[0];
        y0 = p[1];
        z0 = p[2];
        tilt = p[3];
        azimuth = p[4];
        swing = p[5];
        focal = p[6];
        u0 = p[7];
        v0 = p[8];
        
        R = zeros((3,3))
        R[0,0] = -cos(azimuth)*cos(swing)-sin(azimuth)*cos(tilt)*sin(swing)
        R[0,1] =  sin(azimuth)*cos(swing)-cos(azimuth)*cos(tilt)*sin(swing) 
        R[0,2] = -sin(tilt)*sin(swing)
        R[1,0] =  cos(azimuth)*sin(swing)-sin(azimuth)*cos(tilt)*cos(swing)
        R[1,1] = -sin(azimuth)*sin(swing)-cos(azimuth)*cos(tilt)*cos(swing) 
        R[1,2] = -sin(tilt)*cos(swing)
        R[2,0] = -sin(azimuth)*sin(tilt)
        R[2,1] = -cos(azimuth)*sin(tilt)
        R[2,2] =  cos(tilt)
        
        # Get "look at" vector for openGL pose
        ######################################
        
        #Generate vectors in camera system
        dirCam = array([0,0,-focal])
        upCam = array([0,-1,0])
        downCam = array([0,1,0])
        
        #Rotate in the world system
        dirWorld = dot(linalg.inv(R),dirCam.T)
        lookat = array(dirWorld)+array([x0,y0,z0])
        
        upWorld = dot(linalg.inv(R),upCam.T) 
        #not_awesome_vector = array([0,0,-focal])
        #almost_awesome_vector = dot(linalg.inv(R),not_awesome_vector.T)
        #awesome_vector = array(almost_awesome_vector)+array([x0,y0,z0])
        
        
        return x, L1p, lookat, upWorld#awesome_vector
    
    def CoeftoMatrixProjection(self,x):
        L1p = zeros((4,4))
        L1_line = zeros(12)
        x0 = x[0]
        y0 = x[1]
        z0 = x[2]
        tilt = x[3]
        azimuth = x[4]
        swing = x[5]
        focal = x[6]
        u0 = x[7]
        v0 = x[8]
        R = zeros((3,3))
        R[0,0] = -cos(azimuth)*cos(swing)-sin(azimuth)*cos(tilt)*sin(swing)
        R[0,1] =  sin(azimuth)*cos(swing)-cos(azimuth)*cos(tilt)*sin(swing) 
        R[0,2] = -sin(tilt)*sin(swing)
        R[1,0] =  cos(azimuth)*sin(swing)-sin(azimuth)*cos(tilt)*cos(swing)
        R[1,1] = -sin(azimuth)*sin(swing)-cos(azimuth)*cos(tilt)*cos(swing) 
        R[1,2] = -sin(tilt)*cos(swing)
        R[2,0] = -sin(azimuth)*sin(tilt)
        R[2,1] = -cos(azimuth)*sin(tilt)
        R[2,2] =  cos(tilt)
        D = -(x0*R[2,0]+y0*R[2,1]+z0*R[2,2])
        L1_line[0] = old_div((u0*R[2,0]-focal*R[0,0]),D)
        L1_line[1] = old_div((u0*R[2,1]-focal*R[0,1]),D)
        L1_line[2] = old_div((u0*R[2,2]-focal*R[0,2]),D)
        L1_line[3] = old_div(((focal*R[0,0]-u0*R[2,0])*x0+(focal*R[0,1]-u0*R[2,1])*y0+(focal*R[0,2]-u0*R[2,2])*z0),D)
        L1_line[4] = old_div((v0*R[2,0]-focal*R[1,0]),D)
        L1_line[5] = old_div((v0*R[2,1]-focal*R[1,1]),D)
        L1_line[6] = old_div((v0*R[2,2]-focal*R[1,2]),D)
        L1_line[7] = old_div(((focal*R[1,0]-v0*R[2,0])*x0+(focal*R[1,1]-v0*R[2,1])*y0+(focal*R[1,2]-v0*R[2,2])*z0),D)
        L1_line[8] = old_div(R[2,0],D)
        L1_line[9] = old_div(R[2,1],D)
        L1_line[10] = old_div(R[2,2],D)
        L1_line[11] = 1
        L1p =  L1_line.reshape(3,4)
        return L1p
    
    def DLTcalibration(self, xyz, uv):
        # written by Marcos Duarte - duartexyz@gmail.com
        """
        Methods for camera calibration and point reconstruction based on DLT.
    
        DLT is typically used in two steps: 
        1. Camera calibration. Function: L, err = DLTcalib(nd, xyz, uv). 
        2. Object (point) reconstruction. Function: xyz = DLTrecon(nd, nc, Ls, uvs)
    
        The camera calibration step consists in digitizing points with known coordinates 
         in the real space and find the camera parameters.
        At least 4 points are necessary for the calibration of a plane (2D DLT) and at 
         least 6 points for the calibration of a volume (3D DLT). For the 2D DLT, at least
         one view of the object (points) must be entered. For the 3D DLT, at least 2 
         different views of the object (points) must be entered.
        These coordinates (from the object and image(s)) are inputed to the DLTcalib 
         algorithm which estimates the camera parameters (8 for 2D DLT and 11 for 3D DLT).
        Usually it is used more points than the minimum necessary and the overdetermined 
         linear system is solved by a least squares minimization algorithm. Here this 
         problem is solved using singular value decomposition (SVD).
        With these camera parameters and with the camera(s) at the same position of the 
         calibration step, we now can reconstruct the real position of any point inside 
         the calibrated space (area for 2D DLT and volume for the 3D DLT) from the point 
         position(s) viewed by the same fixed camera(s).
        This code can perform 2D or 3D DLT with any number of views (cameras).
        For 3D DLT, at least two views (cameras) are necessary.
        """
        """
        Camera calibration by DLT using known object points and their image points.

        This code performs 2D or 3D DLT camera calibration with any number of views (cameras).
        For 3D DLT, at least two views (cameras) are necessary.
        Inputs:
         nd is the number of dimensions of the object space: 3 for 3D DLT and 2 for 2D DLT.
         xyz are the coordinates in the object 3D or 2D space of the calibration points.
         uv are the coordinates in the image 2D space of these calibration points.
         The coordinates (x,y,z and u,v) are given as columns and the different points as rows.
         For the 2D DLT (object planar space), only the first 2 columns (x and y) are used.
         There must be at least 6 calibration points for the 3D DLT and 4 for the 2D DLT.
        Outputs:
         L: array of the 8 or 11 parameters of the calibration matrix.
         err: error of the DLT (mean residual of the DLT transformation in units 
          of camera coordinates).
        """
        
        # Convert all variables to numpy array:
        xyz = asarray(xyz)
        uv = asarray(uv)
        # Number of points:
        npoints = xyz.shape[0]
        # Check the parameters:
            
        # Normalize the data to improve the DLT quality (DLT is dependent on the
        #  system of coordinates).
        # This is relevant when there is a considerable perspective distortion.
        # Normalization: mean position at origin and mean distance equals to 1 
        #  at each direction.
        Txyz, xyzn = self.Normalization(3,xyz)
        Tuv, uvn = self.Normalization(2, uv)
        # Formulating the problem as a set of homogeneous linear equations, M*p=0:
        A = []
        for i in range(npoints):
            x,y,z = xyzn[i,0], xyzn[i,1], xyzn[i,2]
            u,v = uvn[i,0], uvn[i,1]
            A.append( [x, y, z, 1, 0, 0, 0, 0, -u*x, -u*y, -u*z, -u] )
            A.append( [0, 0, 0, 0, x, y, z, 1, -v*x, -v*y, -v*z, -v] )

        # Convert A to array: 
        A = asarray(A) 
        # Find the 11 (or 8 for 2D DLT) parameters: 

        U, S, Vh = linalg.svd(A)
        # The parameters are in the last line of Vh and normalize them: 
        L = old_div(Vh[-1,:], Vh[-1,-1])
        # Camera projection matrix: 
        H = L.reshape(3,4)

        # Denormalization: 
        H = dot( dot( linalg.pinv(Tuv), H ), Txyz );
        H = old_div(H, H[-1,-1])
        L = H.flatten()
        # Mean error of the DLT (mean residual of the DLT transformation in 
        #  units of camera coordinates): 
        uv2 = dot( H, concatenate( (xyz.T, ones((1,xyz.shape[0]))) ) ) 
        uv2 = old_div(uv2,uv2[2,:]) 
        # Mean distance: 
        err = sqrt( mean(sum( (uv2[0:2,:].T - uv)**2,1 )) ) 
        return L, err

    def Normalization(self, nd,x):
        # written by Marcos Duarte - duartexyz@gmail.com
        """Normalization of coordinates (centroid to the origin and mean distance of sqrt(2 or 3)).
        Inputs:
         nd: number of dimensions (2 for 2D; 3 for 3D)
         x: the data to be normalized (directions at different columns and points at rows)
        Outputs:
         Tr: the transformation matrix (translation plus scaling)
         x: the transformed data
        """
        x = asarray(x)
        m = mean(x,0)
        if nd==2:
            Tr = array([[std(x[:,0]), 0, m[0]], [0, std(x[:,1]), m[1]], [0, 0, 1]])
        else:
            Tr = array([[std(x[:,0]), 0, 0, m[0]], [0, std(x[:,1]), 0, m[1]], [0, 0, std(x[:,2]), m[2]], [0, 0, 0, 1]])
            
        Tr = linalg.inv(Tr)

        x = dot( Tr, concatenate( (x.T, ones((1,x.shape[0]))) ) )
        x = x[0:nd,:].T
        return Tr, x


    def DLTMain(self,xyz,uv1):
        L1, err1 = self.DLTcalibration(xyz, uv1)
        L1p = array([[L1[0],L1[1],L1[2], L1[3]],[L1[4], L1[5], L1[6], L1[7]],[L1[8], L1[9], L1[10], L1[11]]])

        #Reconstruction of parameters
        D2=old_div(1,(L1[8]**2+L1[9]**2+L1[10]**2));
        D = sqrt(D2);
        u0 = D2*(L1[0]*L1[8]+L1[1]*L1[9]+L1[2]*L1[10]);
        v0 = D2*(L1[4]*L1[8]+L1[5]*L1[9]+L1[6]*L1[10]);
        x0y0z0 = dot(linalg.pinv(L1p[0:3,0:3]),[[-L1[3]],[-L1[7]],[-1]]);
        du2 = D2*((u0*L1[8]-L1[0])**2+(u0*L1[9]-L1[1])**2+(u0*L1[10]-L1[2])**2);
        dv2 = D2*((v0*L1[8]-L1[4])**2+(v0*L1[9]-L1[5])**2+(v0*L1[10]-L1[6])**2);
        du = sqrt(du2);
        dv = sqrt(dv2);
        focal = old_div((du+dv),2)

        R_mat = array([[old_div((u0*L1[8]-L1[0]),du),old_div((u0*L1[9]-L1[1]),du),old_div((u0*L1[10]-L1[2]),du)],\
                [old_div((v0*L1[8]-L1[4]),dv),old_div((v0*L1[9]-L1[5]),dv),old_div((v0*L1[10]-L1[6]),dv)],\
                [L1[8],L1[9],L1[10]]]);

        if linalg.det(R_mat) < 0:
            R_mat = -R_mat;
        R = D * array(R_mat);
        U,s,V = linalg.svd(R,full_matrices=True,compute_uv=True)
        R = dot(U,V)


        tilt = arccos(R[2,2])
        swing = arctan2(-R[0,2],-R[1,2])
        azimuth = arctan2(-R[2,0],-R[2,1])
        not_awesome_vector = array([0,0,-1])
        
        #Generate vectors in camera system
        dirCam = array([0,0,-1])
        upCam = array([0,-1,0])
        downCam = array([0,1,0])
        
        #Rotate in the world system
        dirWorld = dot(linalg.inv(R),dirCam.T)
        upWorld = dot(linalg.inv(R),upCam.T) 
        
        #almost_awesome_vector = dot(linalg.inv(R),not_awesome_vector)
        lookat = array(dirWorld)+array([x0y0z0[0,0],x0y0z0[1,0],x0y0z0[2,0]])
        
        return [x0y0z0[0,0],x0y0z0[1,0],x0y0z0[2,0],tilt,azimuth,swing,focal,u0,v0], L1p, lookat, upWorld#awesome_vector
    
    def rq(self, A): 
         Q,R = linalg.qr(flipud(A).T)
         R = flipud(R.T)
         Q = Q.T 
         return R[:,::-1],Q[::-1,:]
    
    
    
    def dircal(self,x_unkown,abscissa,x_fix,PARAM):
        p = zeros(shape=(len(PARAM)))
        m = 0
        #n = 0
        for k in range(len(PARAM)):
            if (PARAM[k]==1) or (PARAM[k]==2): #Apriori or free
                p[k] = x_unkown[m]
                m = m+1
            else:
                p[k] = x_fix[k]###############
                #n = n+1

        x1 = abscissa[0];
        y1 = abscissa[1];
        z1 = abscissa[2];
        x0 = p[0];
        y0 = p[1];
        z0 = p[2];
        tilt = p[3];
        azimuth = p[4];
        swing = p[5];
        focal = p[6];
        u0 = p[7];
        v0 = p[8];
        R = zeros((3,3))
        R[0,0] = -cos(azimuth)*cos(swing)-sin(azimuth)*cos(tilt)*sin(swing)
        R[0,1] =  sin(azimuth)*cos(swing)-cos(azimuth)*cos(tilt)*sin(swing) 
        R[0,2] = -sin(tilt)*sin(swing)
        R[1,0] =  cos(azimuth)*sin(swing)-sin(azimuth)*cos(tilt)*cos(swing)
        R[1,1] = -sin(azimuth)*sin(swing)-cos(azimuth)*cos(tilt)*cos(swing) 
        R[1,2] = -sin(tilt)*cos(swing)
        R[2,0] = -sin(azimuth)*sin(tilt)
        R[2,1] = -cos(azimuth)*sin(tilt)
        R[2,2] =  cos(tilt)
        
        ures = old_div(-focal*(R[0,0]*(x1-x0)+R[0,1]*(y1-y0)+R[0,2]*(z1-z0)),\
            (R[2,0]*(x1-x0)+R[2,1]*(y1-y0)+R[2,2]*(z1-z0)))+u0;
        vres = old_div(-focal*(R[1,0]*(x1-x0)+R[1,1]*(y1-y0)+R[1,2]*(z1-z0)),\
            (R[2,0]*(x1-x0)+R[2,1]*(y1-y0)+R[2,2]*(z1-z0)))+v0;

        return ures,vres

    def savePositionCamera(self) :
        xPos = -self.result[0]
        yPos = self.result[1]
        point = ogr.Geometry(ogr.wkbPoint)
        point.AddPoint(xPos, yPos)

        camPosName = '/' + (self.picture_name.split(".")[0]).split("/")[-1] + '_CameraPosition'
        path = self.pathToData + camPosName

        shapeSaveName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Camera Position" ,path, "Shapefile (*.shp)")
        
        filename = (shapeSaveName.split("/")[-1]).split(".")[0]
        layers = QgsProject.instance().mapLayers()
        for layer in layers:
            f = QFileInfo(layer)
            head, sep, tail = f.filePath().partition("CameraPosition")
            baseName = head + sep
            if filename == baseName :
                QgsProject.instance().removeMapLayer(f.filePath())
                canvas = self.iface.mapCanvas()
                canvas.refresh()

            
        if shapeSaveName:
            outShapefile = shapeSaveName
            outDriver = ogr.GetDriverByName("ESRI Shapefile")
            
            # Remove output shapefile if it already exists
            if os.path.exists(outShapefile):
                outDriver.DeleteDataSource(outShapefile)
            
            # Create the output shapefile
            outDataSource = outDriver.CreateDataSource(outShapefile)
            if outDataSource is None :
                QMessageBox.warning(self, "Camera Position is an active layer", "You tried to delete a camera position present in the project layer. \n The camera postion layer was remove. Please try again")
                return 0
            
            #Create projection
            camPosSRS = osr.SpatialReference()
            epsg = int(self.crs.authid().split(':')[1])
            camPosSRS.ImportFromEPSG(epsg)#2056)
            
            outLayer = outDataSource.CreateLayer(filename, camPosSRS, geom_type = ogr.wkbPoint)
            
            # Add an ID field
            XField = ogr.FieldDefn("X", ogr.OFTReal)
            outLayer.CreateField(XField)
            YField = ogr.FieldDefn("Y", ogr.OFTReal)
            outLayer.CreateField(YField)
            ZField = ogr.FieldDefn("Z", ogr.OFTReal)
            outLayer.CreateField(ZField)
            tiltField = ogr.FieldDefn("tilt", ogr.OFTReal)
            outLayer.CreateField(tiltField)
            headingField = ogr.FieldDefn("heading", ogr.OFTReal)
            outLayer.CreateField(headingField)
            swingField = ogr.FieldDefn("swing", ogr.OFTReal)
            outLayer.CreateField(swingField)
            nameField = ogr.FieldDefn("picture", ogr.OFTString)
            outLayer.CreateField(nameField)
            
            # Create the feature and set values
            featureDefn = outLayer.GetLayerDefn()
            feature = ogr.Feature(featureDefn)
            feature.SetGeometry(point)
            feature.SetField("picture", (self.picture_name.split(".")[0]).split("/")[-1])
            feature.SetField("X",-self.result[0])
            feature.SetField("Y",self.result[1])
            feature.SetField("Z",self.result[2])
            feature.SetField("tilt",self.result[3])
            feature.SetField("heading",self.result[4])
            feature.SetField("swing",self.result[5])
            outLayer.CreateFeature(feature)

            # Close DataSource
            outDataSource.Destroy()
            ret = QMessageBox.question(self, "Load Camera Position", "Do you want to load the camera position on the canvas?", QMessageBox.Yes| QMessageBox.No)
            if ret == QMessageBox.Yes : 
                self.iface.addVectorLayer(outShapefile, filename, "ogr")
