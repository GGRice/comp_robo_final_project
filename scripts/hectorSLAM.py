#!/usr/bin/env python

import rospy

#how to launch:
#roscore & connect to neato, teleop to move around
#roslaunch neato_node bring_minimal.launch host:=IP_ADDRESS_OF_YOUR_ROBOT
#rosbag record -a -x ".*map$" -o bag- file-name
#roslaunch neato_2dnav hector_mapping_neato.launch
#move around
#rosrun map_server map_saver -f ~/mymap (saves the map)
#end hector_mapping


#roslaunch robot_localizer test_bagfile.launch map_name:=ac109_1 use_builtin:=true
