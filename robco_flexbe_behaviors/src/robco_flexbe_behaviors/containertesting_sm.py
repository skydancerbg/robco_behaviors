#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_states.wait_state import WaitState
from flexbe_states.publisher_string_state import PublisherStringState
from flexbe_states.calculation_state import CalculationState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Jul 30 2018
@author: Ephson
'''
class ContainerTestingSM(Behavior):
	'''
	something description
	'''


	def __init__(self):
		super(ContainerTestingSM, self).__init__()
		self.name = 'ContainerTesting'

		# parameters of this behavior
		self.add_parameter('val', 0.5)
		self.add_parameter('pub_topic', 'results')
		self.add_parameter('wait_time', 3)
		self.add_parameter('msg', 'Custom message')

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:681 y:207, x:479 y:269
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.input_value = self.val
		_state_machine.userdata.value = self.msg

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:93 y:108
			OperatableStateMachine.add('Delay',
										WaitState(wait_time=self.wait_time),
										transitions={'done': 'Find X'},
										autonomy={'done': Autonomy.Off})

			# x:420 y:122
			OperatableStateMachine.add('Publisher',
										PublisherStringState(topic="/results"),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'output_value'})

			# x:232 y:190
			OperatableStateMachine.add('Find X',
										CalculationState(calculation=lambda x: str(x**2)),
										transitions={'done': 'Publisher'},
										autonomy={'done': Autonomy.Off},
										remapping={'input_value': 'input_value', 'output_value': 'output_value'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
