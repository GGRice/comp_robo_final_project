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


    #take x and y changes, add to x and y coords of point
    def translate(self, move, xchange, ychange):

        move[0] += xchange
        move[1] += ychange

        return move

    #take an angle, rotate the point that angle
    def rot(self, move, angle=0 ):
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
    def apply_trans_to_points(self, transform):
        transformed = []
        xchange, ychange = self.avgdist()
        for i in range(0,len(self.points)-1):
            #fix_point = self.points[i][0]
            move_point = self.points[i][1]

            if transform == 'rotate':
                changed = self.rot(move_point, np.pi/2)
            elif transform == 'translate':
                changed = self.translate(move_point, xchange, ychange)
            #print(rotated[0])
            x = int(changed[0])
            y = int(changed[1])
            transformed.append((x,y))
        return transformed

    #finds avg distance between x points and y points
    def avgdist(self):
        xdiff = np.array(0, dtype=np.int64)
        ydiff = np.array(0, dtype=np.int64)
        for i in self.points:
            np.append(xdiff,i[0][0]-i[1][0])
            np.append(ydiff,i[0][1]-i[1][1])
            #xdiff.append(i[0][0]-i[1][0])
            #ydiff.append(i[0][1]-i[1][1])

        x_mean = np.mean(xdiff)
        y_mean = np.mean(ydiff)

        return x_mean, y_mean

    #applies given transform to given set of points
    def run(self, transform):
        transf = self.apply_trans_to_points(transform)

        return transf

    def transform(self, errors):
        transf = self.apply_trans_to_points('translate')

        

        err = np.mean(errors)

        """
        translate
        rotate a random angle <=90
        check error
        if error larger than last error, rotate laser_callback
        once find "min," rotate again to check getting stuck at min
        keep tab of cumulative rotation so can save the different points to go back to

        """




if __name__ == "__main__":

    matching_points = PointMatching()
    matches, errors = matching_points.run()

    type = 'rotate' #rotate or translate


    tran = Transformation(matches)

    transf = tran.run(type)

    viz = Visualize(transf)

    viz.build_img()
    viz.show_img('attempt')
