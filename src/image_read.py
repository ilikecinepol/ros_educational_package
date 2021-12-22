#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

print('read an image from file')
image_name = 'tree'
img = cv2.imread('images/' + image_name + '.jpg')

print('create a window holder for the image')
cv2.namedWindow(image_name, cv2.WINDOW_NORMAL)

print('display the image')
cv2.imshow(image_name, img)

print('press any cey inside the image to make a copy')
cv2.waitKey(0)

print('image copied to folder images/copy')
cv2.imwrite('images/copy/' + image_name + '_copy.jpg', img)
