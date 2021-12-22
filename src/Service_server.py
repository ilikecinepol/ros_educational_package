#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hello_world.srv import AddTwoInts
from hello_world.srv import AddTwoIntsRequest
from hello_world.srv import AddTwoIntsResponce

import rospy
#from hello_world.srv import AddTwoInts


def handle_add_two_ints(req):
    rospy.loginfo('Returning %s + %s = %s' % (req.a, req.b, (req.a + req.b)))
    return AddTwoIntsResponce(req.a + req.b)


def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    rospy.loginfo('Ready AddTwoInts')
    rospy.spin


if __name__ == '__main__':
    add_two_ints_server()
