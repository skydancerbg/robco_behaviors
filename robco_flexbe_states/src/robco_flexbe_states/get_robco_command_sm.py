#!/usr/bin/env python

import rospy

from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyPublisher, ProxySubscriberCached
from std_msgs.msg import String

"""
#     #################################
#     # 
#     # Created by Stefan 
#     # SRG - Service Robotics Group Bulgaria
#     # Version 1.0 from Apr. 9-th, 2019.
#     #
#     #################################
"""
#
# ########## Listen to /robco/command and get new incomming command ##########
# //////////////////////////////////////////////////////////////////////////////////////////////////////
# //
# // ROS topics: 
# //        /robco/command           String
# //
# ///////////////////////////////////////////////////////////////////////////////////////////////////////


class GetRobcoCommand(EventState):
    '''
    Listens to /robco/command and gets the incomming command.

    #> robco_command_OUT    String   Last received robco command

    <= failed                             If behavior is unable to send the TTS message
    <= done                                 TTS message sent succesfully
    '''

    def __init__(self):

        super(GetRobcoCommand, self).__init__(outcomes=['failed', 'done'], output_keys=['robco_command_OUT'])

        self._command_topic = '/robco/command'
        self.command = None

        #create subscriber
        self.sub = ProxySubscriberCached({self._command_topic: String})

    def execute(self, userdata):

        if self.sub.has_msg(self._command_topic):
            command = self._sub.get_last_msg(self._command_topic)
            userdata.robco_command_OUT = command.data
            Logger.loginfo('Incomming command on /robco/command topic: %s' % command)

            # in case you want to make sure the same message is not processed twice:
            self._sub.remove_last_msg(self._command_topic)
            return 'done'


    def on_exit(self, userdata):
        #TODO unsubscribe the subscriber proxy from that topic?
        # self.sub.????
        pass
    def on_stop(self):
        pass


