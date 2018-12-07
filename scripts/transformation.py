#!/usr/bin/env python


# Taken from http://connor-johnson.com/2014/06/06/an-iterative-closest-point-algorithm/
# comments are my own


import numpy as np
import scipy.stats
from pylab import *
import random
import rospy
import cv2

def image(img):
    adress = '../'
    return cv2.imread(img, 0)

#np.matrix.T returns the transpose of the matrix

def T( x, T0, T1, k=1.0 ):
    # apply an affine transformation to `x`
    y = x * T0.T #Y is almost always 'x' so multiply Y by the trnaspose of the transformation (translation,rotation,scaling) matrix
    #print(y[:,0])
    #print(y.size)
    #print(T1)
    #print(y[:,0].size)
    #y[:,0] += -1
    #print(y[:,0])
    y[:,0] += T1[0]
    y[:,1] += T1[1]
    return y*k

def translate( X, Y ):
    # translate to align the centers of mass

    #finds the center of mass of the maps
    #returns an array with the same mean values in it
    mx = np.mean( X, axis=0 ).T
    my = np.mean( Y, axis=0 ).T

    #finds the difference between the com
    translation = mx - my

    #finds length of the image matrix
    t = int(np.sqrt(Y.size))

    #creates a translation matrix with length of image
    I = np.matrix( np.eye( t ) )
    #uses translation matrix and com diff to apply the transformation
    Yp = T( Y, I, translation )
    return Yp
    
    #return errorfct( X, Yp ), translation #returns the error between the first and translated second map and returns the com difference

def rot( X, Y, angle=-1 ):
    # perform a random rotation
    if angle == -1:
        theta = scipy.stats.uniform( 0.0, 2.0*np.pi ).rvs() #generates a random angle
    else:
        theta = angle

    c = np.cos( theta )
    s = np.sin( theta )
    rotation = np.matrix( [[c,-s],[s,c]] ) #creates the roatation matrix
    Z = np.matrix( np.zeros((2,1)) ) #creates a matrix full of 0s
    Yp = T( Y, rotation, Z ) # uses the rotation matrix and the zero matrix to apply the transformation
    return Yp
    #return errorfct( X, Yp ), rotation #returns the error between the first and rotated second map as well as the roation matrix

def scale( X, Y, scale = 0 ):
    # perform a random scaling
    if scale == 0:
        k = scipy.stats.uniform( 0.5, 1.0 ).rvs() #generates random scaling value
    else:
        k = scale

    scaling = k * np.matrix( np.eye(2) ) #created scaling matrix full of zeros and k on the diagonal
    Z = np.matrix( np.zeros((2,1)) ) #creates zero matrix
    Yp = T( Y, scaling, Z ) #uses the scaling matrix and zero matrix to apply the transformation
    return Yp
    #return errorfct( X, Yp ), scaling #returns the error between the first and scaled second matrix and returns the scaling matrix


m1 = image('maze1.jpg')
m2 = image('maze1_2.pgm')

print(m1.size)
print(m2.size)

crop_img1 = m1[920:1120, 920:1120]
crop_img2 = m2[920:1120, 920:1120]
#print(crop_img1)
print(crop_img2.shape)
'''
cv2.imshow('maze 2', crop_img2)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
'''

trans = translate(crop_img1, crop_img2)
cv2.imshow('translated', trans)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
