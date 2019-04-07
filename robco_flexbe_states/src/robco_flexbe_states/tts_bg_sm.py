#!/usr/bin/env python
import rospy
import math

from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyPublisher, ProxySubscriberCached
from std_msgs.msg import String

"""
#     #################################
#       SRG Stefan:
#       Created by Stefan SRG 3.4.2019
#     #################################
"""
# //////////////////////////////////////////////////////////////////////////////////////////////////////
# //
# // ROS topics:
# //        /ttsbg_ros/text_to_be_spoken
# //        /ttsbg_ros/command
# //        '/ttsbg_ros/response
# // MQTT topics: 
# //          /ttsbg_mqtt/text_to_be_spoken
# //          /ttsbg_mqtt/command
# //          /ttsbg_mqtt/
# //
# // mqtt_bridge ROS package is set to transfer the messages between ROS and the MQTT broker in both directions
# // Topics have to be setup in mqtt_bridge package in /home/robcoctrl/catkin_ws/src/mqtt_bridge/config/openhab_tts_params.yaml
# //
# ///////////////////////////////////////////////////////////////////////////////////////////////////////


class TTSBulgarian(EventState):
    '''
    TTS in Bulgarian language, sends messages trough MQTT to the Windows TTS VM console app.
    Sends a string to /ttsbg_mqtt/text_to_be_spoken MQTT topic,
    trough ROS topic /ttsbg_ros/text_to_be_spoken.
    Using mqtt_bridge package.
    Default MQTT broker IP is 192.168.1.2

    -- ttsbg_text    String   Text to be spoken

    <= failed                             If behavior is unable to send the TTS message
    <= done                                 TTS message sent succesfully
    '''

    def __init__(self, ttsbg_text):

        super(TTSBulgarian, self).__init__(outcomes=['failed', 'done'])
        self.odom_data = None
        self.initial_orientation = None
        self.cur_orientation = None
        self._ttsbg_text_to_be_spoken = ttsbg_text

        self._ttsbg_text_to_be_spoken_topic = '/ttsbg_ros/tts_text'
        self._ttsbg_command_topic = '/ttsbg_ros/command'
        self._ttsbg_response_topic = '/ttsbg_ros/response'
        #create publisher passing it the ttsbg_topic and msg_type
        self.pub_ttsbg_text = ProxyPublisher({self._ttsbg_text_to_be_spoken_topic: String})
        #create publisher passing it the ttsbg_topic and msg_type
        self.pub_ttsbg_command = ProxyPublisher({self._ttsbg_command_topic: String})

        #create subscriber
        self.sub_ttsbg_response = ProxySubscriberCached({self._ttsbg_response_topic: String})

    def execute(self, userdata):

        # Logger.loginfo('V execute sam....')
        self.pub_ttsbg_text.publish(self._ttsbg_text_to_be_spoken_topic, self._ttsbg_text_to_be_spoken)
        return 'done'


    def on_exit(self, userdata):
        pass
    def on_stop(self):
        pass


