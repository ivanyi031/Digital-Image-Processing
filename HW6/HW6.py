# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HW6.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import pywt

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1050, 850)
        self.selectfile1 = QtWidgets.QPushButton(Form)
        self.selectfile1.setGeometry(QtCore.QRect(30, 10, 93, 28))
        self.selectfile1.setObjectName("selectfile1")
        self.selectfile1.clicked.connect(self.loadimage1)

        self.image1 = QtWidgets.QLabel(Form)
        self.image1.setGeometry(QtCore.QRect(40, 60, 200, 200))
        self.image1.setObjectName("image1")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 300, 51, 41))
        self.label.setObjectName("label")

        self.height = QtWidgets.QLineEdit(Form)
        self.height.setGeometry(QtCore.QRect(80, 300, 71, 31))
        self.height.setObjectName("height")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 340, 51, 41))
        self.label_2.setObjectName("label_2")

        self.bottom = QtWidgets.QLineEdit(Form)
        self.bottom.setGeometry(QtCore.QRect(80, 350, 71, 31))
        self.bottom.setObjectName("bottom")

        self.traptransform = QtWidgets.QPushButton(Form)
        self.traptransform.setGeometry(QtCore.QRect(180, 330, 93, 28))
        self.traptransform.setObjectName("traptransform")
        self.traptransform.clicked.connect(self.Trapezoidal_transform)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 390, 91, 41))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 420, 91, 41))
        self.label_4.setObjectName("label_4")

        self.yamp = QtWidgets.QLineEdit(Form)
        self.yamp.setGeometry(QtCore.QRect(120, 390, 81, 31))
        self.yamp.setObjectName("yamp")

        self.xamp = QtWidgets.QLineEdit(Form)
        self.xamp.setGeometry(QtCore.QRect(120, 430, 81, 31))
        self.xamp.setObjectName("xamp")

        self.mavytrans = QtWidgets.QPushButton(Form)
        self.mavytrans.setGeometry(QtCore.QRect(210, 410, 93, 28))
        self.mavytrans.setObjectName("mavytrans")
        self.mavytrans.clicked.connect(self.Wavy_transform)

        self.circular = QtWidgets.QPushButton(Form)
        self.circular.setGeometry(QtCore.QRect(210, 370, 81, 31))
        self.circular.setObjectName("circular")
        self.circular.clicked.connect(self.Circular_transform)

        self.image21 = QtWidgets.QLabel(Form)
        self.image21.setGeometry(QtCore.QRect(300, 70, 200, 200))
        self.image21.setObjectName("image2_1")

        self.image22 = QtWidgets.QLabel(Form)
        self.image22.setGeometry(QtCore.QRect(550, 70, 200, 200))
        self.image22.setObjectName("image2_2")

        self.image23 = QtWidgets.QLabel(Form)
        self.image23.setGeometry(QtCore.QRect(800, 70, 200, 200))
        self.image23.setObjectName("image2_3")

        self.wavelet1 = QtWidgets.QPushButton(Form)
        self.wavelet1.setGeometry(QtCore.QRect(340, 280, 93, 28))
        self.wavelet1.setObjectName("wavelet1")
        self.wavelet1.clicked.connect(self.Wavlet1_transform)

        self.wavelet2 = QtWidgets.QPushButton(Form)
        self.wavelet2.setGeometry(QtCore.QRect(610, 280, 93, 28))
        self.wavelet2.setObjectName("wavelet2")
        self.wavelet2.clicked.connect(self.Wavlet2_transform)

        self.wavelet3 = QtWidgets.QPushButton(Form)
        self.wavelet3.setGeometry(QtCore.QRect(880, 280, 93, 28))
        self.wavelet3.setObjectName("wavelet3")
        self.wavelet3.clicked.connect(self.Wavlet3_transform)

        self.Fusion = QtWidgets.QPushButton(Form)
        self.Fusion.setGeometry(QtCore.QRect(475, 330, 93, 28))
        self.Fusion.setObjectName("fusion")
        self.Fusion.clicked.connect(self.Image_Fusion)

        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setGeometry(QtCore.QRect(745, 330, 93, 28))
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.Image_Clear)
        
        self.selectfile2_1 = QtWidgets.QPushButton(Form)
        self.selectfile2_1.setGeometry(QtCore.QRect(300, 10, 93, 28))
        self.selectfile2_1.setObjectName("selectfile2")
        self.selectfile2_1.clicked.connect(self.loadimage2_1)

        self.selectfile2_2 = QtWidgets.QPushButton(Form)
        self.selectfile2_2.setGeometry(QtCore.QRect(400, 10, 93, 28))
        self.selectfile2_2.setObjectName("selectfile2")
        self.selectfile2_2.clicked.connect(self.loadimage2_2)

        self.selectfile2_3 = QtWidgets.QPushButton(Form)
        self.selectfile2_3.setGeometry(QtCore.QRect(500, 10, 93, 28))
        self.selectfile2_3.setObjectName("selectfile2")
        self.selectfile2_3.clicked.connect(self.loadimage2_3)

        self.selectfile3 = QtWidgets.QPushButton(Form)
        self.selectfile3.setGeometry(QtCore.QRect(30, 490, 93, 28))
        self.selectfile3.setObjectName("selectfile3")
        self.selectfile3.clicked.connect(self.loadimage3)

        self.image3 = QtWidgets.QLabel(Form)
        self.image3.setGeometry(QtCore.QRect(50, 550, 251, 231))
        self.image3.setObjectName("image3")

        self.SLIC = QtWidgets.QPushButton(Form)
        self.SLIC.setGeometry(QtCore.QRect(400, 620, 93, 28))
        self.SLIC.setObjectName("SLIC")
        self.SLIC.clicked.connect(self.Slic)

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(360, 570, 121, 21))
        self.label_5.setObjectName("label_5")

        self.superpixel = QtWidgets.QLineEdit(Form)
        self.superpixel.setGeometry(QtCore.QRect(470, 570, 81, 31))
        self.superpixel.setObjectName("superpixel")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(380, 680, 81, 21))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(600, 570, 121, 21))
        self.label_7.setObjectName("label_7")

        self.knum = QtWidgets.QLineEdit(Form)
        self.knum.setGeometry(QtCore.QRect(460, 670, 81, 31))
        self.knum.setObjectName("knum")

        self.Dcm = QtWidgets.QLineEdit(Form)
        self.Dcm.setGeometry(QtCore.QRect(640, 570, 81, 31))
        self.Dcm.setObjectName("Dcm")

        self.Kmean = QtWidgets.QPushButton(Form)
        self.Kmean.setGeometry(QtCore.QRect(400, 720, 93, 28))
        self.Kmean.setObjectName("Kmean")
        self.Kmean.clicked.connect(self.Kmean_calc)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.selectfile1.setText(_translate("Form", "Select File"))
        self.image1.setText(_translate("Form", "Origina lImage"))
        self.label.setText(_translate("Form", "Height"))
        self.label_2.setText(_translate("Form", "Bottom"))
        self.traptransform.setText(_translate("Form", "Trapezoidal"))
        self.label_3.setText(_translate("Form", "Y-Amplitude"))
        self.label_4.setText(_translate("Form", "X-Amplitude"))
        self.mavytrans.setText(_translate("Form", "Wavy"))
        self.circular.setText(_translate("Form", "Circular"))
        self.image21.setText(_translate("Form", "Image 1"))
        self.image22.setText(_translate("Form", "Image 2"))
        self.image23.setText(_translate("Form", "Image 3"))
        self.wavelet1.setText(_translate("Form", "Wavelet1"))
        self.wavelet2.setText(_translate("Form", "Wavelet2"))
        self.wavelet3.setText(_translate("Form", "Wavelet3"))
        self.Fusion.setText(_translate("Form", "Fusion"))
        self.clear.setText(_translate("Form", "Clear"))
        self.selectfile2_1.setText(_translate("Form", "Select image1"))
        self.selectfile2_2.setText(_translate("Form", "Select image2"))
        self.selectfile2_3.setText(_translate("Form", "Select image3"))
        self.selectfile3.setText(_translate("Form", "Select File"))
        self.image3.setText(_translate("Form", "Original Image"))
        self.SLIC.setText(_translate("Form", "SLIC"))
        self.label_5.setText(_translate("Form", "Number of pixels"))
        self.label_6.setText(_translate("Form", "Number of k"))
        self.label_7.setText(_translate("Form", "dcm"))
        self.Kmean.setText(_translate("Form", "K mean"))
    def loadimage1(self):
        try:
            self.image_path, ret= QtWidgets.QFileDialog.getOpenFileName()
            self.im1 = cv2.imread(self.image_path) # 灰階
            self.image1.setPixmap(QtGui.QPixmap(self.image_path))
            self.image1.setScaledContents(True)
            # print(image_path) 
        except:
            Error_Text = 'Failed to open image'
            QtWidgets.QMessageBox.information(None, 'Read Me', Error_Text)
    def loadimage2_1(self):
        self.imgset=[]
        try:
            self.image_path, ret= QtWidgets.QFileDialog.getOpenFileName()
            self.im21 = cv2.imread(self.image_path) # 灰階
            self.image21.setPixmap(QtGui.QPixmap(self.image_path))
            self.image21.setScaledContents(True)
            
            # print(image_path) 
        except:
            Error_Text = 'Failed to open image'
            QtWidgets.QMessageBox.information(None, 'Read Me', Error_Text)
    def loadimage2_2(self):
        try:
            self.image_path, ret= QtWidgets.QFileDialog.getOpenFileName()
            self.im22 = cv2.imread(self.image_path) # 灰階
            self.image22.setPixmap(QtGui.QPixmap(self.image_path))
            self.image22.setScaledContents(True)
            
            # print(image_path) 
        except:
            Error_Text = 'Failed to open image'
            QtWidgets.QMessageBox.information(None, 'Read Me', Error_Text) 
    def loadimage2_3(self):
        try:
            self.image_path, ret= QtWidgets.QFileDialog.getOpenFileName()
            self.im23 = cv2.imread(self.image_path) # 灰階
            self.image23.setPixmap(QtGui.QPixmap(self.image_path))
            self.image23.setScaledContents(True)
            
            # print(image_path) 
        except:
            Error_Text = 'Failed to open image'
            QtWidgets.QMessageBox.information(None, 'Read Me', Error_Text)  
    def loadimage3(self):
        try:
            self.image_path, ret= QtWidgets.QFileDialog.getOpenFileName()
            self.im3 = cv2.imread(self.image_path) # 灰階
            self.image3.setPixmap(QtGui.QPixmap(self.image_path))
            self.image3.setScaledContents(True)
            # print(image_path) 
        except:
            Error_Text = 'Failed to open image'
            QtWidgets.QMessageBox.information(None, 'Read Me', Error_Text)
    def Trapezoidal_transform(self):
        image= np.copy(self.im1)
        height = float(self.height.text())
        bottom = float(self.bottom.text())
        rows,cols =image.shape[:2]
        cx = int(cols/2)
        transform = np.zeros((rows,cols,3))
        
        for i in range(rows):
            new_h=int(height*i)
            transform[new_h,:,:]=image[i,:,:]
        h=int(height*rows)
        w=int(bottom*cols)
        for j in range(h):
            width=j/h*w+(h-j)/h*cols
            ratio=float(width/cols)
            for x in range(cols):
                transform[j,int(x*ratio),:]=transform[j,x,:]
                if(x>width):
                    transform[j,x,:]=0
        final = np.zeros((rows,cols,3))
        for j in range(h):
            width=int(j/h*w+(h-j)/h*cols)
            for x in range(width):
                offset=cx-int(width/2)
                final[j,x+offset,:]=transform[j,x,:]
        final=cv2.normalize(final,None,0,1,cv2.NORM_MINMAX)
        cv2.namedWindow("Trapezoidal Transform",0)
        cv2.resizeWindow("Trapezoidal Transform",rows,cols)
        cv2.imshow("Trapezoidal Transform",final)
    def Wavy_transform(self):
        image= np.copy(self.im1)
        xamp=float(self.xamp.text())
        yamp=float(self.yamp.text())
        transform=np.zeros((image.shape))
        rows, cols = image.shape[:2]
        for i in range(rows):
            for j in range(cols):

                offset_x =  xamp * np.cos(2 * np.pi * i / 180)
                offset_y = yamp * np.sin(2 * np.pi * j / 180) 

                if (j + offset_x < cols) and (i + offset_y < rows) and (j + offset_x > 0) and (i + offset_y > 0):
                    transform[i, j,:] = image[int(i + offset_y) % rows, int(j + offset_x) % cols,:]

                else:
                    transform[i, j,:] = 0
        transform=cv2.normalize(transform,None,0,1,cv2.NORM_MINMAX)
        cv2.namedWindow("Wavy Transform",0)
        cv2.resizeWindow("Wavy Transform",rows,cols)
        cv2.imshow("Wavy Transform",transform)
    def Circular_transform(self):
        image= np.copy(self.im1)
        rows,cols =image.shape[:2]
        cx = int(cols/2)
        cy = int(rows/2)
        transform=np.zeros((image.shape))
        for i in range(cy):
            distance=cy-i
            width=int(np.sqrt(600**2-distance**2))*2
            ratio=float(width/cols)
            for x in range(cols):
                transform[i,int(x*ratio),:]=image[i,x,:]
                transform[rows-i-1,int(x*ratio),:]=image[rows-i-1,x,:]
                if(x>width):
                    transform[i,x,:]=0
        final = np.zeros((image.shape))
        for j in range(rows):
            distance=cy-j
            width=int(np.sqrt(600**2-distance**2))*2
            for x in range(width):
                offset=cx-int(width/2)
                final[j,x+offset,:]=transform[j,x,:]
        final=cv2.normalize(final,None,0,1,cv2.NORM_MINMAX)
        cv2.namedWindow("Circular Transform",0)
        cv2.resizeWindow("Circular Transform",rows,cols)
        cv2.imshow("Circular Transform",final)
    def Wavlet1_transform(self):
        image=np.copy(self.im21)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        coeffs = pywt.dwt2(image, 'haar')
        LL, (LH, HL, HH) = coeffs
        
        wrows,wcols=LL.shape
        output=np.zeros([wrows*2,wcols*2])
        self.imgset.append([LL,LH,HL,HH])
        LL=cv2.normalize(LL,None,0,1,cv2.NORM_MINMAX)
        LH=cv2.normalize(LH,None,0,1,cv2.NORM_MINMAX)
        HL=cv2.normalize(HL,None,0,1,cv2.NORM_MINMAX)
        HH=cv2.normalize(HH,None,0,1,cv2.NORM_MINMAX)
        
        output[0:wrows,0:wcols]=LL
        output[0:wrows,wcols:2*wcols]=LH
        output[wrows:wrows*2,0:wcols]=HL
        output[wrows:wrows*2,wcols:wcols*2]=HH
        cv2.imshow("Wavelet1 Transform",output)
    def Wavlet2_transform(self):
        image=np.copy(self.im22)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        coeffs = pywt.dwt2(image, 'haar')
        LL, (LH, HL, HH) = coeffs
        wrows,wcols=LL.shape
        output=np.zeros([wrows*2,wcols*2])
        self.imgset.append([LL,LH,HL,HH])
        LL=cv2.normalize(LL,None,0,1,cv2.NORM_MINMAX)
        LH=cv2.normalize(LH,None,0,1,cv2.NORM_MINMAX)
        HL=cv2.normalize(HL,None,0,1,cv2.NORM_MINMAX)
        HH=cv2.normalize(HH,None,0,1,cv2.NORM_MINMAX)
        
        output[0:wrows,0:wcols]=LL
        output[0:wrows,wcols:2*wcols]=LH
        output[wrows:wrows*2,0:wcols]=HL
        output[wrows:wrows*2,wcols:wcols*2]=HH
        cv2.imshow("Wavelet2 Transform",output)
    def Wavlet3_transform(self):
        image=np.copy(self.im23)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        coeffs = pywt.dwt2(image, 'haar')
        LL, (LH, HL, HH) = coeffs
        wrows,wcols=LL.shape
        
        output=np.zeros([wrows*2,wcols*2])
        self.imgset.append([LL,LH,HL,HH])
        LL=cv2.normalize(LL,None,0,1,cv2.NORM_MINMAX)
        LH=cv2.normalize(LH,None,0,1,cv2.NORM_MINMAX)
        HL=cv2.normalize(HL,None,0,1,cv2.NORM_MINMAX)
        HH=cv2.normalize(HH,None,0,1,cv2.NORM_MINMAX)
        
        output[0:wrows,0:wcols]=LL
        output[0:wrows,wcols:2*wcols]=LH
        output[wrows:wrows*2,0:wcols]=HL
        output[wrows:wrows*2,wcols:wcols*2]=HH
        cv2.imshow("Wavelet3 Transform",output)
    def Image_Fusion(self):
        rows,cols = self.imgset[0][0].shape
        for  m in range(len(self.imgset)):
            if(m==0):
                LL_fusion = self.imgset[m][0]
                LH_fusion = self.imgset[m][1]
                HL_fusion = self.imgset[m][2]
                HH_fusion = self.imgset[m][3]
            else:
                for i in range(rows):
                    for j in range(cols):
                        LL_fusion[i][j]+=self.imgset[m][0][i][j]
                        if(self.imgset[m][1][i][j]>LH_fusion[i][j]):
                            LH_fusion[i][j]=self.imgset[m][1][i][j]
                        if(self.imgset[m][2][i][j]>LH_fusion[i][j]):
                            HL_fusion[i][j]=self.imgset[m][2][i][j]
                        if(self.imgset[m][3][i][j]>LH_fusion[i][j]):
                            HH_fusion[i][j]=self.imgset[m][3][i][j]
        LL_fusion = LL_fusion/(len(self.imgset))
        fusion_image=LL_fusion+LH_fusion+HL_fusion+HH_fusion
        output=np.zeros([rows*2,cols*2])
        LL_fusion=cv2.normalize(LL_fusion,None,0,1,cv2.NORM_MINMAX)
        LH_fusion=cv2.normalize(LH_fusion,None,0,1,cv2.NORM_MINMAX)
        HL_fusion=cv2.normalize(HL_fusion,None,0,1,cv2.NORM_MINMAX)
        HH_fusion=cv2.normalize(HH_fusion,None,0,1,cv2.NORM_MINMAX)
        fusion_image=cv2.normalize(fusion_image,None,0,1,cv2.NORM_MINMAX)
        output[0:rows,0:cols]=LL_fusion
        output[0:rows,cols:2*cols]=LH_fusion
        output[rows:rows*2,0:cols]=HL_fusion
        output[rows:rows*2,cols:cols*2]=HH_fusion
        cv2.imshow("Wavelet Transform of fusion",output)
        cv2.imshow("fusion image",fusion_image)
    def Image_Clear(self):
        try:
            self.imgset.clear
            self.image21.setPixmap(QtGui.QPixmap(""))
            self.image22.setPixmap(QtGui.QPixmap(""))
            self.image23.setPixmap(QtGui.QPixmap(""))
        except:
            pass
        cv2.destroyAllWindows()
    def Kmean_calc(self):
        image=np.copy(self.im3)
        data = image.reshape((-1,3))
        data=np.float32(data)
        k = int(self.knum.text())
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        kimage = center[label.flatten()]
        kimage2 = kimage.reshape((image.shape))
        cv2.imshow("After K mean",kimage2)
    def Slic(self):
        image=np.copy(self.im3)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        rows,cols=image.shape
        supixel = np.zeros(image.shape)
        #print("total pixel number:",rows*cols)
        sp = int(self.superpixel.text())
        s = int(np.sqrt(rows*cols/sp))
        #print(s)
        dcm = int(self.Dcm.text())
        center=[]
        previous_mean = []
        label= -np.ones((rows,cols),dtype=np.int16)
        distance = 10**100*np.ones((rows,cols))
        center=getcoordinate(center,rows,cols,s)
        center=adjust_center(center,image)
        for i in range(len(center)):
            x = center[i][0]
            y = center[i][1]
            previous_mean.append([image[x,y],x,y])#[Intensity,x,y]
        for t in range(10):
            x_sum=np.zeros(len(center))
            y_sum=np.zeros(len(center))
            I_sum = np.zeros(len(center))
            count = np.zeros(len(center),dtype=np.int16)
            for c in range (len(center)):
                I_c=previous_mean[c][0]
                x_c=previous_mean[c][1]
                y_c=previous_mean[c][2]
                for x in range(int(x_c-s),int(x_c+s)):
                    if(x<0 or x>=rows):
                        continue
                    for y in range(int(y_c-s),int(y_c+s)):
                        if(y<0 or y>=cols):
                            continue
                        euclidean = np.sqrt((x-x_c)**2+(y-y_c)**2)
                        intensity = np.sqrt((int(image[x][y])-I_c)**2)
                        D = np.sqrt((euclidean/s)**2+(intensity/dcm)**2)
                        if (distance[x][y]>D):
                            distance[x][y]=D
                            label[x][y]=c             
            for row in range(rows):
                for col in range(cols):
                    cluster=label[row][col]
                    count[cluster]+=1
                    x_sum[cluster]+=x
                    y_sum[cluster]+=y
                    I_sum[cluster]+=int(image[row][col])
            for i in range(len(center)):
                Im=I_sum[i]/count[i]
                xm=x_sum[i]/count[i]
                ym=y_sum[i]/count[i]
                previous_mean[i] = [Im,xm,ym]
        for i in range(rows):
                for j in range(cols):
                    supixel[i][j]=previous_mean[label[i,j]][0]
                    if(i == 0 or i==rows-1 or j==0 or j==cols-1):
                        pass
                    else:
                        if(label[i][j]!=label[i+1][j] or label[i][j]!=label[i][j+1]):
                            image[i][j]=255                
        supixel=cv2.normalize(supixel,None,0,1,cv2.NORM_MINMAX)
        cv2.imshow("superpixel",supixel)
        cv2.imshow("border",image)
        
def adjust_center(center,image):
    for i in range(len(center)):
        G=10**100
        x=center[i][0]
        y=center[i][1]
        for k in range(x-1,x+2):
            for m in range(y-1,y+2):
                gx=np.abs(image[k-1][m]-image[k+1][m])
                gy=np.abs(image[k][m-1]-image[k][m+1])
                if(G>np.sqrt(gx**2+gy**2)):
                    G=np.sqrt(gx**2+gy**2)
                    center[i][0]=k
                    center[i][1]=m
    return center
def getcoordinate(center,rows,cols,s):
    x_coordinate=[]
    y_coordinate=[]
    xs = int(s/2)
    ys = int(s/2)
    rx=int(rows/s)+1
    ry=int(cols/s)+1
    for i in range(rx):
        x_coordinate.append(xs+i*s)
    for j in range(ry):
        y_coordinate.append(ys+j*s)
    for k in range(len(x_coordinate)):
        for m in range(len(y_coordinate)):
            center.append([x_coordinate[k],y_coordinate[m]])
    return center

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())