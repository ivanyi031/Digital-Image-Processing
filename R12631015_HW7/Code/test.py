import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import skimage
from skimage.measure import regionprops

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        image=cv2.imread(file_path)
def Lab(image):
    def hq_func(q):
        if (q > 0.008856):
            output = pow(q, 1/3)
        else:
            output = 7.787*q + 16/116
        return output
    def L_func(Y):
        if Y>0.008856:
            return 116*Y**(1/3)-16
        else:
            return 903.3*Y
    rows,cols=image.shape[:2]
    B=image[:,:,0]
    G=image[:,:,1]
    R=image[:,:,2]
    L=np.zeros((rows,cols))
    A=np.zeros((rows,cols))
    B=np.zeros((rows,cols))
    X = (0.412453*R + 0.357580*G + 0.180423*B)
    Y = (0.212671*R + 0.715160*G + 0.072169*B)
    Z = (0.019334*R + 0.119193*G + 0.950227*B)
    for i in range(rows):
        for j in range(cols):
            L[i,j]  = L_func(Y[i,j])
            A[i,j]  = 500*(hq_func(X[i,j]/0.950456)-hq_func(Y[i,j]))
            B[i,j] = 200*(hq_func(Y[i,j])-hq_func(Z[i,j]/1.088754))
    L=(L*255/100)
    A=(np.array(A)+128)
    B=(np.array(B)+128)
    return L,A,B
def Slic(img,image2):
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
        rx=int(rows/s)
        ry=int(cols/s)
        for i in range(rx):
            x_coordinate.append(xs+i*s)
        for j in range(ry):
            y_coordinate.append(ys+j*s)
        for k in range(len(x_coordinate)):
            for m in range(len(y_coordinate)):
                center.append([x_coordinate[k],y_coordinate[m]])
        return center
    image=np.copy(img)
    border = np.copy(image2)
    rows,cols=image.shape
    supixel = np.zeros(image.shape)
    sp = 2000
    s = int(np.sqrt(rows*cols/sp))
    dcm = 20
    center=[]
    previous_mean = []
    center=getcoordinate(center,rows,cols,s)
    center=adjust_center(center,image)
    for i in range(len(center)):
        x = center[i][0]
        y = center[i][1]
        previous_mean.append([image[x,y],x,y])#[Intensity,x,y]
    for t in range(2):
        x_sum=np.zeros(len(center))
        y_sum=np.zeros(len(center))
        I_sum = np.zeros(len(center))
        count = np.zeros(len(center),dtype=np.int16)
        label= -np.ones((rows,cols),dtype=np.int16)
        distance = 10**100*np.ones((rows,cols))
        for c in range (len(center)):
            I_c=previous_mean[c][0]
            x_c=previous_mean[c][1]
            y_c=previous_mean[c][2]
            for x in range(int(x_c-s),int(x_c+s)):
                for y in range(int(y_c-s),int(y_c+s)):
                    if(x<0 or x>=rows or y<0 or y>=cols):
                        pass
                    else:
                        euclidean = np.sqrt((x-x_c)**2+(y-y_c)**2)
                        intensity = np.sqrt((int(image[x][y])-I_c)**2)
                        D = np.sqrt((euclidean/s)**2+(intensity/dcm)**2)
                        if (distance[x][y]>D):
                            if(label[x][y] > -1): #delete past information
                                plabel=label[x][y]
                                x_sum[plabel]-=x
                                y_sum[plabel]-=y
                                I_sum[plabel]-=image[x][y]
                                count[plabel]-=1
                            x_sum[c]+=x
                            y_sum[c]+=y
                            I_sum[c]+=image[x][y]
                            count[c]+=1
                            distance[x][y]=D
                            label[x][y]=c
        print(t)
        for i in range(len(center)):
            Im=int(I_sum[i]/count[i])
            xm=int(x_sum[i]/count[i])
            ym=int(y_sum[i]/count[i])
            previous_mean[i] = [Im,xm,ym]
    for i in range(rows):
        for j in range(cols):
            supixel[i][j]=previous_mean[label[i,j]][0]
            if(i == 0 or i==rows-1 or j==0 or j==cols-1):
                pass
            else:
                if(label[i][j]!=label[i+1][j] or label[i][j]!=label[i][j+1]):
                    border[i,j,:]=255                    
                    supixel=cv2.normalize(supixel,None,0,1,cv2.NORM_MINMAX)
    cv2.namedWindow("superpixel",cv2.WINDOW_NORMAL)
    cv2.namedWindow("border",cv2.WINDOW_NORMAL)
    cv2.imshow("superpixel",supixel)
    cv2.imshow("border",border)
    cv2.waitKey(0)
    return previous_mean,label,border
def find_thres(hist):
    fi =0
    start=0
    while(True):
        if hist[fi]==0:
            fi+=1
        else:
            start=hist[fi]
            break
    max=np.max(hist)
    maxloc=np.where(hist==max)[0][0]
    m=(max-start)/(maxloc-fi)
    b=-m*fi+start
    distance=0
    thresloc=0
    for i in range(fi,maxloc):
        t=m/(m**2+1)*(hist[i]-m*i-b)
        d=np.sqrt(t**2+(t/m)**2)
        if d>distance:
            distance=d
            thresloc=i
    return thresloc
