# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HW4.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2,sys
import numpy as np
import math
import time
class Ui_Inverse(object):
    def setupUi(self, Inverse):
        Inverse.setObjectName("Inverse")
        Inverse.resize(939, 491)
        self.image = QtWidgets.QLabel(Inverse)
        self.image.setGeometry(QtCore.QRect(70, 110, 261, 241))
        self.image.setObjectName("image")

        self.selectfile = QtWidgets.QPushButton(Inverse)
        self.selectfile.setGeometry(QtCore.QRect(50, 30, 93, 28))
        self.selectfile.setObjectName("selectfile")
        self.selectfile.clicked.connect(self.loadimage)

        self.FFT = QtWidgets.QPushButton(Inverse)
        self.FFT.setGeometry(QtCore.QRect(130, 390, 93, 28))
        self.FFT.setObjectName("FFT")
        self.FFT.clicked.connect(self.FT)

        self.IDLF = QtWidgets.QPushButton(Inverse)
        self.IDLF.setGeometry(QtCore.QRect(370, 100, 93, 28))
        self.IDLF.setObjectName("IDLF")
        self.IDLF.clicked.connect(self.IdealLowpass)

        self.IDHF = QtWidgets.QPushButton(Inverse)
        self.IDHF.setGeometry(QtCore.QRect(500, 100, 93, 28))
        self.IDHF.setObjectName("IDHF")
        self.IDHF.clicked.connect(self.IdealHighpass)

        self.BLF = QtWidgets.QPushButton(Inverse)
        self.BLF.setGeometry(QtCore.QRect(370, 170, 93, 28))
        self.BLF.setObjectName("BLF")
        self.BLF.clicked.connect(self.butterworthLow)

        self.BHF = QtWidgets.QPushButton(Inverse)
        self.BHF.setGeometry(QtCore.QRect(500, 170, 93, 28))
        self.BHF.setObjectName("BHF")
        self.BHF.clicked.connect(self.butterworthHigh)

        self.GLF = QtWidgets.QPushButton(Inverse)
        self.GLF.setGeometry(QtCore.QRect(370, 250, 93, 28))
        self.GLF.setObjectName("GLF")
        self.GLF.clicked.connect(self.gaussianLow)

        self.GHF = QtWidgets.QPushButton(Inverse)
        self.GHF.setGeometry(QtCore.QRect(500, 250, 93, 28))
        self.GHF.setObjectName("GHF")
        self.GHF.clicked.connect(self.gaussianHigh)

        self.Homorphic = QtWidgets.QPushButton(Inverse)
        self.Homorphic.setGeometry(QtCore.QRect(430, 310, 93, 28))
        self.Homorphic.setObjectName("Homorphic")
        self.Homorphic.clicked.connect(self.homorphic)

        self.label = QtWidgets.QLabel(Inverse)
        self.label.setGeometry(QtCore.QRect(280, 390, 21, 16))
        self.label.setObjectName("label")

        self.cuttoff = QtWidgets.QLineEdit(Inverse)
        self.cuttoff.setGeometry(QtCore.QRect(310, 390, 51, 22))
        self.cuttoff.setObjectName("cuttoff")

        self.label_2 = QtWidgets.QLabel(Inverse)
        self.label_2.setGeometry(QtCore.QRect(380, 390, 31, 21))
        self.label_2.setObjectName("label_2")

        self.gammaH = QtWidgets.QLineEdit(Inverse)
        self.gammaH.setGeometry(QtCore.QRect(410, 390, 61, 22))
        self.gammaH.setObjectName("gammaH")

        self.label_3 = QtWidgets.QLabel(Inverse)
        self.label_3.setGeometry(QtCore.QRect(490, 390, 58, 15))
        self.label_3.setObjectName("label_3")

        self.gammaL = QtWidgets.QLineEdit(Inverse)
        self.gammaL.setGeometry(QtCore.QRect(520, 390, 51, 22))
        self.gammaL.setObjectName("gammaL")

        self.c_ = QtWidgets.QLineEdit(Inverse)
        self.c_.setGeometry(QtCore.QRect(600, 390, 51, 22))
        self.c_.setObjectName("c_")

        self.label_4 = QtWidgets.QLabel(Inverse)
        self.label_4.setGeometry(QtCore.QRect(580, 390, 21, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Inverse)
        self.label_5.setGeometry(QtCore.QRect(670, 390, 21, 16))
        self.label_5.setObjectName("label_5")

        self.n_ = QtWidgets.QLineEdit(Inverse)
        self.n_.setGeometry(QtCore.QRect(690, 390, 51, 22))
        self.n_.setObjectName("n_")

        self.Motionblur = QtWidgets.QPushButton(Inverse)
        self.Motionblur.setGeometry(QtCore.QRect(670, 100, 93, 28))
        self.Motionblur.setObjectName("Motionblur")
        self.Motionblur.clicked.connect(self.motionblur)

        self.Noise = QtWidgets.QPushButton(Inverse)
        self.Noise.setGeometry(QtCore.QRect(670, 170, 93, 28))
        self.Noise.setObjectName("Noise")
        self.Noise.clicked.connect(self.addnoise)

        self.Wiener = QtWidgets.QPushButton(Inverse)
        self.Wiener.setGeometry(QtCore.QRect(670, 250, 93, 28))
        self.Wiener.setObjectName("Wiener")
        self.Wiener.clicked.connect(self.wienerfilter)

        self.Inversefilter = QtWidgets.QPushButton(Inverse)
        self.Inversefilter.setGeometry(QtCore.QRect(670, 320, 93, 28))
        self.Inversefilter.setObjectName("Inverse")
        self.Inversefilter.clicked.connect(self.inversefilter)

        self.Kratio = QtWidgets.QLabel(Inverse)
        self.Kratio.setGeometry(QtCore.QRect(770, 390, 21, 21))
        self.Kratio.setObjectName("label_9")

        self.K = QtWidgets.QLineEdit(Inverse)
        self.K.setGeometry(QtCore.QRect(800, 390, 61, 22))
        self.K.setObjectName("K_ratio")

        self.IDHF.raise_()
        self.image.raise_()
        self.selectfile.raise_()
        self.FFT.raise_()
        self.IDLF.raise_()
        self.BLF.raise_()
        self.BHF.raise_()
        self.GLF.raise_()
        self.GHF.raise_()
        self.Homorphic.raise_()
        self.label.raise_()
        self.cuttoff.raise_()
        self.label_2.raise_()
        self.gammaH.raise_()
        self.label_3.raise_()
        self.gammaL.raise_()
        self.c_.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.n_.raise_()
        self.Motionblur.raise_()
        self.Noise.raise_()
        self.Wiener.raise_()
        self.Inversefilter.raise_()
        self.Kratio.raise_()
        self.K.raise_()

        self.retranslateUi(Inverse)
        QtCore.QMetaObject.connectSlotsByName(Inverse)

    def retranslateUi(self, Inverse):
        _translate = QtCore.QCoreApplication.translate
        Inverse.setWindowTitle(_translate("Inverse", "Form"))
        self.image.setText(_translate("Inverse", "TextLabel"))
        self.selectfile.setText(_translate("Inverse", "Select File"))
        self.FFT.setText(_translate("Inverse", "FFT"))
        self.IDLF.setText(_translate("Inverse", "IDLF"))
        self.IDHF.setText(_translate("Inverse", "IDHF"))
        self.BLF.setText(_translate("Inverse", "BLF"))
        self.BHF.setText(_translate("Inverse", "BHF"))
        self.GLF.setText(_translate("Inverse", "GLF"))
        self.GHF.setText(_translate("Inverse", "GHF"))
        self.Homorphic.setText(_translate("Inverse", "Homorphic"))
        self.label.setText(_translate("Inverse", "D0"))
        self.label_2.setText(_translate("Inverse", "rH"))
        self.label_3.setText(_translate("Inverse", "rL"))
        self.label_4.setText(_translate("Inverse", "c"))
        self.label_5.setText(_translate("Inverse", "n"))
        self.Motionblur.setText(_translate("Inverse", "Motion Blur"))
        self.Noise.setText(_translate("Inverse", "Noise"))
        self.Wiener.setText(_translate("Inverse", "Wiener"))
        self.Inversefilter.setText(_translate("Inverse", "Inverse"))
        self.Kratio.setText(_translate("Inverse", "K"))
    def loadimage(self):
        try:
            self.image_path, ret= QtWidgets.QFileDialog.getOpenFileName()
            self.im = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE) # 灰階

            self.image.setPixmap(QtGui.QPixmap(self.image_path))
            self.image.setScaledContents(True)
            # print(image_path) 
        except:
            Error_Text = 'Failed to open image'
            QtWidgets.QMessageBox.information(None, 'Read Me', Error_Text)
    def FT(self):
        timeStart = time.time()
        f = np.fft.fft2((self.im)) # fourier transform
        self.f_shift = np.fft.fftshift(f)# shift origin point
        # show specturm photo
        Fmin=np.log(1+np.min(np.abs(self.f_shift)))
        Fmax=np.log(1+np.max(np.abs(self.f_shift)))
        Y=255*(np.log(1+np.abs(self.f_shift))-Fmin)/(Fmax-Fmin)

        #f_normalize=cv2.normalize(self.mag,None,0,1,cv2.NORM_MINMAX)
        Y=cv2.normalize(Y,None,0,1,cv2.NORM_MINMAX)

        
        phase_angle = np.angle(f) # show phase angle fig

        f_ishift=np.fft.ifftshift(f)
        inverse=np.fft.ifft2(f_ishift)
        inverse=np.abs(inverse)
        timeEnd = time.time()
        timeSpend = timeEnd - timeStart
        print(self.image_path+":"+str(timeSpend))
        inverse = cv2.normalize(inverse,None,0,1,cv2.NORM_MINMAX)
        image_contrast = np.abs(inverse-self.im)

        
        cv2.imshow("spectrum2",Y)
        cv2.imshow("phase",phase_angle)

        cv2.imshow("Inverse image",inverse)
        cv2.imshow("Contrast after inverse fourier transform",image_contrast)
        return
    def IdealLowpass(self):
        cv2.destroyAllWindows()
        self.Type="IDLP"
        self.processImage()
        return
    def IdealHighpass(self):
        cv2.destroyAllWindows()
        self.Type="IDHP"
        self.processImage()
        return
    def butterworthLow(self):
        cv2.destroyAllWindows()
        self.Type="BLF"
        self.processImage()
        return
    def butterworthHigh(self):
        cv2.destroyAllWindows()
        self.Type="BHF"
        self.processImage()
        return
    def gaussianLow(self):
        cv2.destroyAllWindows()
        self.Type="GLF"
        self.processImage()
        return
    def gaussianHigh(self):
        cv2.destroyAllWindows()
        self.Type="GHF"
        self.processImage()
        return
    def homorphic(self):
        cv2.destroyAllWindows()
        self.Type="Homorphic"
        self.processImage()
        return
    def processImage(self): 
        D0 = float(self.cuttoff.text())
        image = np.fft.fft2((self.im))
        image = np.fft.fftshift(image)
        h,w =image.shape
        cx = int(w/2)
        cy = int(h/2)
        for i in range(h):
            for j in range(w):
                distance = math.sqrt((i-cx)**2+(j-cy)**2)
                if(self.Type=="IDLP"):
                    if(distance>D0):
                        image[i][j]=0
                elif(self.Type=="IDHP"):
                    if(distance<D0):
                        image[i][j]=0
                elif(self.Type=="BLF"):
                    n = int(self.n_.text())
                    image[i][j] *=1/((1+(distance/D0))**(2*n))
                elif(self.Type=="BHF"):
                    n = int(self.n_.text())
                    image[i][j] *=(1-1/((1+(distance/D0))**(2*n)))
                elif(self.Type=="GLF"):
                    image[i][j]*=np.exp(-(distance)**2/(2*D0**2))
                elif(self.Type=="GHF"):
                    image[i][j]*=(1-np.exp(-(distance)**2/(2*D0**2)))
                elif(self.Type=="Homorphic"):
                    try:
                        rH=float(self.gammaH.text())
                        rL=float(self.gammaL.text())
                        c=float(self.c_.text())
                        image[i][j]*=((rH-rL)*(1-np.exp(-c*(distance**2)/D0**2))+rL)
                    except:
                        Error_Text = "parameters haven't been input"
                        QtWidgets.QMessageBox.information(None, 'Read Me', Error_Text)
        #f_ishift=np.fft.ifftshift(image)
        image=np.fft.ifft2(image)
        image=np.abs(image)
        image = cv2.normalize(image,None,0,1,cv2.NORM_MINMAX)
        cv2.imshow(self.Type,image)
    def addnoise(self):
        cv2.destroyAllWindows()
        image = np.fft.fft2((self.im))
        image = np.fft.fftshift(image)
        M,N=image.shape
        T=1
        a=b=0.1
        H = np.zeros((M + 1, N + 1), dtype = np.complex128)
        for u in range(1, M + 1):
            for v in range(1, N + 1):
                w = np.pi * (u * a + v * b)
                H[u, v] = (T / w) * np.sin(w) * np.exp(-1j * w) # formular 5-77
        H = H[1 : , 1 : ] 
        G_noise = H*image
        G_noise=np.fft.ifftshift(G_noise)
        blur_noise=np.fft.ifft2(G_noise)
        blur_noise=np.abs(blur_noise)
        mean = 0
        variance = 20 # 題目設定
        noise = np.random.normal(mean, variance, self.im.size)
        noise = noise.reshape(self.im.shape[0], self.im.shape[1]).astype('uint8')
        blur_noise*=noise
        blur_normalize = cv2.normalize(blur_noise,None,0,1,cv2.NORM_MINMAX)
        cv2.imshow("Motion Blur",blur_normalize)

        image = np.fft.fft2(blur_noise)
        blur_noise_wiener = np.fft.fftshift(image)
        k= float(self.K.text())
        F_wiener=(1 / H) * (np.abs(H)**2 / (np.abs(H)**2 + k)) * blur_noise_wiener
        wiener_image=np.fft.ifft2(F_wiener)
        wiener_image=np.abs(wiener_image)
        contrast_wiener= np.abs(self.im-wiener_image)
        self.wiener_image = cv2.normalize(wiener_image,None,0,1,cv2.NORM_MINMAX)
        self.weiner_contrast = cv2.normalize(contrast_wiener,None,0,1,cv2.NORM_MINMAX)

        image = np.fft.fft2(blur_noise)
        blur_noise_inverse = np.fft.fftshift(image)
        F_inverse = blur_noise_inverse/H
        F_inverse = np.fft.ifftshift(F_inverse)
        inverse_image=np.fft.ifft2(F_inverse)
        inverse_image=np.abs(inverse_image)
        contrast_inverse = np.abs(self.im-inverse_image)
        self.inverse_image = cv2.normalize(inverse_image,None,0,1,cv2.NORM_MINMAX)
        self.inverse_contrast = cv2.normalize(contrast_inverse,None,0,1,cv2.NORM_MINMAX)
        
    def motionblur(self):
        cv2.destroyAllWindows()
        image = np.fft.fft2(self.im)
        image = np.fft.fftshift(image)
        M,N=image.shape
        T=1
        a=b=0.1
        H = np.zeros((M + 1, N + 1), dtype = np.complex128)
        for u in range(1, M + 1):
            for v in range(1, N + 1):
                w = np.pi * (u * a + v * b)
                H[u, v] = (T / w) * np.sin(w) * np.exp(-1j * w) # formular 5-77
        H = H[1 : , 1 : ] 
        G = H*image
        blur=np.fft.ifft2(G)
        g=np.abs(blur)
        blur_normalize = cv2.normalize(g,None,0,1,cv2.NORM_MINMAX)
        cv2.imshow("Motion Blur",blur_normalize)

        #Wiener
        image = np.fft.fft2(blur)
        blur = np.fft.fftshift(image)
        k= float(self.K.text())
        F_wiener=(1 / H) * (np.abs(H)**2 / (np.abs(H)**2 + k)) * G
        wiener_image=np.fft.ifft2(F_wiener)
        wiener_image=np.abs(wiener_image)
        contrast_wiener = np.abs(self.im-wiener_image)
        self.wiener_image = cv2.normalize(wiener_image,None,0,1,cv2.NORM_MINMAX)
        self.weiner_contrast = cv2.normalize(contrast_wiener,None,0,1,cv2.NORM_MINMAX)
        #Inverse
        blur = np.copy(G)
        F_inverse = blur/H
        F_inverse = np.fft.ifftshift(F_inverse)
        inverse_image=np.fft.ifft2(F_inverse)
        inverse_image=np.abs(inverse_image)
        contrast_inverse = np.abs(self.im-inverse_image)
        self.inverse_image = cv2.normalize(inverse_image,None,0,1,cv2.NORM_MINMAX)
        self.inverse_contrast = cv2.normalize(contrast_inverse,None,0,1,cv2.NORM_MINMAX)
    def wienerfilter(self):
        
        cv2.imshow("Wiener Image",self.wiener_image)
        cv2.imshow("contrast",self.weiner_contrast)
    def inversefilter(self):
        
        cv2.imshow("Inverse Image",self.inverse_image)
        cv2.imshow("contrast",self.inverse_contrast)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Inverse = QtWidgets.QWidget()
    ui = Ui_Inverse()
    ui.setupUi(Inverse)
    Inverse.show()
   
    sys.exit(app.exec_())