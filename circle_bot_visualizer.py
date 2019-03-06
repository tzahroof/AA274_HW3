#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from visualization_msgs.msg import Marker
from std_msgs.msg import ColorRGBA, Header
from geometry_msgs.msg import Pose, Quaternion, Point, Vector3
import tf

def work():
	# #Create the circle_marker message
	# circle_marker = Marker()
	# circle_marker.header.frame_id = "/base_footprint"
	# circle_marker.ns = "circle_bot_marker"
	# circle_marker.type = Marker.CYLINDER
	# circle_marker.scale.x = 0.01
	# circle_marker.scale.y = 0.01
	# circle_marker.scale.z = 0.01
	# circle_marker.color.g = 1
	# circle_marker.color.a = 1


	pub = rospy.Publisher('/viz/circle_bot_marker', Marker, queue_size=10)
	rospy.init_node('publisher', anonymous=True)
	rate = rospy.Rate(100)

	while not rospy.is_shutdown():
		### Insert Code here to publish a string ###
		marker = Marker(type=Marker.SPHERE, id=0, scale=Vector3(0.2,0.2, 0.1), 
					pose=Pose(Point(0.0, 0.0, 0), Quaternion(0, 0, 0, 1)), 
					header=Header(frame_id='base_footprint', stamp=rospy.Time(0)), 
					color=ColorRGBA(0.0, 1.0, 0.0, 1.0))
		pub.publish(marker)

		rate.sleep()

if __name__ == '__main__':
	try:
		work()
	except rospy.ROSInterruptException:
		pass