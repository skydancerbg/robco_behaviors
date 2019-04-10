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
from robco_flexbe_states.tts_bg_from_incomming_key_state import TTSBulgarianFromIncommingKey
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun Apr 07 2019
@author: Stefan
'''
class TellajokeBulgarianSM(Behavior):
	'''
	Tell a joke in Bulgarian
	'''


	def __init__(self):
		super(TellajokeBulgarianSM, self).__init__()
		self.name = 'Tell a joke Bulgarian'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:161 y:85
			OperatableStateMachine.add('Pick a joke',
										PickRobotJokeState(),
										transitions={'done': 'say joke'},
										autonomy={'done': Autonomy.Off},
										remapping={'robot_joke_OUT': 'robot_joke_OUT'})

			# x:411 y:131
			OperatableStateMachine.add('say joke',
										TTSBulgarianFromIncommingKey(),
										transitions={'failed': 'failed', 'done': 'finished'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Off},
										remapping={'ttsbg_text': 'robot_joke_OUT'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
