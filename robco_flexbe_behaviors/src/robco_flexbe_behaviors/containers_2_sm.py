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
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Jul 30 2018
@author: Ephson
'''
class Containers2SM(Behavior):
	'''
	Using priority and concurrency containers. A demonstration.
	'''


	def __init__(self):
		super(Containers2SM, self).__init__()
		self.name = 'Containers 2'

		# parameters of this behavior
		self.add_parameter('wait_time_A', 5)
		self.add_parameter('wait_time_B', 2)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:319, x:130 y:319
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:561 y:203, x:130 y:310
		_sm_priority_container_0 = PriorityContainer(outcomes=['finished', 'failed'])

		with _sm_priority_container_0:
			# x:154 y:92
			OperatableStateMachine.add('DelayB',
										WaitState(wait_time=self.wait_time_B),
										transitions={'done': 'Logger'},
										autonomy={'done': Autonomy.Off})

			# x:303 y:124
			OperatableStateMachine.add('Logger',
										LogState(text="MESSAGE FROM THE LOGGER", severity=Logger.REPORT_INFO),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		# x:405 y:253, x:500 y:316, x:275 y:331, x:330 y:310, x:430 y:310, x:549 y:310
		_sm_concurrency_container_1 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('Priority Container', 'finished')]),
										('failed', [('Priority Container', 'failed')]),
										('finished', [('DelayA', 'done')])
										])

		with _sm_concurrency_container_1:
			# x:167 y:96
			OperatableStateMachine.add('DelayA',
										WaitState(wait_time=self.wait_time_A),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:520 y:124
			OperatableStateMachine.add('Priority Container',
										_sm_priority_container_0,
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})



		with _state_machine:
			# x:213 y:148
			OperatableStateMachine.add('Concurrency Container',
										_sm_concurrency_container_1,
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
