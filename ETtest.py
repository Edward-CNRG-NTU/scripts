#!/usr/bin/env python

import rospy
import socket
from beginner_tutorials.msg import Auditory

def talker():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind(('127.0.0.1', 11111))
    except socket.error as msg:
        rospy.loginfo("[ERROR] %s\n" % msg[1])

    rospy.init_node('earModule', anonymous=True)
    pub = rospy.Publisher('earSignal', Auditory, queue_size=100)
    msg = Auditory()    
    while not rospy.is_shutdown():
        data, address = sock.recvfrom(1024)
        sock.sendto('ack', ('127.0.0.1', 11112))
        if data:
            msg.info = data
        else:
            msg.info = 'na'
        msg.earR = 123.456
        msg.earL = 246.802
        msg.timecode = str(rospy.get_time())
        rospy.loginfo(msg)
        pub.publish(msg)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

