#!/usr/bin/env python
# ROS python API
import rospy
from geometry_msgs.msg import PoseStamped

def publisher():
    rospy.init_node("dummy_publisher")
    goal_publisher = rospy.Publisher("dummpy/local_position/pose", PoseStamped, queue_size=10)
    goal = PoseStamped()
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # goal.header.seq = 1
        # goal.header.frame_id = "map"
        goal.header.stamp = rospy.Time.now()

        goal.pose.position.x = 0.0
        goal.pose.position.y = 0.0
        goal.pose.position.z = 0.0

        goal.pose.orientation.x = 0.0
        goal.pose.orientation.y = 0.0
        goal.pose.orientation.z = 0.0
        goal.pose.orientation.w = 1.0

        goal_publisher.publish(goal)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
