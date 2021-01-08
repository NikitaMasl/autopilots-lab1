#! /usr/bin/python

import rospy
import random
from turtlesim.srv import Spawn

rospy.init_node('turtle_spawner')

rospy.wait_for_service('/spawn')
spawn_func = rospy.ServiceProxy('/spawn', Spawn)

turtle = spawn_func(random.uniform(0.0, 10.0), random.uniform(0.0, 10.0), random.uniform(0.0, 10.0), 'turtle2')