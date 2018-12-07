#!/usr/bin/env python

import rospy
import cv2
import numpy as np
import random


def findPoints(filename):
    #TODO: fix long distance noise being picked
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)
    return img,dst

def showPoints(img, dst):#for showing image
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
    matrix[matrix<0.01*matrix.max()]=0
    return array_points, matrix


def matchPoints(fixed,moving,fixed_array,moving_array,a=0):#, moving):
    #TODO: run for 100 cycles
    #make arrays the same length
    numpoints = min((len(fixed)),(len(moving)))
    if len(fixed)!=len(moving):
        if len(fixed)>len(moving):
            random.shuffle(fixed)
            fixed=fixed[:numpoints]
        if len(fixed)<len(moving):
            random.shuffle(moving)
            moving=moving[:numpoints]
    #fixed=sorted(fixed)
    #moving=sorted(moving)

    for i in range(0,numpoints):
        x1,y1 = moving_array[i]
        x2,y2 = fixed_array[i]
        #searchingNeighbors
        X = np.square(fixed-[moving_array[i]])
        idx = np.where( fixed_array.contains(moving_array[i]))
        idx = idx == X.min()
        A[idx[0], idx[1]]


        '''
        if not (fixed_array.includes([x1,y1])):
            if not (fixed_array.includes([x1-1,y1])):
                if not (fixed_array.includes([x1-1,y1-1])):
                    if not (fixed_array.includes([x1,y1-1])):
                        if not (fixed_array.includes([x11,y1])):

        hypo = (x1)**2 + (y)**2
        '''


    '''a+=1
    if a<100:
        matchPoints(fixed, a)
    if a>=100:
        print(a)
        '''



imgfixed,fixed = findPoints('maze1.pgm')
showPoints(imgfixed,fixed)
fixed_array, fixedzeros = arrangePoints(fixed)
#imgmoving,moving = findPoints('room2.jpg')
#moving_array, fixedzeros = arrangePoints(moving)

#matchPoints(fixed, moving,fixed_array,moving_array)
