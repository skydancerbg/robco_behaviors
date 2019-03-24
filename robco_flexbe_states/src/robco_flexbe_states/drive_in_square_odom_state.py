#!/usr/bin/env python
import rospy

from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyPublisher
from geometry_msgs.msg import Twist
from math import radians

"""
#     #################################
#     # SRG Stefan: 
#     # Created by Stefan SRG 23.3.2019, based on:	
#     # 
#     # https://github.com/markwsilliman/turtlebot/blob/master/draw_a_square.py
#     #################################
"""


class DriveInSquareByOdom(EventState):
	'''
	Drive the robot in squre using odom (cmd_vel)- not acurate!
	TODO change this text: This example lets the behavior wait until the given target_time has passed since the behavior has been started.

 	-- square_side_in_m float     Lenght of the side for the square in meters.
	-- speed 	float 	Speed at which to drive the robot

	<= continue 			Driving the square finished
	<= failed 				TODO Change or remove this outcome! Example for a failure outcome.

	'''

	def __init__(self, target_time, square_side_in_m, speed):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(DriveInSquareByOdom, self).__init__(outcomes = ['continue', 'failed'])

		self._target_time = rospy.Duration(target_time)
		self._square_side_lenght = square_side_in_m
		self._speed = speed
		self.vel_topic = '/cmd_vel'
		self.pub = ProxyPublisher({self.vel_topic: Twist}) # TODO set publish rate to 5 HZ
		self.finished = False

	def execute(self, userdata):
		# This method is called periodically while the state is active.
		# Main purpose is to check state conditions and trigger a corresponding outcome.
		# If no outcome is returned, the state will stay active.

		# create two different Twist() variables.  One for moving forward.  One for turning 45 degrees.
		# for x in range(4):
		# let's go forward at 0.2 m/s
		move_cmd = Twist()
		move_cmd.linear.x = 0.2
		# by default angular.z is 0 so setting this isn't required
        # 		#let's turn at 45 deg/s

		turn_cmd = Twist()
		turn_cmd.linear.x = 0
		turn_cmd.angular.z = radians(45) #45 deg/s in radians/s

		count = 0
		while not (count < 5) :
			Logger.loginfo("Going Straight")
			for x in range(0,10):
				self.pub.publish(move_cmd)
				# r.sleep()

			# turn 90 degrees
			Logger.loginfo("Turning")
			for x in range(0,10):
				self.pub.publish(turn_cmd)
				# r.sleep()            
			count = count + 1
			if(count == 4): 
				count = 0
			if(count == 0): 
				Logger.loginfo("The robot should be close to the original starting position (but it's probably way off)")

	    

		if self.finished:
			self.pub.publish(Twist())
			Logger.loginfo('The robot finished dirving in a square.')
			return 'continue'
		

	def on_enter(self, userdata):
		# This method is called when the state becomes active, i.e. a transition from another state to this one is taken.
		# It is primarily used to start actions which are associated with this state.

		Logger.loginfo('The robot will drive using cmd_vel (odom data) in a square with side lenght of %.1f meters.' % userdata.square_side_in_m)


	def on_exit(self, userdata):
		# This method is called when an outcome is returned and another state gets active.
		# It can be used to stop possibly running processes started by on_enter.

		pass # Nothing to do in this example.


	def on_start(self):
        
		# This method is called when the behavior is started.
		# If possible, it is generally better to initialize used resources in the constructor
		# because if anything failed, the behavior would not even be started.
		pass # Nothing to do in this example.

	def on_stop(self):
		# This method is called whenever the behavior stops execution, also if it is cancelled.
		# Use this event to clean up things like claimed resources.

		pass # Nothing to do in this example.
		
