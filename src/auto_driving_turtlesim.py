#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

x = 5.5
y = 5.5
yaw = 0


def poseCallback(pose_message):
    global x
    global y, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta
    # print(f'Current position: x0 = {x}, y0 = {y}')


def move(velocity_publisher, speed, distance, is_forward):
    # declare a Twist message to send velocity commands
    velocity_message = Twist()
    # get current location
    global x, y
    # set starting coordinates
    x0 = x
    y0 = y

    if (is_forward):
        velocity_message.linear.x = abs(speed)
    else:
        velocity_message.linear.x = -abs(speed)

    distance_moved = 0.0
    loop_rate = rospy.Rate(1)  # we publish the velocity at 10 Hz (10 times a second)

    while True:
        rospy.loginfo("Turtlesim moves forwards")
        velocity_publisher.publish(velocity_message)

        loop_rate.sleep()

        distance_moved = abs(math.sqrt(((x - x0) ** 2) + ((y - y0) ** 2)))
        print(distance_moved)
        if not (distance_moved < distance):
            rospy.loginfo("reached")
            break

    # finally, stop the robot when the distance is moved
    velocity_message.linear.x = 0
    velocity_publisher.publish(velocity_message)


def rotate(angular_speed_degree, relative_angle_degree, clockwise):
    velocity_message = Twist()

    angular_speed = math.radians(abs(angular_speed_degree))
    if (clockwise):
        velocity_message.angular.z = -abs(angular_speed)
    else:
        velocity_message.angular.z = abs(angular_speed)
    angle_moved = 0.0
    loop_rate = rospy.Rate(10)  # we publish the velocity at 10 Hz (10 times a second)
    t0 = rospy.Time.now().to_sec()

    while True:
        rospy.loginfo("Turtlesim rotates")
        velocity_publisher.publish(velocity_message)
        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1 - t0) * angular_speed_degree
        loop_rate.sleep()

        if (current_angle_degree > relative_angle_degree):
            rospy.loginfo("reached")
            break

    # finally, stop the robot when the distance is moved
    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message)


def go_to_goal(x_goal, y_goal):
    global x
    global y, yaw
    velocity_message = Twist()
    cmd_vel_topic = '/turtle1/cmd_vel'

    while (True):

        distance = abs(math.sqrt(((x_goal - x) ** 2) + ((y_goal - y) ** 2)))
        KP = 0.5
        linear_speed = distance * KP

        K_angular = 4.0
        desired_angle_goal = math.atan2(y_goal - y, x_goal - x)
        angular_speed = (desired_angle_goal - yaw) * K_angular

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed

        velocity_publisher.publish(velocity_message)

        # print velocity_message.linear.x
        # print velocity_message.angular.z
        print(f'x={x}, y={y}')

        if (distance < 0.01):
            break


def set_desired_orientation(speed_in_degree, desired_angle_degree):
    relative_angle_radians = math.radians(desired_angle_degree) - yaw
    # clockwise = 0
    clockwise = 1 if relative_angle_radians < 0 else 0
    print('relative angle radians: ', math.degrees(relative_angle_radians))
    print('desired angle degree: ', desired_angle_degree)
    rotate(speed_in_degree, math.degrees(abs(relative_angle_radians)), clockwise)


def spiral_motion(velocity_publisher, kl, ka=2.5):
    vel_msg = Twist()
    loop_rate = rospy.Rate(1)

    while x < 10.5 and y < 10.5:
        kl += 0.5
        vel_msg.linear.x = kl
        vel_msg.angular.z = ka
        velocity_publisher.publish(vel_msg)
        loop_rate.sleep()

    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)


def grid_clean(publisher):
    desiered_pose = Pose()
    desiered_pose.x = 1
    desiered_pose.y = 1
    desiered_pose.theta = 0

    go_to_goal(1,1)
    set_desired_orientation(10, math.radians(desiered_pose.theta))


if __name__ == '__main__':
    try:

        rospy.init_node('turtlesim_motion_pose', anonymous=True)
        cmd_vel_topic = '/turtle1/cmd_vel'

        position_topic = '/turtle1/pose'
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        # move(velocity_publisher, 1.0, 4.0, True)
        # rotate(90, 90, True)
        # go_to_goal(1.2, 9.9)
        # speed_in_degree = int(input('input speed: '))
        # desired_angle = int(input('input desired angle: '))
        # set_desired_orientation(float(speed_in_degree), float(desired_angle))
        spiral_motion(velocity_publisher, 0.1)
        grid_clean(velocity_publisher)
        time.sleep(1.0)


    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
