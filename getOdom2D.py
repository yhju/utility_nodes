#!/usr/bin/env python

import roslib; roslib.load_manifest('utility_nodes')
import rospy
import tf
import math

from tf.transformations import euler_from_quaternion

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Pose2D #pubilsh to pose2d

def OdomCallback(data):
	#print data.orientation
	#print '---'
	px = data.pose.pose.position.x
	py = data.pose.pose.position.y
	quat = data.pose.pose.orientation
	q = [quat.x, quat.y, quat.z, quat.w]
	roll, pitch, yaw = euler_from_quaternion(q)

	vx = data.twist.twist.linear.x
	vy = data.twist.twist.linear.y
	yaw_rate = data.twist.twist.angular.z
	print "pose: x: {0:+2.5f}".format(px) + ", y: {0:+2.5f}".format(py)\
	+ ", th: {0:+.4f}".format(yaw) + " rad; "\
	+ "{0:+.2f}".format(math.degrees(yaw)) + " deg"
	print "rate: x: {0:+2.5f}".format(vx) + ", y: {0:+2.5f}".format(vy)\
	+ ", th: {0:+.2f}".format(yaw_rate) + " rad/s; "\
	+ "{0:+.2f}".format(math.degrees(yaw_rate)) + " deg/s"
	print '---'
	#qq = tf.transformations.quaternion_from_euler( 0, 0, yaw );
	#print qq
	#print '---'
	#print Quaternion(*qq)
	#print '---'

	
rospy.init_node("getOdom2D", anonymous=True)
rospy.Subscriber("odom", Odometry, OdomCallback)
print 
print "It prints angle and angular_velocity from Imu message of single yaw gyro."
print
rospy.spin()
