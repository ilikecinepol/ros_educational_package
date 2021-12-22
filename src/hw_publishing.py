#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rospy.loginfo("Hello from PUB node")
    r = rospy.Rate(1)  # 1hz
    i = 0
    while not rospy.is_shutdown():
        hello_str = "Hello world %s" % i
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        r.sleep()
        i += 1


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


