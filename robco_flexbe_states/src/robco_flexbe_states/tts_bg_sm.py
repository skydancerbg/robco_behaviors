#!/usr/bin/env python
import rospy
import math

from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyPublisher, ProxySubscriberCached
from std_msgs.msg import String

"""
#     #################################
#     # 
#     # Created by Stefan 
#     # SRG - Service Robotics Group Bulgaria
#     # Version 1.0 from Apr. 3th, 2019.
#     #
#     #################################
"""
#
#     There is no good Bulgarian Voice in Ubuntu. 
#     As a workaround, we are forced to start a Windows VM
#     and synthesize the speech there, playing it back on the Robco robot speakers
#     over a bluetooth connection
#     
#     #################################
#     
#     # On the ROS side:
#     # Set serializer/deserializer in mqtt_bridge: /home/robcoctrl/catkin_ws/src/mqtt_bridge/config/openhab_tts_stt_params.yaml
#     # to:   serializer: json:dumps        deserializer: json: loads
#
# ########## Publish/Subscribe to TTS (Text To Speech) Bulgarian topics ROS/MQTT communication ##########
# //////////////////////////////////////////////////////////////////////////////////////////////////////
# //
# // ROS topics: 
# //        /ttsbg_ros/tts_text           String
# //        /ttsbg_ros/command            String
# //        /ttsbg_ros/response           String
# // MQTT topics: 
# //          /ttsbg_mqtt/tts_text        String
# //          /ttsbg_mqtt/command         String
# //          /ttsbg_mqtt/response        String
# //
# // The mqtt_bridge ROS package is set to transfer the messages between ROS and the MQTT broker, between the corrresponding topics
# // These topics are configured in ROS mqtt_bridge package, in /home/<your user>/catkin_ws/src/mqtt_bridge/config/openhab_tts_stt_params.yaml
# // In the same config file, set serializer/deserializer for mqtt_bridge to:   serializer: json:dumps        deserializer: json: loads
# ///////////////////////////////////////////////////////////////////////////////////////////////////////

# TODO
#   This state is of type fire and forget - no response from the TTS engine, even if it does not exist...
#   Create action server and a new FlexBe state, which to be able to get the current state of the TTS engine

class TTSBulgarian(EventState):
    '''
    TTS in Bulgarian language, sends messages trough MQTT to the Windows TTS VM console app.
    Sends a string to /ttsbg_mqtt/tts_text MQTT topic,
    trough sending a ROS String message to ROS topic /ttsbg_ros/tts_text
    mqtt_bridge resends the ROS message to the MQTT broker on /ttsbg_mqtt/tts_text.
    Default MQTT broker IP is 192.168.1.2

    -- ttsbg_text    String   Text to be synthesized

    <= failed                             If behavior is unable to send the TTS message
    <= done                                 TTS message sent succesfully
    '''

    def __init__(self, ttsbg_text):

        super(TTSBulgarian, self).__init__(outcomes=['failed', 'done'])
        self.odom_data = None
        self.initial_orientation = None
        self.cur_orientation = None
        self._ttsbg_text_to_be_synthesized = ttsbg_text

        self._ttsbg_text_to_be_synthesized_topic = '/ttsbg_ros/tts_text'
        self._ttsbg_command_topic = '/ttsbg_ros/command'
        self._ttsbg_response_topic = '/ttsbg_ros/response'
        #create publisher passing it the ttsbg_topic and msg_type
        self.pub_ttsbg_text = ProxyPublisher({self._ttsbg_text_to_be_synthesized_topic: String})
        #create publisher passing it the ttsbg_topic and msg_type
        self.pub_ttsbg_command = ProxyPublisher({self._ttsbg_command_topic: String})

        #create subscriber
        self.sub_ttsbg_response = ProxySubscriberCached({self._ttsbg_response_topic: String})

    def execute(self, userdata):

        # Logger.loginfo('V execute sam....')
        self.pub_ttsbg_text.publish(self._ttsbg_text_to_be_synthesized_topic, self._ttsbg_text_to_be_synthesized)
        return 'done'


    def on_exit(self, userdata):
        pass
    def on_stop(self):
        pass


