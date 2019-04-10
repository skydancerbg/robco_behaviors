#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robco_flexbe_states.get_robco_command_sm import GetRobcoCommand
from robco_flexbe_behaviors.tell_a_joke_bulgarian_sm import TellajokeBulgarianSM
from flexbe_states.decision_state import DecisionState
from flexbe_states.log_key_state import LogKeyState
from robco_flexbe_behaviors.drive_in_squre_stop_if_obstacle_sm import Drive_In_Squre_Stop_If_ObstacleSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue Apr 09 2019
@author: Stefan
'''
class Robco19eFullDemo2019SM(Behavior):
	'''
	Robco19e Full Demo 2019
	'''


	def __init__(self):
		super(Robco19eFullDemo2019SM, self).__init__()
		self.name = 'Robco19e Full Demo 2019'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(TellajokeBulgarianSM, 'Tell a joke Bulgarian')
		self.add_behavior(Drive_In_Squre_Stop_If_ObstacleSM, 'Drive in square and move arm demo/Drive_In_Squre_Stop_If_Obstacle')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:332 y:411, x:368 y:23
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:30 y:365, x:130 y:365, x:230 y:365, x:330 y:365
		_sm_drive_in_square_and_move_arm_demo_0 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('Drive_In_Squre_Stop_If_Obstacle', 'finished')]),
										('failed', [('Drive_In_Squre_Stop_If_Obstacle', 'failed')])
										])

		with _sm_drive_in_square_and_move_arm_demo_0:
			# x:64 y:131
			OperatableStateMachine.add('Drive_In_Squre_Stop_If_Obstacle',
										self.use_behavior(Drive_In_Squre_Stop_If_ObstacleSM, 'Drive in square and move arm demo/Drive_In_Squre_Stop_If_Obstacle'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})



		with _state_machine:
			# x:72 y:47
			OperatableStateMachine.add('get new command',
										GetRobcoCommand(),
										transitions={'failed': 'failed', 'done': 'log key'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Off},
										remapping={'robco_command_OUT': 'robco_command_OUT'})

			# x:579 y:56
			OperatableStateMachine.add('Tell a joke Bulgarian',
										self.use_behavior(TellajokeBulgarianSM, 'Tell a joke Bulgarian'),
										transitions={'finished': 'get new command', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:227 y:122
			OperatableStateMachine.add('which demo?',
										DecisionState(outcomes=['joke','demo', 'exit'], conditions=lambda x: 'joke' if x == 'tell_a_joke' else ('demo' if x == 'full_demo' else 'exit')),
										transitions={'joke': 'Tell a joke Bulgarian', 'demo': 'Drive in square and move arm demo', 'exit': 'finished'},
										autonomy={'joke': Autonomy.Low, 'demo': Autonomy.Low, 'exit': Autonomy.Off},
										remapping={'input_value': 'robco_command_OUT'})

			# x:129 y:242
			OperatableStateMachine.add('log key',
										LogKeyState(text='robco_command_OUT value: {}', severity=Logger.REPORT_INFO),
										transitions={'done': 'which demo?'},
										autonomy={'done': Autonomy.Off},
										remapping={'data': 'robco_command_OUT'})

			# x:548 y:180
			OperatableStateMachine.add('Drive in square and move arm demo',
										_sm_drive_in_square_and_move_arm_demo_0,
										transitions={'finished': 'get new command', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
