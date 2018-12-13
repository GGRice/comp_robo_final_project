#!/usr/bin/env python

import rospy
import cv2
import numpy as np
import random


def findPoints(filename):
    #TODO: fix long distance noise being picked
    img = cv2.imread(filename)
    img = img[920:1120, 920:1120]
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
    matrix[matrix<=0.01*matrix.max()]=0
    x,y = np.where(matrix > 0.01*matrix.max())
    for i in range(0,len(x)):
        array_points.append([x[i],y[i]])
    return array_points, matrix


def matchPoints(fixed,moving,fixed_array,moving_array,a=0):#, moving):
    #TODO: run for 100 cycles

    #same amount of points for array and matrix
    numpoints = min((np.count_nonzero(fixed)),(np.count_nonzero(moving)))
    if len(fixed_array)!=len(moving_array):
        if len(fixed_array)>len(moving_array):
            random.shuffle(fixed_array)
            fixed_array_bad = fixed_array[numpoints:]
            fixed_array=fixed_array[:numpoints]
            for i in range(0,len(fixed_array_bad)):
                fixed[fixed_array_bad[i]] = 0
        if len(fixed_array)<len(moving_array):
            random.shuffle(moving_array)
            moving_array_bad = moving_array[numpoints:]
            moving_array=moving_array[:numpoints]
            for i in range(0,len(moving_array_bad)):
                moving[moving_array_bad[i]] = 0

    #searching non-zero points
    idx=np.zeros(numpoints)
    matches = np.zeros(numpoints, dtype='(2,2)int8')
    for i in range(0,numpoints):
        #iterates through moving_array (new map)
        X= []
        for n in range(0,numpoints):
            #iterates through fixed_array (established map)
            #TODO: remove from matching list
            val = np.subtract(np.square(moving_array[i]),np.square(fixed_array[n]))    #gets hypotenuse
            X.append(np.square(val[0]+val[1]))                                             #square of error distance appended to X
        idx[i] = int((np.where(X == min(X))[0][0])) #found closest interesting point
        matches[i] = [moving_array[i],fixed_array[int(idx[i])]]
    print(matches.min())
    print(matches.max())
    return matches





imgfixed,fixed = findPoints('maze1.pgm')
#showPoints(imgfixed,fixed)
fixed_array, fixedzeros = arrangePoints(fixed)
imgmoving,moving = findPoints('maze1_2.pgm')
moving_array, fixedzeros = arrangePoints(moving)

a = matchPoints(fixed, moving,fixed_array,moving_array)
print(a)
