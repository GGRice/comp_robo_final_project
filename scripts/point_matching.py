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


    def findPoints(self,filename, t):
        #run corner detection
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


    def showPoints(self,t):
        #visualize corner detection
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


    def arrangePoints(self,t):
        #finding key points and putting them in an array
        array_points = []
        if t == 'fixed':
            self.fixedmatrix[self.fixedmatrix<=0.01*self.fixedmatrix.max()]=0
            x,y = np.where(self.fixedmatrix > 0.01*self.fixedmatrix.max())
            for i in range(0,len(x)):
                self.fixedarray.append((x[i],y[i]))
        elif t == 'moving':
            self.movingmatrix[self.movingmatrix<=0.01*self.movingmatrix.max()]=0
            x,y = np.where(self.movingmatrix > 0.01*self.movingmatrix.max())
            for i in range(0,len(x)):
                self.movingarray.append((x[i],y[i]))


    def limitPoints(self):
        #same amount of points for array and matrix
        self.numpoints = min(len(self.fixedarray),len(self.movingarray))
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
                    self.moving[moving_array_bad[i]] = 0


    def matchPoints(self):
        #searching non-zero points
        idx=np.zeros(self.numpoints)
        self.matches = np.zeros(self.numpoints, dtype='(2,2)int8')
        for i in range(0,self.numpoints):
            #iterates through moving_array (new map)
            X = []
            for n in range(0,self.numpoints):
                #iterates through fixed_array (established map)
                #TODO: remove from matching list
                val = np.subtract(np.square(self.movingarray[i]),np.square(self.fixedarray[n]))    #gets hypotenuse
                X.append(np.square(val[0]+val[1]))                                             #square of error distance appended to X
            idx[i] = int(np.where(X == min(X))[0][0]) #found closest interesting point
            self.matches[i] = [self.movingarray[i],self.fixedarray[int(idx[i])]]


    def run(self):
        #run with two maps: fixed is the established map, moving is new map
        #while not rospy.is_shutdown():
        self.findPoints('maze1.pgm','fixed')
        self.arrangePoints('fixed')
        self.findPoints('maze1_2.pgm','moving')
        self.arrangePoints('moving')
        self.limitPoints()
        #NEVER CALLED LIMIT POINTS (I called above), so never set numpoints
        #working through limitPoints errors now
        self.matchPoints()
        #return self.matches
        self.showPoints('fixed')


if __name__ == "__main__":
    P=PointMatching()
    matching = P.run()
    print(matching)
    time.sleep(30)
