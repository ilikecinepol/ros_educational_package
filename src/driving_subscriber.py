#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO

in1 = 16
in2 = 26
in3 = 20
in4 = 21
en_r = 13
en_l = 12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = [in1, in2, in3, in4, en_r, en_l]
GPIO.setup(pins, GPIO.OUT)

pwm_r = GPIO.PWM(en_r, 50)
pwm_r.start(0)
pwm_l = GPIO.PWM(en_l, 50)
pwm_l.start(0)


def driving(data):
    speed_linear = data.linear.x
    speed_angular = data.angular.z
    rospy.loginfo('x: ', str(data.linear.x), 'z: ', str(data.angular.z))
    speed_l = 0
    speed_r = 0

    if speed_linear > 0 and speed_angular == 0.0:
        GPIO.output([in1, in3], GPIO.HIGH)
        GPIO.output([in2, in4], GPIO.LOW)
    elif speed_linear < 0 and speed_angular == 0.0:
        GPIO.output([in2, in4], GPIO.HIGH)
        GPIO.output([in1, in3], GPIO.LOW)
    else:
        if speed_angular > 0:
            pwm_r.ChangeDutyCycle(speed_r)
        else:
            pwm_l.ChangeDutyCycle(speed_l)


rospy.init_node('turtle_driving_node', anonymous=True)

rospy.Subscriber('cmd_vel', Twist, driving)
rospy.spin()

if __name__ == '__main__':
    while True:
        try:
            r = int(input('r: '))
            l = int(input('l: '))
            drive(r, l)
        except KeyboardInterrupt:
            pwm_r.stop()
            pwm_l.stop()
            GPIO.cleanup()
            break
