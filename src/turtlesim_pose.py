#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from turtlesim.msg import Pose


def pose_callback(pose_message):
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta
    out_data = 'pose callback: x = ' + str(x) + ' y = ' + str(y) + ' yaw = ' + str(yaw)

    rospy.loginfo(out_data)

if __name__ == '__main__':
    try:
        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        rospy.Subscriber('turtle1/pose', Pose, pose_callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo('node termonated')
