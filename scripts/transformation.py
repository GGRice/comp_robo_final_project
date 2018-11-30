# Taken from http://connor-johnson.com/2014/06/06/an-iterative-closest-point-algorithm/
# comments are my own


import numpy as np
import scipy.stats
from pylab import *
import random

#np.matrix.T returns the transpose of the matrix

def T( x, T0, T1, k=1.0 ):
    # apply an affine transformation to `x`
    y = x * T0.T #Y is almost always 'x' so multiply Y by the trnaspose of the transformation (translation,rotation,scaling) matrix
    y[:,0] += T1[0,0]
    y[:,1] += T1[1,0]
    return y*k

def translate( X, Y ):
    # translate to align the centers of mass
    mx = np.mean( X, axis=0 ).T #finds the center of mass of the first map -> returns an array with the mean values in it
    my = np.mean( Y, axis=0 ).T #finds the center of mass of the second map
    translation = mx - my #finds the difference between the com
    I = np.matrix( np.eye( 2 ) ) #creates a translation matrix
    Yp = T( Y, I, translation ) #uses the translation matrix and difference between com to apply the transformation
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

def sscale( X, Y, scale = 0 ):
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
