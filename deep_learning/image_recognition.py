#!/usr/bin/env python
### https://github.com/qboticslabs/rostensorflow/blob/master/image_recognition.py

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.models.image.imagenet import classify_image

sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

class RosTensorflow():
    def __init__(self):
        classify_image.maybe_download_and_extract()  # what does it do?
        self._session = tf.Session()
        classify_image.create_graph()
        self._cv_bridge = CvBridge()  # what does this do?

        self._sub = rospy.Subscriber('image', Image, self.callback, queue_size=1)  # callback is the argument if we callback or # NOTE:
        self._pub = rospy.Publisher('result', String, queue_size=1)
        self.score_threshold = rospy.get_param('~score_threshold', 0.1)  # ~ means private name
        self.use_top_k = rospy.get_param('~use_top_k', 5)

    def callback(self, image_msg):
        # convert image from ROS image msg type to opencv format
        cv_image = self._cv_bridge.imgmsg_to_cv2(image_msg, "bgr8")
        image_data = cv2.imencode('.jpg', cv_image)[1].tostring()
        softmax_tensor = self._session.graph.get_tensor_by_name('softmax:0')
        predictions = self._session.run(
            softmax_tensor, {'DecodeJpeg/contents:0':image_data}
        )
        predictions = np.squeeze(predictions)
        # create nodeID -- english string lookup
        node_lookup = classify_image.NodeLookup()
        top_k = predictions.argsort()[-self.use_top_k:][::-1]  # get top k
        for node_id in top_k:
            human_string = node_lookup.id_to_string(node_id)
            score = predictions[node_id]
            if score > self.score_threshold:
                rospy.loginfo('%s (score = %.5f)' %(human_string, score))
                self._pub.publish(human_string)

    def main(self):
        rospy.spin()


if __name__ == "__main__":
    rospy.init_node('rostensorflow')
    tensor = RosTensorflow()
    tensor.main()
