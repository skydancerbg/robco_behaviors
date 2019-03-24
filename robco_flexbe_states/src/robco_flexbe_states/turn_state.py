#!/usr/bin/env python
import rospy
import math

from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyPublisher, ProxySubscriberCached
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from tf import transformations

"""
#     #################################
#     # SRG Stefan: 
#     # Created by Stefan SRG 24.3.2019	
#     #################################
"""

class TurnState(EventState):
    '''
	Turns the robot in place to a set angle and with set speed.
    Uses /odom data.

	-- angle 	float 	Angle to turn to in degrees, +/- for direction.
    -- speed    float   Turn speed

	<= failed 			    If behavior is unable to ready on time
	<= done 				Example for a failure outcome.

	'''
    def __init__(self, angle, speed):

        super(TurnState, self).__init__(outcomes=['failed', 'done'])
        self.odom_data = None
        self.initial_orientation = None
        self.cur_orientation = None
        self._angle = angle
        self._speed = speed
        self._turn = False
        self._turn_angle = None
        self.cmd_pub = Twist()
        self._vel_topic = '/cmd_vel'
        self._odom_topic = '/odom'

        #create publisher passing it the vel_topic_name and msg_type
        self.pub_cmd_vel = ProxyPublisher({self._vel_topic: Twist})
        #create subscriber
        self.sub_odom = ProxySubscriberCached({self._odom_topic: Odometry})

    def execute(self, userdata):

        if self.sub_odom.has_msg(self._odom_topic):
            self.data = self.sub_odom.get_last_msg(self._odom_topic)
            self.sub_odom.remove_last_msg(self._odom_topic)
            # Logger.loginfo('New Current orientation from Odom data.pose.pose.orientation: %s' % self.data.pose.pose.orientation)
            self.cur_orientation = self.data.pose.pose.orientation
            
            cur_angle = transformations.euler_from_quaternion((self.cur_orientation.x, self.cur_orientation.y, 
            self.cur_orientation.z, self.cur_orientation.w))
    
            start_angle = transformations.euler_from_quaternion((self.initial_orientation.x, self.initial_orientation.y, 
            self.initial_orientation.z, self.initial_orientation.w))
            # Logger.loginfo('initial orientation: %f' % start_angle[2])
            # Logger.loginfo('current orientation: %f' % cur_angle[2])
            
            turned_so_far = math.fabs(cur_angle[2] - start_angle[2])
            # Logger.loginfo      ("The Robot turned so far: %s" % turned_so_far)
            
            if (turned_so_far >= self._turn_angle):
                # Turn completed
                self._turn = False
                Logger.loginfo ("Turn successfully completed!")
                return 'done'
                    
       
            # Turn the robot
            if self._turn:
                self.cmd_pub.linear.x = 0.0
                if self._angle   > 0:
                    self.cmd_pub.angular.z = self._speed
                else:
                    self.cmd_pub.angular.z = -self._speed
                self.pub_cmd_vel.publish(self._vel_topic, self.cmd_pub)
            
            else: # Send stop command to the robot if turning is completed
                self.cmd_pub.angular.z = 0.0
                self.pub_cmd_vel.publish(self._vel_topic, self.cmd_pub)


    def on_exit(self, userdata):
        self.cmd_pub.angular.z = 0.0
        self.pub_cmd_vel.publish(self._vel_topic, self.cmd_pub)
        Logger.loginfo("Turn in place COMPLETED! Exiting the state!")
        
    # def on_start(self):
    def on_enter(self, userdata):

        Logger.loginfo("Turn in place READY!")
        # self._start_time = rospy.Time.now() #bug detected! (move to on_enter)
        if not self.pub_cmd_vel:
            Logger.loginfo('Failed to setup the publisher.')
            return 'failed'

        # Read current orientation from /odom  
        if self.sub_odom.has_msg(self._odom_topic):
            self.data = self.sub_odom.get_last_msg(self._odom_topic)
            # Logger.loginfo('Set Initial Current Robot orientation: %s' % self.data.pose.pose.orientation)
            self.cur_orientation = self.data.pose.pose.orientation


        # TODO Seting publishing rate - should I do this in FlexBe????
        r = rospy.Rate(30)

        # Convert the input turn angle value from degrees to Rad
        self._turn_angle = math.fabs((self._angle   * math.pi)/ 180)
        Logger.loginfo ("Set TurnAngle _ angle to turn to in Rad: %s" % self._turn_angle)
        
        # Save the initial robot orientation in self.initial_orientation for latter use
        # if not self.initial_orientation:
        Logger.loginfo('Save the initial robot orientation ')
        self.initial_orientation = self.cur_orientation
        Logger.loginfo('Initial Robot orientation: %s' % self.initial_orientation)
        # Enable turning
        self._turn = True
   
        
    def on_stop(self):
		Logger.loginfo("Turn in place STOPPED!")
		self.initial_orientation = None
		self.cmd_pub.angular.z = 0.0
		self.cmd_pub.linear.x = 0.0
		self.pub_cmd_vel.publish(self._vel_topic, self.cmd_pub)

    def sub_odom_callback(self, data):
        self.data = data