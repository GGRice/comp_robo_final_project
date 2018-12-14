#!/usr/bin/env python

# Starter code for rotation taken from http://connor-johnson.com/2014/06/06/an-iterative-closest-point-algorithm/

import numpy as np
import scipy.stats
import random
import rospy
import cv2
from cornerfinder import matchPoints
from point_matching import PointMatching
from visualize import Visualize

class Transformation(object):
    def __init__(self, points):
        self.points = points
        self.err_thresh = 200


    ''' Take x and y changes, add to x and y coords of point '''
    def translate(self, move, xchange, ychange):

        move[0] += xchange
        move[1] += ychange

        return move

    ''' Take an angle, rotate the point that angle '''
    def rot(self, move, angle=0 ):
        # perform a random rotation
        theta = angle

        c = np.cos( theta )
        s = np.sin( theta )
        rotation = np.matrix( [[c,-s],[s,c]] ) #creates the roatation matrix

        moved = move * rotation.T #Y is almost always 'x' so multiply Y by the transpose of the transformation (translation,rotation,scaling) matrix

        x = moved[0,0]
        y = moved[0,1]
        r = [x,y] #ccreates a single array to hold the poiint

        return r


    ''' applies transformation trans to points '''
    def apply_trans_to_points(self, transform, angle = 0, points = self.points):
        transformed = []

        #find the average distance between x and y
        xchange, ychange = self.avgdist()

        if points ==self.points: #if not given an array of points, look at the points matrix of point pairs
            for i in range(0,len(self.points)-1):
                move_point = self.points[i][1] #find the point to be moved

                #determine if rotate or translate requested
                if transform == 'rotate':
                    changed = self.rot(move_point, angle)
                elif transform == 'translate':
                    changed = self.translate(move_point, xchange, ychange)
                x = int(changed[0])
                y = int(changed[1])
                transformed.append((x,y))
        else: #if given array of points
            for i in range(0,len(points)-1):
                move_point = points[i]

                if transform == 'rotate':
                    changed = self.rot(move_point, angle)
                elif transform == 'translate':
                    changed = self.translate(move_point, xchange, ychange)
                x = int(changed[0])
                y = int(changed[1])
                transformed.append((x,y))
        return transformed


    ''' Finds avg distance between x points and y points '''
    def avgdist(self):
        #create empty numpy matrices to hold hte values
        xdiff = np.array(0, dtype=np.int64)
        ydiff = np.array(0, dtype=np.int64)

        #add the differences from every pari of points ot the respective matrix
        for i in self.points:
            np.append(xdiff,i[0][0]-i[1][0])
            np.append(ydiff,i[0][1]-i[1][1])

        #find the avg value f the differences and return
        x_mean = np.mean(xdiff)
        y_mean = np.mean(ydiff)

        return x_mean, y_mean


    ''' Applies given transform to given set of points '''
    def run(self, transform):
        transf = self.apply_trans_to_points(transform)

        return transf

    ''' UNTESTED: Perform ICP '''
    #if avg error is higher than threshold
    #translate then rotate random able between 0 and 90
    #find new points in transoformed matrix
    #recursive until error is less than threshold
    def transform(self, errors, viz, pm):
        err = np.mean(errors)

        if err > self.err_thresh:
            transf = self.apply_trans_to_points('translate')
            rot = self.apply_trans_to_points('rotate', random.uniform(0,np.pi/2), transf)

            for i in range(0,len(self.points)-1):
                fix_points.append(self.points[i][0])

            fixed = viz.build_img(fix_points)
            moving = viz.build_img(rot)

            pm.arrangePoints(fixedm = fixed, movingm = moving, 'moving', len(fixed))
            pm.limitPoints()
            pm.matchingPoints()

            transform(pm.errors, viz, pm)
        else:
            return moving




if __name__ == "__main__":

    matching_points = PointMatching()
    matches, errors = matching_points.run()

    type = 'rotate' #rotate or translate


    tran = Transformation(matches)

    transf = tran.run(type)

    viz = Visualize(transf)

    viz.build_img()
    viz.show_img('attempt')
