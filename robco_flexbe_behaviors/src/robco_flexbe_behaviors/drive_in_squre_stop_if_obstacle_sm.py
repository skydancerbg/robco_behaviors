#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robco_flexbe_states.go_forward_fixed_distance_obst_avoid_state import GoFowardFixedDistanceState
from robco_flexbe_states.turn_state import TurnState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sat Mar 23 2019
@author: Stefan
'''
class Drive_In_Squre_Stop_If_ObstacleSM(Behavior):
	'''
	Drives the robot ina square with side lenght based on imput value, by using cmd_vel and fused odometry. I case of obstacle infornt at the set (input) distace fails.
	'''


	def __init__(self):
		super(Drive_In_Squre_Stop_If_ObstacleSM, self).__init__()
		self.name = 'Drive_In_Squre_Stop_If_Obstacle'

		# parameters of this behavior
		self.add_parameter('angle_degrees', 90)
		self.add_parameter('speed_forward', 0.3)
		self.add_parameter('speed_turning', 0.2)
		self.add_parameter('distance_to_obstacle_stop', 0.3)
		self.add_parameter('distance_forward_metes', 0.5)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:356 y:697, x:13 y:202
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:302 y:2
			OperatableStateMachine.add('Go Forward First Leg',
										GoFowardFixedDistanceState(speed=self.speed_forward, travel_dist=self.distance_forward_metes, obstacle_dist=self.distance_to_obstacle_stop),
										transitions={'failed': 'failed', 'done': 'Turn 90 degrees'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Low})

			# x:300 y:158
			OperatableStateMachine.add('Go Forward Secong Leg',
										GoFowardFixedDistanceState(speed=self.speed_forward, travel_dist=self.distance_forward_metes, obstacle_dist=self.distance_to_obstacle_stop),
										transitions={'failed': 'failed', 'done': 'Turn 180 degrees'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Low})

			# x:326 y:251
			OperatableStateMachine.add('Turn 180 degrees',
										TurnState(angle=self.angle_degrees, speed=self.speed_turning),
										transitions={'failed': 'failed', 'done': 'Go Forward Third Leg'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Low})

			# x:301 y:338
			OperatableStateMachine.add('Go Forward Third Leg',
										GoFowardFixedDistanceState(speed=self.speed_forward, travel_dist=self.distance_forward_metes, obstacle_dist=self.distance_to_obstacle_stop),
										transitions={'failed': 'failed', 'done': 'Turn to 270 degrees'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Low})

			# x:327 y:429
			OperatableStateMachine.add('Turn to 270 degrees',
										TurnState(angle=self.angle_degrees, speed=self.speed_turning),
										transitions={'failed': 'failed', 'done': 'Go Forward Final Leg'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Low})

			# x:306 y:520
			OperatableStateMachine.add('Go Forward Final Leg',
										GoFowardFixedDistanceState(speed=self.speed_forward, travel_dist=self.distance_forward_metes, obstacle_dist=self.distance_to_obstacle_stop),
										transitions={'failed': 'failed', 'done': 'Turn to 360 degrees'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Low})

			# x:324 y:610
			OperatableStateMachine.add('Turn to 360 degrees',
										TurnState(angle=self.angle_degrees, speed=self.speed_turning),
										transitions={'failed': 'failed', 'done': 'finished'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Low})

			# x:325 y:79
			OperatableStateMachine.add('Turn 90 degrees',
										TurnState(angle=self.angle_degrees, speed=self.speed_turning),
										transitions={'failed': 'failed', 'done': 'Go Forward Secong Leg'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Low})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
