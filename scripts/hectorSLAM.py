#!/usr/bin/env python

import rospy
'''
how to launch:
roscore
roslaunch neato_node bringup_minimal.launch host:=IP_ADDRESS_OF_YOUR_ROBOT
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
rosbag record -a -x ".*map$" -o bag- file-name
roslaunch neato_2dnav hector_mapping_neato.launch
move around
rosrun map_server map_saver -f map-name (saves the map)
end hector_mapping


roslaunch com_robo_final_project test_bagfile.launch map_name:=map-name use_builtin:=true
'''
