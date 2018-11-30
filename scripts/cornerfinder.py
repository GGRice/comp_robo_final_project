#!/usr/bin/env python

import rospy
import cv2
import numpy as np


def find_points(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)

    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)
    #for showing image
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst>0.01*dst.max()]=[0,0,255]
    cv2.imshow('dst',img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
    return dst
'''
def match_points(fixed, moving):
    #finding nonzeros
    for i in len(fixed):
        for i in len(fixed[1]):

    f = np.transpose(np.nonzero(fixed))
    m = np.transpose(np.nonzero(fixed))
    print(type(fixed[1]))
'''



fixed = find_points('room1.jpg')
moving = find_points('room2.jpg')

#match_points(fixed, moving)
