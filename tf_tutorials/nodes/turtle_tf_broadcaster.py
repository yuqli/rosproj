#!/usr/bin/env python
### 20181119
### Yuqiong Li
### Starting to learn turlesim and tf
import roslib
roslib.load_manifest("learning_tf")  # reads python path for the package learning_tf
import rospy

import tf
import turlesim

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     tf.transfromations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")

if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')
    turtlename = ros.getparam('~turtle')
    rospy.Subscriber('/%s/pose' % turtlename,  # subscribes to node /turtle/                     turtlesim.msg.Pose,  # what is this ? The argument of handle_turtle_pose?
                     handle_turtle_pose,  # the function above
                     turtlename)  # messanging interface?
    rospy.spin()
    
