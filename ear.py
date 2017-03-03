#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from beginner_tutorials.msg import Auditory

def talker():
    rospy.init_node('earModule', anonymous=True)
    rate = rospy.Rate(2)
    pub = rospy.Publisher('earSignal', Auditory, queue_size=100)
    msg = Auditory()    
    while not rospy.is_shutdown():
        msg.info = 'test signal.'
        msg.earR = 123.456
        msg.earL = 246.802
        msg.timecode = str(rospy.get_time())
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
