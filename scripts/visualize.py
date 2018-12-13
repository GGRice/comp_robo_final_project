#!/usr/bin/env python


import numpy as np
import cv2

class Vizualize(object):
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
