#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robco_flexbe_states.foo_state import FooState
from robco_flexbe_states.bar_state import BarState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue Mar 12 2019
@author: Stefan
'''
class TestFooSM(Behavior):
	'''
	Test Foo
	'''


	def __init__(self):
		super(TestFooSM, self).__init__()
		self.name = 'Test Foo'

		# parameters of this behavior
		self.add_parameter('target_time', 3)
		self.add_parameter('time2', 3)

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
			# x:216 y:62
			OperatableStateMachine.add('ff',
										FooState(target_time=self.target_time),
										transitions={'continue': 'bb', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'text_same_name': 'text_same_name'})

			# x:405 y:85
			OperatableStateMachine.add('bb',
										BarState(target_time=self.time2),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'text_same_name': 'text_same_name'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
