#!/usr/bin/env python

import rospy
import bluetooth
from std_msgs.msg import String
from beginner_tutorials.msg import Auditory

def talker():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(('', 1))
    server_sock.listen(1)
    client_sock = []

    try:
        client_sock, address = server_sock.accept()
        print('Accepted connection from', address)

        rospy.init_node('earModule', anonymous=True)
        pub = rospy.Publisher('earSignal', Auditory, queue_size=100)
        msg = Auditory()    
        while not rospy.is_shutdown():
            data = client_sock.recv(1024)            
            if data:
                msg.info = data
            else:
                msg.info = 'na'
            msg.earR = 123.456
            msg.earL = 246.802
            msg.timecode = str(rospy.get_time())
            rospy.loginfo(msg)
            pub.publish(msg)

    except:
        if client_sock:
            client_sock.close()
        server_sock.close()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

