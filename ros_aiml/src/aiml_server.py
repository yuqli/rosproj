#!/usr/bin/python2
## 20181117
## Yuqiong Li

def load_aiml():
    data_path = rospy.get_parm("aiml_path")
    print data_path
    os.chdir(data_path)

    if os.paht.isfile("standard.brn"):
        mybot.bootstrap(brainFile="standard.brn")
    else:
        mybot.bootstrap(learnFile=xml_file, commands="LOAD AIML B")
        mybot.saveBrain("standard.brn")

def callback(data):
    input = data.data
    response = mybot.respond(input)
    rospy.loginfo("I heard:: %s".data.data)
    rospy.loginfo("I spoke:: $s".response)
    response_publisher.publish(response)

def listener():
    rospy.loginfo("Starting ROS AIML server")
    rospy.subscriber("chatter", Sring, callback)
    rospy.spin()

if __name__=='__main__':
    load_aiml('../startup.xml')
    listener()
