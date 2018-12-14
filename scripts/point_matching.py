#!/usr/bin/env python

import rospy
import cv2
import numpy as np
import random
import time


class PointMatching(object):

    def __init__(self):
        self.fixedimg = []
        self.fixedmatrix = []
        self.fixedarray = []
        self.fixed = []

        self.movingimg = []
        self.movingmatrix = []
        self.movingarray = []

        self.numpoints = 0
        self.matches = []
#fix shit with passing into functions

    ''' Run corner detection to find important points ''''
    def findPoints(self,filename, t):
        #want to created different variables for fixed or moving array

        #make images black and white
        #run Harris corener detection
        #make the points in the matrix bigger

        if t == 'fixed':
            img = cv2.imread(filename)
            self.fixedimg = img[920:1120, 920:1120]
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            gray = np.float32(gray)
            matrix = cv2.cornerHarris(gray,2,3,0.04)
            self.fixedmatrix = cv2.dilate(matrix,None)
        elif t == 'moving':
            img = cv2.imread(filename)
            self.movingimg = img[920:1120, 920:1120]
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            gray = np.float32(gray)
            matrix = cv2.cornerHarris(gray,2,3,0.04)
            self.movingmatrix = cv2.dilate(matrix,None)

    ''' Visualize corner detection '''
    def showPoints(self,t):
        if t == 'fixed':
            self.fixedimg[self.fixedmatrix>0.01*self.fixedmatrix.max()]=[0,0,255]
            cv2.imshow(self.fixedmatrix,self.fixedimg)
            if cv2.waitKey(0) & 0xff == 27:
                cv2.destroyAllWindows()
        elif t == 'moving':
            self.movingimg[self.movingmatrix>0.01*self.movingmatrix.max()]=[0,0,255]
            cv2.imshow(self.movingmatrix,self.movingimg)
            if cv2.waitKey(0) & 0xff == 27:
                cv2.destroyAllWindows()

    ''' find key points, above threshold, and saving to array '''
    def arrangePoints(self,fixedm = self.fixedmatrix, movingm = self.movingmatrix, t, a):
        # t is the type of matrix, fixed or moving
        # a is WHAT IS A??
        array_points = []
        if t == 'fixed':
            self.fixedmatrix = fixedm
            if a>0:
                self.fixedmatrix[self.fixedmatrix<=0.01*self.fixedmatrix.max()]=0
                x,y = np.where(self.fixedmatrix > 0.01*self.fixedmatrix.max())
            else:
                x,y = np.where(self.fixedmatrix > 0)
            for i in range(0,len(x)):
                self.fixedarray.append((x[i],y[i]))
        elif t == 'moving':
            self.movingmatrix = movingm
            if a>0:
                self.movingmatrix[self.movingmatrix<=0.01*self.movingmatrix.max()]=0
                x,y = np.where(self.movingmatrix > 0.01*self.movingmatrix.max())
            else:
                x,y = np.where(self.movingmatrix > 0)
            for i in range(0,len(x)):
                self.movingarray.append((x[i],y[i]))


    ''' makes sure both matricies of points hold the same number of points '''
    def limitPoints(self):
        #determine how many points should be in each set
        self.numpoints = min(len(self.fixedarray),len(self.movingarray))

        #randomly shuffles points in the array
        #gets rid of some points form the fixed or moving array to equalize the number of points in each

        if len(self.fixedarray)!=len(self.movingarray):
            if len(self.fixedarray)>len(self.movingarray):
                random.shuffle(self.fixedarray)
                fixed_array_bad = self.fixedarray[self.numpoints:]
                self.fixedarray=self.fixedarray[:self.numpoints]
                for i in range(0,len(fixed_array_bad)):
                    self.fixedmatrix[fixed_array_bad[i][0]][fixed_array_bad[i][1]] = 0
            if len(self.fixedarray)<len(self.movingarray):
                random.shuffle(self.movingarray)
                moving_array_bad = self.movingarray[self.numpoints:]
                self.movingarray=self.movingarray[:self.numpoints]
                for i in range(0,len(moving_array_bad)):
                    self.movingmatrix[moving_array_bad[i][0]][moving_array_bad[i][1]] = 0

    ''' Finds the non-zero points in each array and saves them as pairs '''
    def matchPoints(self):
        #finds point from other array with smallest error between
        #saves points as a pair in a matrix of point pairs

        idx=np.zeros(self.numpoints)
        self.matches = np.zeros(self.numpoints, dtype='(2,2)int8')
        self.errors = np.zeros(self.numpoints)
        for i in range(0,self.numpoints):
            #iterates through moving_array (new map)
            X = []
            for n in range(0,self.numpoints):
                #iterates through fixed_array (established map)
                #TODO: remove from matching list
                val = np.subtract(self.movingarray[i],self.fixedarray[n])    #gets hypotenuse
                X.append(np.square(val[0])+np.square(val[1]))                                             #square of error distance appended to X
            idx[i] = int(np.where(X == min(X))[0][0]) #found closest interesting point
            self.errors[i] = X[int(idx[i])]
            self.matches[i] = [self.movingarray[i],self.fixedarray[int(idx[i])]]

    ''' Run with two maps: fixed is the established map, moving is new map '''
    def run(self):
        self.findPoints('maze1.pgm','fixed')
        self.arrangePoints('fixed')
        self.findPoints('maze1_2.pgm','moving')
        cv2.imshow('test', self.movingmatrix)
        if cv2.waitKey(0) & 0xff == 27:
            cv2.destroyAllWindows()
        self.arrangePoints('moving')
        self.limitPoints()
        self.matchPoints()
        return self.matches, self.errors


if __name__ == "__main__":
    P=PointMatching()
    matches, errors = P.run()
    print(errors)
    print(np.mean(errors))
    time.sleep(10)
