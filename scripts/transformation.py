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
from cornerfinder import matchPoints

def image(img):
    #adress = '../'
    return cv2.imread(img, 0)

#np.matrix.T returns the transpose of the matrix



def translate(move, xchange, ychange):

    move[0] += xchange
    move[1] += ychange

    return Y


def rot( move, angle=0 ):
    # perform a random rotation
    theta = angle

    c = np.cos( theta )
    s = np.sin( theta )
    rotation = np.matrix( [[c,-s],[s,c]] ) #creates the roatation matrix

    moved = move * rotation.T #Y is almost always 'x' so multiply Y by the transpose of the transformation (translation,rotation,scaling) matrix

    x = moved[0,0]
    y = moved[0,1]
    r = [x,y]

    return r

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


def apply_trans_to_points(trans, a):
    transformed = []
    xchange, ychange = com(points)
    for i in range(0,len(a)-1):
        #fix_point = a[i][0]
        move_point = a[i][1]

        if trans == 'rotate':
            changed = rot(move_point, np.pi/2)
        elif trans == 'translate':
            changed = translate(move_point, xchange, ychange)
        #print(rotated[0])
        x = int(changed[0])
        y = int(changed[1])
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

def build_img(transf, crop_img1):
    changed_img = np.ones((len(crop_img1), len(crop_img1[0])), np.uint8)
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

#show_img('map2',crop_img2)

imgfixed,fixed = findPoints(crop_img1)
fixed_array, fixedzeros = arrangePoints(fixed)

imgmoving,moving = findPoints(crop_img2)
moving_array, fixedzeros = arrangePoints(moving)

a = matchPoints(fixed, moving,fixed_array, moving_array)


type = 'translate' #rotate or translate
transf = apply_trans_to_points(type,a)

changed_img = build_img(transf, crop_img1)
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
