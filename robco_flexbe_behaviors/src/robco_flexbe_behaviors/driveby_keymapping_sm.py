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
Created on Mon Jul 30 2018
@author: Ephson
'''
class DriveByKeyMappingSM(Behavior):
	'''
	New logic Added
	'''


	def __init__(self):
		super(DriveByKeyMappingSM, self).__init__()
		self.name = 'DriveBy KeyMapping'

		# parameters of this behavior
		self.add_parameter('my_speed', 0.4)
		self.add_parameter('turn_angle', 90)
		self.add_parameter('travel_dist', 5)
		self.add_parameter('obstacle_dist', 1.5)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:678 y:98, x:682 y:193
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.data_OUT = self.travel_dist

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:134 y:114
			OperatableStateMachine.add('Drive',
										GoFowardState(speed=self.my_speed, travel_dist=self.travel_dist, obstacle_dist=self.obstacle_dist),
										transitions={'failed': 'Turn', 'done': 'finished'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Off},
										remapping={'remaining_travel_dist_IN': 'data_OUT', 'remaining_travel_dist_OUT': 'data_IN'})

			# x:367 y:227
			OperatableStateMachine.add('Turn',
										TurnState(turn_angle=self.turn_angle, t_speed=self.my_speed),
										transitions={'done': 'Drive', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'data_IN': 'data_IN', 'data_OUT': 'data_OUT'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
