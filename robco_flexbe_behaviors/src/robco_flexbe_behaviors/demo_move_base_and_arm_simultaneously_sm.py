#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robco_flexbe_states.tts_bg_sm import TTSBulgarian
from flexbe_states.wait_state import WaitState
from robco_flexbe_behaviors.drive_in_squre_stop_if_obstacle_sm import Drive_In_Squre_Stop_If_ObstacleSM
from flexbe_manipulation_states.srdf_state_to_moveit import SrdfStateToMoveit
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Apr 10 2019
@author: Stefan
'''
class DemomovebaseandarmsimultaneouslySM(Behavior):
	'''
	Demo move base and arm simultaneously
	'''


	def __init__(self):
		super(DemomovebaseandarmsimultaneouslySM, self).__init__()
		self.name = 'Demo move base and arm simultaneously'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(Drive_In_Squre_Stop_If_ObstacleSM, 'Move base and arm while speaking/Drive_In_Squre_Stop_If_Obstacle')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:744 y:92, x:65 y:535
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:220 y:611, x:575 y:295
		_sm_move_arm_up_and_down_0 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_move_arm_up_and_down_0:
			# x:387 y:20
			OperatableStateMachine.add('say while moving the arm',
										TTSBulgarian(ttsbg_text='Сега ще движа ръката си нагоре и надолу, докато се движа в квадрат.'),
										transitions={'failed': 'failed', 'done': 'move to transport pos'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Off})

			# x:624 y:41
			OperatableStateMachine.add('move to transport pos',
										SrdfStateToMoveit(config_name='transport_position', move_group="robot", action_topic='/move_group', robot_name=""),
										transitions={'reached': 'ton reach up', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:748 y:213
			OperatableStateMachine.add('ton reach up',
										SrdfStateToMoveit(config_name='reach_up', move_group="robot", action_topic='/move_group', robot_name=""),
										transitions={'reached': 'back to trnsport pos', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:104 y:150
			OperatableStateMachine.add('back to trnsport pos',
										SrdfStateToMoveit(config_name='transport_positiion', move_group="robot", action_topic='/move_group', robot_name=""),
										transitions={'reached': 'to reach up again', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:112 y:287
			OperatableStateMachine.add('to reach up again',
										SrdfStateToMoveit(config_name='reach_up', move_group="robot", action_topic='/move_group', robot_name=""),
										transitions={'reached': 'finally back to transport pos', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:139 y:423
			OperatableStateMachine.add('finally back to transport pos',
										SrdfStateToMoveit(config_name='transport_position', move_group="robot", action_topic='/move_group', robot_name=""),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})


		# x:30 y:365, x:130 y:365, x:230 y:365, x:330 y:365, x:430 y:365
		_sm_move_base_and_arm_while_speaking_1 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('Drive_In_Squre_Stop_If_Obstacle', 'finished'), ('move arm up and down', 'finished')]),
										('failed', [('Drive_In_Squre_Stop_If_Obstacle', 'failed')]),
										('failed', [('move arm up and down', 'failed')])
										])

		with _sm_move_base_and_arm_while_speaking_1:
			# x:54 y:87
			OperatableStateMachine.add('Drive_In_Squre_Stop_If_Obstacle',
										self.use_behavior(Drive_In_Squre_Stop_If_ObstacleSM, 'Move base and arm while speaking/Drive_In_Squre_Stop_If_Obstacle'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:390 y:87
			OperatableStateMachine.add('move arm up and down',
										_sm_move_arm_up_and_down_0,
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		# x:586 y:62, x:23 y:199, x:230 y:365, x:330 y:365
		_sm_say_intro_2 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('Say intro', 'done'), ('give it time tos peak', 'done')]),
										('failed', [('Say intro', 'failed')])
										])

		with _sm_say_intro_2:
			# x:28 y:61
			OperatableStateMachine.add('Say intro',
										TTSBulgarian(ttsbg_text='Нека Ви се представя, аз съм Телеуправляемия Сервизен Робот Робко 19. За мен е чест да участвам в ГОДИШНАТА МЕЖДУНАРОДНА НАУЧНА КОНФЕРЕНЦИЯ НА АВИАЦИОННИЯ ФАКУЛТЕТ. Създаден съм от групата по сервизна роботика по проект, Финансиран от Фонда Научни изследвания. Сега ще направя кратка демонстрация на част от моите възможности.'),
										transitions={'failed': 'failed', 'done': 'finished'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Off})

			# x:108 y:302
			OperatableStateMachine.add('give it time tos peak',
										WaitState(wait_time=15),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})



		with _state_machine:
			# x:108 y:54
			OperatableStateMachine.add('Say intro',
										_sm_say_intro_2,
										transitions={'finished': 'Move base and arm while speaking', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:332 y:184
			OperatableStateMachine.add('Move base and arm while speaking',
										_sm_move_base_and_arm_while_speaking_1,
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
