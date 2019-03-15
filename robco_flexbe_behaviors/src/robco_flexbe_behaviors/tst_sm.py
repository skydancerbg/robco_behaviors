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
from robco_flexbe_states.speech_trough_sound_play_state import SpeechOutputViaSoundPlayState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue Mar 12 2019
@author: st
'''
class tstSM(Behavior):
	'''
	tst
	'''


	def __init__(self):
		super(tstSM, self).__init__()
		self.name = 'tst'

		# parameters of this behavior
		self.add_parameter('jk', 0)
		self.add_parameter('tmr', 3)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:136 y:451
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:562 y:117
			OperatableStateMachine.add('pk',
										PickRobotJokeState(),
										transitions={'done': 'spk'},
										autonomy={'done': Autonomy.Off},
										remapping={'robot_joke_OUT': 'robot_joke_OUT'})

			# x:713 y:229
			OperatableStateMachine.add('spk',
										SpeechOutputViaSoundPlayState(),
										transitions={'done': 'finished', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'text_IN': 'robot_joke_OUT'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
