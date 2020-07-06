#!/usr/bin/env python
# -*- coding: utf-8 -*-

#==================     Librerias      ==================#
import rospy  # Necesario para ROS
import getch
from std_msgs.msg import String, Float64  # String message
from std_msgs.msg import Int8

# pip install getch
pub_1 = rospy.Publisher(
    'front_joint_1_controller/command', Float64, queue_size=10)
pub_2 = rospy.Publisher(
    'front_joint_2_controller/command', Float64, queue_size=10)
pub_3 = rospy.Publisher(
    'rear_joint_1_controller/command', Float64, queue_size=10)
pub_4 = rospy.Publisher(
    'rear_joint_2_controller/command', Float64, queue_size=10)
max_vel = 5

#==================      Functions      ==================#
def keys():
    rospy.init_node('keypress', anonymous=True)
    while not rospy.is_shutdown():
        k = ord(getch.getch())
        if ((k == 67) | (k == 68) | (k == 66) | (k == 65)):
            rospy.loginfo(str(k))
            if k == 66 or k == 65:
                vel = 0
            elif k == 67:
                vel = 1
            else:
                vel = -1
            go_forward(vel*max_vel)


def go_forward(send_vel):
    global pub_1, pub_2, pub_3, pub_4
    pub_1.publish(send_vel)
    pub_2.publish(send_vel)
    pub_3.publish(send_vel)
    pub_4.publish(send_vel)


if __name__ == '__main__':
    try:
        keys()
    except rospy.ROSInterruptException:
        pass
