#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String


def chatter_callback(message):
    rospy.loginfo('i heart %s', message.data)




rospy.init_node('listener', anonymous=True)

rospy.Subscriber('chatter', String, chatter_callback)
rospy.spin()