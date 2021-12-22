#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
from hello_world.srv import AddTwoInts
from hello_world.srv import AddTwoIntsRequest
from hello_world.srv import AddTwoIntsResponce


def add_two_ints_cliet(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp1 = add_two_ints(x, y)
        return resp1.sum
    except ServiceException(e):
        print('Service call failed')

def usage():
    return

if __name__ == '__main__':
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print('%s [x y]'%sys.argv[0])
        sys.exit(1)
    print('requesting %s+%s'%(x, y))
    s = add_two_ints_cliet(x, y)
    print(s)
