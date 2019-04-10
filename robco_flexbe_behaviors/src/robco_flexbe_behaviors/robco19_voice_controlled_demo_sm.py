#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robco_flexbe_behaviors.tell_a_joke_bulgarian_sm import TellajokeBulgarianSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Apr 08 2019
@author: Stefan
'''
class Robco19VoiceControlledDemoSM(Behavior):
	'''
	Robco19 Voice Controlled Demo
	'''


	def __init__(self):
		super(Robco19VoiceControlledDemoSM, self).__init__()
		self.name = 'Robco19 Voice Controlled Demo'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(TellajokeBulgarianSM, 'Tell a joke Bulgarian')

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
			# x:185 y:142
			OperatableStateMachine.add('Tell a joke Bulgarian',
										self.use_behavior(TellajokeBulgarianSM, 'Tell a joke Bulgarian'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
