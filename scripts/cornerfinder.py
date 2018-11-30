#!/usr/bin/env python

import rospy
import cv2
import numpy as np


def findPoints(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)
    return dst

def showPoints(dst):#for showing image
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst>0.01*dst.max()]=[0,0,255]
    cv2.imshow('dst',img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

def arrangePoints(matrix):
    #finding nonzeros
    array_points = []
    x,y = np.where(matrix > 0.01*matrix.max())
    for i in range(0,len(x)):
        array_points.append((x[i],y[i]))
    return array_points

def matchPoints(fixed, moving)


fixed = findPoints('room1.jpg')
fixed_array = arrangePoints(fixed)

moving = findPoints('room2.jpg')
moving_array = arrangePoints(moving)
