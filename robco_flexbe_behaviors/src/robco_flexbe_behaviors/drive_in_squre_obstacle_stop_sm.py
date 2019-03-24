#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robco_flexbe_states.go_forward_state import GoFowardState
from robco_flexbe_states.turn_state import TurnState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sat Mar 23 2019
@author: Stefan
'''
class Drive_In_Squre_Obstacle_StopSM(Behavior):
	'''
	Drives the robot ina square with side lenght based on imput value, by using cmd_vel and fused odometry. I case of obstacle infornt at the set (input) distace fails.
	'''


	def __init__(self):
		super(Drive_In_Squre_Obstacle_StopSM, self).__init__()
		self.name = 'Drive_In_Squre_Obstacle_Stop'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1023 y:583, x:219 y:689
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.travel_dist_IN = 0.5

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:81 y:68
			OperatableStateMachine.add('Go Forward First Leg',
										GoFowardState(speed=0.3, travel_dist=0.5, obstacle_dist=0.2),
										transitions={'failed': 'failed', 'done': 'Turn In Place To Set Degree First'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Low},
										remapping={'remaining_travel_dist_IN': 'travel_dist_IN', 'remaining_travel_dist_OUT': 'remaining_travel_dist_OUT'})

			# x:690 y:153
			OperatableStateMachine.add('Go Forward Second Leg',
										GoFowardState(speed=0.3, travel_dist=0.5, obstacle_dist=0.2),
										transitions={'failed': 'failed', 'done': 'Turn In Place Second'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Low},
										remapping={'remaining_travel_dist_IN': 'remaining_travel_dist_OUT', 'remaining_travel_dist_OUT': 'remaining_travel_dist_OUT'})

			# x:392 y:14
			OperatableStateMachine.add('Turn In Place To Set Degree First',
										TurnState(turn_angle=90, t_speed=0.2),
										transitions={'done': 'Go Forward Second Leg', 'failed': 'failed'},
										autonomy={'done': Autonomy.Low, 'failed': Autonomy.Off},
										remapping={'data_IN': 'remaining_travel_dist_OUT', 'data_OUT': 'remaining_travel_dist_OUT'})

			# x:62 y:185
			OperatableStateMachine.add('Go Forward Third Leg',
										GoFowardState(speed=0.3, travel_dist=0.5, obstacle_dist=0.2),
										transitions={'failed': 'failed', 'done': 'Turn In Place Third'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Low},
										remapping={'remaining_travel_dist_IN': 'remaining_travel_dist_OUT', 'remaining_travel_dist_OUT': 'remaining_travel_dist_OUT'})

			# x:443 y:213
			OperatableStateMachine.add('Turn In Place Second',
										TurnState(turn_angle=90, t_speed=0.2),
										transitions={'done': 'Go Forward Third Leg', 'failed': 'failed'},
										autonomy={'done': Autonomy.Low, 'failed': Autonomy.Off},
										remapping={'data_IN': 'remaining_travel_dist_OUT', 'data_OUT': 'remaining_travel_dist_OUT'})

			# x:388 y:317
			OperatableStateMachine.add('Turn In Place Third',
										TurnState(turn_angle=90, t_speed=0.2),
										transitions={'done': 'Go Forward Fourth Leg', 'failed': 'failed'},
										autonomy={'done': Autonomy.Low, 'failed': Autonomy.Off},
										remapping={'data_IN': 'remaining_travel_dist_OUT', 'data_OUT': 'remaining_travel_dist_OUT'})

			# x:739 y:326
			OperatableStateMachine.add('Go Forward Fourth Leg',
										GoFowardState(speed=0.3, travel_dist=0.5, obstacle_dist=0.2),
										transitions={'failed': 'failed', 'done': 'Turn In Place Fourth'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Low},
										remapping={'remaining_travel_dist_IN': 'remaining_travel_dist_OUT', 'remaining_travel_dist_OUT': 'remaining_travel_dist_OUT'})

			# x:738 y:467
			OperatableStateMachine.add('Turn In Place Fourth',
										TurnState(turn_angle=90, t_speed=0.2),
										transitions={'done': 'finished', 'failed': 'failed'},
										autonomy={'done': Autonomy.Low, 'failed': Autonomy.Off},
										remapping={'data_IN': 'remaining_travel_dist_OUT', 'data_OUT': 'data_OUT'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
