#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robco_flexbe_states.moveit_commander_move_arm_to_named_position_state import MoveitCommanderMoveGroupNamedPositiomState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Mar 13 2019
@author: Stefan
'''
class testMoveItNamedSM(Behavior):
	'''
	testMoveItNamed
	'''


	def __init__(self):
		super(testMoveItNamedSM, self).__init__()
		self.name = 'testMoveItNamed'

		# parameters of this behavior
		self.add_parameter('named_position_name', 'reach_up')
		self.add_parameter('planning_group_name', 'robot')

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
			# x:213 y:84
			OperatableStateMachine.add('Move To reach_up Position',
										MoveitCommanderMoveGroupNamedPositiomState(planning_group=self.planning_group_name, named_position=self.named_position_name),
										transitions={'reached': 'finished', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
