#!/usr/bin/env python


# Taken from http://connor-johnson.com/2014/06/06/an-iterative-closest-point-algorithm/
# comments are my own


import numpy as np
import scipy.stats
from pylab import *
from PIL import Image
import matplotlib.pyplot as plt
import random
import rospy
import cv2

def image(img):
    #adress = '../'
    return cv2.imread(img, 0)

#np.matrix.T returns the transpose of the matrix

def T( x, T0, T1, k=1.0 ):
    # apply an affine transformation to `x`

    #print(T1)

    y = x * T0.T #Y is almost always 'x' so multiply Y by the transpose of the transformation (translation,rotation,scaling) matrix
    y[:,0] += T1[0,0]
    y[:,1] += T1[1,0]
    return y*k

def translate( points ):
    xchange, ychange = com(points)

    for i in points:
        i[1][0] = i[1][0] + xchange
        i[1][1] = i[1][1] + ychange

    print(points)
    return points


def rot( X, Y, angle=0 ):
    # perform a random rotation
    theta = angle

    c = np.cos( theta )
    s = np.sin( theta )
    rotation = np.matrix( [[c,-s],[s,c]] ) #creates the roatation matrix

    Z = np.matrix( np.zeros((2,1)) ) #creates a matrix full of 0s

    Yp = T( Y, rotation, Z ) # uses the rotation matrix and the zero matrix to apply the transformation
    return Yp

#From cornerfinder
def findPoints(filename):
    #TODO: fix long distance noise being picked
    #img = cv2.imread(filename)
    img = filename
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = np.float32(img)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)
    return img,dst


def arrangePoints(matrix):
    #finding nonzeros
    array_points = []
    matrix[matrix<=0.01*matrix.max()]=0
    x,y = np.where(matrix > 0.01*matrix.max())
    for i in range(0,len(x)):
        array_points.append((x[i],y[i]))
    return array_points, matrix


def apply_trans_to_points(trans, fixed_array1, fixed_array2):
    transformed = []
    for i in range(0,len(fixed_array2)-1):
        point1 = fixed_array1[i]
        point2 = fixed_array2[i]

        if trans == 'rotate':
            changed = rot(point1, point2, np.pi/2)
        elif trans == 'translate':
            changed = translate(point1, point2)
        #print(rotated[0])
        x = int(changed[0,0])
        y = int(changed[0, 1])
        transformed.append((x,y))
    return transformed

def show_img(name, img):
    cv2.imshow(name, img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

def com(points):
    xdiff = []
    ydiff = []
    for i in points:
        xdiff.append(i[0][0]-i[1][0])
        ydiff.append(i[0][1]-i[1][1])

    x_mean = np.mean(xdiff)
    y_mean = np.mean(ydiff)

    return x_mean, y_mean

def build_img(transf):
    changed_img = np.ones((len(fixedzeros2), len(fixedzeros2[0])), np.uint8)
    changed_img[:] = 255

    for index in transf:
        changed_img[index[0], index[1]] = 0

    return changed_img






#show full array in printout
#np.set_printoptions(threshold=np.nan)

m1 = image('maze1.jpg')
m2 = image('maze1_2.pgm')


crop_img1 = m1[920:1120, 920:1120]
crop_img2 = m2[920:1120, 920:1120]

imgfixed1,fixed1 = findPoints(crop_img1)
fixed_array1, fixedzeros1 = arrangePoints(fixed1)

imgfixed2,fixed2 = findPoints(crop_img2)
fixed_array2, fixedzeros2 = arrangePoints(fixed2)


type = 'rotate' #rotate or translate
transf = apply_trans_to_points(type,fixed_array1, fixed_array2)

changed_img = build_img(transf)
#print(changed_img)





show_img(type, changed_img)

# [[(x1,y1),(x2,y2)],[(x3,y3),(x4,y4)]]

#find center of mazz of points, shift all points that amount

'''
X=[]
Y=[]
for i in points:
    X.apend(i[0])
    Y.append(i[1])
'''
