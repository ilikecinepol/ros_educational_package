#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from hello_world.msg import IOTSensor
import random


def talker():
    pub = rospy.Publisher('iot_sensor_topic', IOTSensor, queue_size=10)
    rospy.init_node('IOT_sensor_publiser_node', anonymous=True)
    rospy.loginfo("IOT publicate")
    r = rospy.Rate(1)  # 1hz
    i = 0
    while not rospy.is_shutdown():
        data = IOTSensor()
        data.id = 1
        data.name = 'test_sensor'
        data.temperature = random.random()
        data.humidity = random.random()
        rospy.loginfo(str(i) + str(data))
        pub.publish(data)
        r.sleep()
        i += 1


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
