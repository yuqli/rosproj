#!usr/bin/env python2
import rospy
from std_msgs.msg import String
rospy.init_node('aiml_speech_recog_client')
pub = rospy.Publisher('chatter', String, queue_size=10)
r = ros.Rate(1)

def get_speech(data):
    speech_text = data.data
    rospy.loginfo("I said:: %s", speech_text)
    pub.publish(speech_text)

def listener():
    rospy.loginfo("Starting speech recognition")
    rospy.Subscriber("/recognizer/output", String, get_speech)
    rospy.spin()

while not rospy.is_shutdown():
    listenr()