def find_seed(dist)  :
    rows,cols =dist.shape
    seed=[]
    area = np.zeros((rows,cols),dtype='uint8')
    seed_map = np.zeros((rows,cols),dtype='uint8')
    for i in range(rows):
        for j in range (cols):
            if dist[i,j]!=0:
                area[i,j]=1
    kernel = np.ones((5,5),np.uint8)
    area=cv2.morphologyEx(area,cv2.MORPH_OPEN,kernel)
    contours, hierarchy = cv2.findContours(area, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnts in contours:
        mask2 = np.zeros((rows,cols),np.uint8)
        cv2.drawContours(mask2,[cnts],0,255,thickness=-1)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(dist,mask = mask2)
        x=max_loc[0]
        y=max_loc[1]
        seed.append(max_loc)
    print(len(contours))
    for s in seed:
        label_num=label[s[1],s[0]]
        seed_map[label==label_num]=255
    cv2.imshow("seed map",seed_map)  
    return seed_map

if __name__ == "__main__":
    window=tk.Tk()
    file_path=filedialog.askopenfilename()
    image=cv2.imread(file_path)
    rows,cols=image.shape[:2]
    imagelab = cv2.cvtColor(image,cv2.COLOR_BGR2Lab)
    window.destroy()
    A=imagelab[:,:,1]
    #centerinfo,label,border=Slic(A,image)
    label = skimage.segmentation.slic(A,n_segments=3000, compactness=0.1,channel_axis=None)

    print("finish")
    binary = np.zeros((rows,cols))
    hist_A=np.zeros(256)
    for i in range(rows):
        for j in range(cols):
            hist_A[A[i,j]]+=1
    thres=find_thres(hist_A)
    for i in range(rows):
        for j in range(cols):
            if A[i][j]<thres:
                binary[i][j]=255
                #image[i,j,:]=255
            else:
                binary[i][j]=0
    binary=binary.astype('uint8')
    kernel = np.ones((5,5),np.uint8)
    binary = cv2.morphologyEx(binary,cv2.MORPH_OPEN,kernel)
    plt.hist(A.ravel(),256,[0,200])
    #distance map
    dist=cv2.distanceTransform(binary, cv2.DIST_L2,3)
    cv2.normalize(dist,dist, 0,1.0,cv2.NORM_MINMAX)
    cv2.namedWindow("distance map",cv2.WINDOW_NORMAL)
    cv2.imshow("distance map",dist)
    dist[dist<0.45]=0
    regions = regionprops(label)
    kerneld = np.ones((13,13),np.uint8)
    seed_loc=find_seed(dist)
    seed_map = find_seed(dist)

    # Marker labelling
    ret, markers = cv2.connectedComponents(seed_map)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1
    # Now, mark the region of unknown with zero
    unknown=cv2.subtract(binary,seed_map)
    markers[unknown==255] = 0
    img=np.zeros((rows,cols,3),dtype='uint8')
    for i in range(3):
        img[:,:,i]=A
    markers = cv2.watershed(img, markers)
    fig, ax = plt.subplots(figsize=(6, 6)) 
    ax.imshow(markers, cmap="tab20b") 
    ax.axis('off') 
    plt.show()
    cv2.namedWindow("SLIC",cv2.WINDOW_NORMAL)
    
    image[seed_map==255,:]=255
    cv2.imshow("SLIC",skimage.segmentation.mark_boundaries(image,label))
    cv2.namedWindow("plant",cv2.WINDOW_NORMAL)
    cv2.namedWindow("plant_lab",cv2.WINDOW_NORMAL)
    cv2.namedWindow("binary",cv2.WINDOW_NORMAL)
    #cv2.namedWindow("binary_accuracy",cv2.WINDOW_NORMAL)
    
    cv2.imshow("plant_lab",A)
    cv2.imshow("binary",binary)
    #cv2.imshow("binary_accuracy",image)
    cv2.imshow("distance map",dist)
    #cv2.imshow("seed",markers)
    fig, ax = plt.subplots(figsize=(5, 5)) 
    ax.imshow(markers, cmap="tab20b") 
    ax.axis('off') 
    labels = np.unique(markers) 
  
    leaves = [] 
    for label in labels[2:]:   
    
    # Create a binary image in which only the area of the label is in the foreground  
    #and the rest of the image is in the background    
        target = np.where(markers == label, 255, 0).astype(np.uint8) 
        
    # Perform contour extraction on the created binary image 
        contours, hierarchy = cv2.findContours( 
            target, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE 
        ) 
        leaves.append(contours[0]) 
    
    # Draw the outline 
    watershed = cv2.drawContours(image, leaves, -1, color=(0, 23, 223), thickness=2) 
    cv2.imshow('watershed',watershed)
    plt.show()
    cv2.waitKey(0)
    