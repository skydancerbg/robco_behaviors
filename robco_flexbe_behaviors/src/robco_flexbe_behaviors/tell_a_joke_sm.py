#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robco_flexbe_states.pick_robot_joke_state import PickRobotJokeState
from robco_flexbe_states.log_output_from_input_key_state import LogInputKeyMessage
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue Mar 12 2019
@author: Stefan
'''
class TellAJokeSM(Behavior):
	'''
	Tell a random robot joke
	'''


	def __init__(self):
		super(TellAJokeSM, self).__init__()
		self.name = 'Tell A Joke'

		# parameters of this behavior
		self.add_parameter('joke_select', 0)
		self.add_parameter('timer_time', 1)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:883 y:112, x:671 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:146 y:79
			OperatableStateMachine.add('Pick A Joke',
										PickRobotJokeState(),
										transitions={'done': 'Print'},
										autonomy={'done': Autonomy.Low},
										remapping={'robot_joke_OUT': 'robot_joke_OUT'})

			# x:440 y:226
			OperatableStateMachine.add('Print',
										LogInputKeyMessage(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'robot_joke_OUT': 'robot_joke_OUT'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
