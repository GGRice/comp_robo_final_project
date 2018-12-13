#!/usr/bin/env python


# Starter code for rotation taken from http://connor-johnson.com/2014/06/06/an-iterative-closest-point-algorithm/


import numpy as np
import scipy.stats
import random
import rospy
import cv2
from cornerfinder import matchPoints

class Transformation(object):
    def __init__(self, points, transform):
        self.points = points
        self.transform = transform #'rotate' or 'translate'


    #take x and y changes, add to x and y coords of point
    def translate(move, xchange, ychange):

        move[0] += xchange
        move[1] += ychange

        return Y

    #take an angle, rotate the point that angle
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


    #applies transformation trans to points
    def apply_trans_to_points(trans):
        transformed = []
        xchange, ychange = self.avgdist()
        for i in range(0,len(a)-1):
            #fix_point = self.points[i][0]
            move_point = self.points[i][1]

            if trans == 'rotate':
                changed = rot(move_point, np.pi/2)
            elif trans == 'translate':
                changed = translate(move_point, xchange, ychange)
            #print(rotated[0])
            x = int(changed[0])
            y = int(changed[1])
            transformed.append((x,y))
        return transformed

    #finds avg distance between x points and y points
    def avgdist():
        xdiff = []
        ydiff = []
        for i in self.points:
            xdiff.append(i[0][0]-i[1][0])
            ydiff.append(i[0][1]-i[1][1])

        x_mean = np.mean(xdiff)
        y_mean = np.mean(ydiff)

        return x_mean, y_mean

    #applies given transform to given set of points
    def run():
        type = self.type #rotate or translate
        transf = apply_trans_to_points(self.type, self.points)

        return transf
