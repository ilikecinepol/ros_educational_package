#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

print('read an image from file')
image_name = 'tree'
color_img = cv2.imread('images/' + image_name + '.jpg', cv2.IMREAD_COLOR)

height, width, channels = color_img.shape

print('Split the image into tree channel')
blue, green, red = cv2.split(color_img)

print('display the image')
cv2.imshow('Original image', color_img)
cv2.moveWindow('Original image', 0, 0)

cv2.imshow('Blue channel', blue)
cv2.moveWindow('Blue channel', 2 * width + 10, 0)
cv2.imshow('Green channel', green)
cv2.moveWindow('Green channel', 3 * width + 100, 0)
cv2.imshow('Red channel', red)
cv2.moveWindow('Red channel', 4 * width + 100, 0)

print('Convert to HSV')
hsv = cv2.cvtColor(color_img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
hsv_img = np.concatenate((h,s,v), axis=1)
cv2.imshow('HSV image', hsv_img)

cv2.waitKey(0)
cv2.destroyWindow()
