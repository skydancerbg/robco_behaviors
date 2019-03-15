#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from turtlebot_flexbe_states.go_forward_state import GoFowardState
from turtlebot_flexbe_states.turn_state import TurnState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue Jul 17 2018
@author: Ephson
'''
class DriveForwardSM(Behavior):
	'''
	Enables robot to move a certain distance.
	'''


	def __init__(self):
		super(DriveForwardSM, self).__init__()
		self.name = 'Drive Forward'

		# parameters of this behavior
		self.add_parameter('my_speed', 0.4)
		self.add_parameter('distance_to_travel', 2)
		self.add_parameter('obstance_distance', 1.5)
		self.add_parameter('turn_angle_3', 0)
		self.add_parameter('turn_speed', 0.4)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:780 y:93, x:798 y:306
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:168 y:169
			OperatableStateMachine.add('Drive State',
										GoFowardState(speed=self.my_speed, travel_dist=self.distance_to_travel, obstacle_dist=self.obstance_distance),
										transitions={'failed': 'TurnAround', 'done': 'finished'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Off})

			# x:467 y:217
			OperatableStateMachine.add('TurnAround',
										TurnState(turn_angle=self.turn_angle_3, t_speed=self.turn_speed),
										transitions={'done': 'Drive State', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
