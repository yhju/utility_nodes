#!/usr/bin/env python

import roslib; roslib.load_manifest('utility_nodes')
import rospy
import tf
import math

from tf.transformations import euler_from_quaternion

from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion


def ImuCallback(data):
	#print data.orientation
	#print '---'
	quat = data.orientation
	q = [quat.x, quat.y, quat.z, quat.w]
	roll, pitch, yaw = euler_from_quaternion(q)
	print "angle: " + "{0:+.4f}".format(yaw) + " rad; "\
	+ "{0:+.2f}".format(math.degrees(yaw)) + " deg"
	print "rate:  " + "{0:+.2f}".format(data.angular_velocity.z) + " rad/s; "\
	+ "{0:+.2f}".format(math.degrees(data.angular_velocity.z)) + " deg/s"
	print '---'
	#qq = tf.transformations.quaternion_from_euler( 0, 0, yaw );
	#print qq
	#print '---'
	#print Quaternion(*qq)
	#print '---'

	
rospy.init_node("getYaw", anonymous=True)
rospy.Subscriber("imu", Imu, ImuCallback)
print 
print "It prints angle and angular_velocity from Imu message of single yaw gyro."
print
rospy.spin()
