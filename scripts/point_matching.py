#!/usr/bin/env python

import rospy
import cv2
import numpy as np
import random


class PointMatching(object):

    def __init__(self):
        self.img = []
        self.dst = []
        self.array_points = []
#fix shit with passing into functions

    def findPoints(filename):
        img = cv2.imread(filename)
        self.img = img[920:1120, 920:1120]
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray,2,3,0.04)
        self.dst = cv2.dilate(dst,None)

    def showPoints(self):#for showing image
        # Threshold for an optimal value, it may vary depending on the image.
        self.img[dst>0.01*dst.max()]=[0,0,255]
        cv2.imshow(self.dst,self.img)
        if cv2.waitKey(0) & 0xff == 27:
            cv2.destroyAllWindows()


#fix this
    def arrangePoints(matrix):
        #finding nonzeros
        array_points = []
        matrix[matrix<=0.01*matrix.max()]=0
        x,y = np.where(matrix > 0.01*matrix.max())
        for i in range(0,len(x)):
            self.array_points.append((x[i],y[i]))
