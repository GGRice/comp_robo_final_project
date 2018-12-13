#!/usr/bin/env python


# Starter code for rotation taken from http://connor-johnson.com/2014/06/06/an-iterative-closest-point-algorithm/


import numpy as np
import scipy.stats
import random
import rospy
import cv2
from cornerfinder import matchPoints
#import visualize

class Transformation(object):
    def __init__(self, points, transform):
        self.points = points
        self.transform = transform #'rotate' or 'translate'


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
    def apply_trans_to_points(self):
        transformed = []
        xchange, ychange = self.avgdist()
        for i in range(0,len(a)-1):
            #fix_point = self.points[i][0]
            move_point = self.points[i][1]

            if self.transform == 'rotate':
                changed = self.rot(move_point, np.pi/2)
            elif self.transform == 'translate':
                changed = self.translate(move_point, xchange, ychange)
            #print(rotated[0])
            x = int(changed[0])
            y = int(changed[1])
            transformed.append((x,y))
        return transformed

    #finds avg distance between x points and y points
    def avgdist(self):
        xdiff = []
        ydiff = []
        for i in self.points:
            xdiff.append(i[0][0]-i[1][0])
            ydiff.append(i[0][1]-i[1][1])

        x_mean = np.mean(xdiff)
        y_mean = np.mean(ydiff)

        return x_mean, y_mean

    #applies given transform to given set of points
    def run(self):
        transf = self.apply_trans_to_points()

        return transf


class Visualize(object):
    def __init__(self, matrix):
        self.to_be_img = matrix
        self.width = 200
        self.height = 200

        self.changed_img = None


    def build_img(self):
        self.changed_img = np.ones(self.width, self.height, np.uint8)
        self.changed_img[:] = 255

        for index in self.to_be_img:
            self.changed_img[index[0], index[1]] = 0


    def show_img(self, name):
        cv2.imshow(name, self.changed_img)
        if cv2.waitKey(0) & 0xff == 27:
            cv2.destroyAllWindows()




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

def image(img):
    #adress = '../'
    return cv2.imread(img, 0)

if __name__ == "__main__":

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


    tran = Transformation(a, type)

    transf = tran.run()

    viz = Visualize(transf)

    viz.build_img()
    viz.show_img('attempt')
