import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class follower:
    def __init__(self):
        self.pose = Pose()
        self.msg = Twist()
        self.pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=1)
        self.sub1 = rospy.Subscriber('/turtle1/pose', Pose, self.follow)
        self.sub2 = rospy.Subscriber('/turtle2/pose', Pose, self.update)

    def update(self, turtle2Pose):
        self.pose = turtle2Pose

    def get_angle(self, pose1, pose2):
        return math.atan2(pose1.y - pose2.y, pose1.x - pose2.x) - pose2.theta

    def follow(self, turtle1Pose):
        self.msg.angular.z = 5 * self.get_angle(turtle1Pose, self.pose)
        self.msg.linear.x = turtle1Pose.linear_velocity

        self.pub.publish(self.msg)

rospy.init_node('turtle_listener')

f = follower()

rospy.spin()