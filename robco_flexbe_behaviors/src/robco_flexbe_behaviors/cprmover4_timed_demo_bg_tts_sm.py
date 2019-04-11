#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_manipulation_states.srdf_state_to_moveit import SrdfStateToMoveit
from flexbe_states.wait_state import WaitState
from robco_flexbe_states.tts_bg_sm import TTSBulgarian
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Mar 28 2019
@author: Stefan
'''
class CPRmover4_timed_demo_BG_ttsSM(Behavior):
	'''
	Mover4 arm demo with timed movements and Bulgarian language narration
	'''


	def __init__(self):
		super(CPRmover4_timed_demo_BG_ttsSM, self).__init__()
		self.name = 'CPRmover4_timed_demo_BG_tts'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1190 y:670, x:11 y:681
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:30 y:365, x:130 y:365, x:230 y:365, x:330 y:365
		_sm_vstapitelno_slovo_0 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('govori', 'done'), ('give time to speak', 'done')]),
										('failed', [('govori', 'failed')])
										])

		with _sm_vstapitelno_slovo_0:
			# x:86 y:149
			OperatableStateMachine.add('govori',
										TTSBulgarian(ttsbg_text='Нека Ви се представя, аз съм Телеуправляемия Сервизен Робот Робко 19. За мен е чест да участвам в ГОДИШНАТА МЕЖДУНАРОДНА НАУЧНА КОНФЕРЕНЦИЯ НА АВИАЦИОННИЯ ФАКУЛТЕТ. Създаден съм от групата по сервизна роботика по проект, Финансиран от Фонда Научни изследвания. Сега ще направя кратка демонстрация на част от моите възможности.'),
										transitions={'failed': 'failed', 'done': 'finished'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Off})

			# x:282 y:111
			OperatableStateMachine.add('give time to speak',
										WaitState(wait_time=20),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		# x:844 y:69, x:586 y:560, x:242 y:373, x:16 y:367, x:156 y:366, x:578 y:490, x:857 y:563
		_sm_move_to_pick_from_small_table_1 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('Move to pick_from_small_table', 'reached'), ('Timer give time for motion to execute', 'done'), ('say text', 'done')]),
										('failed', [('Move to pick_from_small_table', 'param_error')]),
										('failed', [('Move to pick_from_small_table', 'planning_failed')]),
										('failed', [('Move to pick_from_small_table', 'control_failed')]),
										('failed', [('say text', 'failed')])
										])

		with _sm_move_to_pick_from_small_table_1:
			# x:71 y:40
			OperatableStateMachine.add('Move to pick_from_small_table',
										SrdfStateToMoveit(config_name="pick_from_small_table", move_group="robot", action_topic='/move_group', robot_name=""),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:312 y:116
			OperatableStateMachine.add('Timer give time for motion to execute',
										WaitState(wait_time=12),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:538 y:206
			OperatableStateMachine.add('say text',
										TTSBulgarian(ttsbg_text="Придвижвам ръката надолу и в дясно"),
										transitions={'failed': 'failed', 'done': 'finished'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Off})


		# x:851 y:66, x:441 y:472, x:63 y:338, x:277 y:369, x:179 y:364, x:374 y:469, x:630 y:365
		_sm_move_back_to_transport_position_2 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('Timer give time for motion to execute', 'done'), ('move to transport_position', 'reached'), ('say text', 'done')]),
										('failed', [('move to transport_position', 'planning_failed')]),
										('failed', [('move to transport_position', 'control_failed')]),
										('failed', [('move to transport_position', 'param_error')]),
										('failed', [('say text', 'failed')])
										])

		with _sm_move_back_to_transport_position_2:
			# x:118 y:45
			OperatableStateMachine.add('move to transport_position',
										SrdfStateToMoveit(config_name="transport_position", move_group="robot", action_topic='/move_group', robot_name=""),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:310 y:128
			OperatableStateMachine.add('Timer give time for motion to execute',
										WaitState(wait_time=15),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:525 y:170
			OperatableStateMachine.add('say text',
										TTSBulgarian(ttsbg_text="Връщам ръката в изходн позиция."),
										transitions={'failed': 'failed', 'done': 'finished'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Off})


		# x:614 y:41, x:129 y:345, x:179 y:346, x:347 y:338, x:430 y:365, x:530 y:365, x:630 y:365
		_sm_move_to_place_on_tall_table_3 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('Move to place_on_tall_table', 'reached'), ('Timer give time for motion to execute', 'done'), ('say text', 'done')]),
										('failed', [('Move to place_on_tall_table', 'planning_failed')]),
										('failed', [('Move to place_on_tall_table', 'control_failed')]),
										('failed', [('Move to place_on_tall_table', 'param_error')]),
										('failed', [('say text', 'failed')])
										])

		with _sm_move_to_place_on_tall_table_3:
			# x:30 y:40
			OperatableStateMachine.add('Move to place_on_tall_table',
										SrdfStateToMoveit(config_name="place_on_tall_table", move_group="robot", action_topic='/move_group', robot_name=""),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:277 y:66
			OperatableStateMachine.add('Timer give time for motion to execute',
										WaitState(wait_time=14),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:410 y:128
			OperatableStateMachine.add('say text',
										TTSBulgarian(ttsbg_text="Сега ще придвижа ръката наляво"),
										transitions={'failed': 'failed', 'done': 'finished'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Off})


		# x:296 y:148, x:130 y:365, x:230 y:365, x:330 y:365, x:430 y:365, x:530 y:365, x:630 y:365
		_sm_move_to_reach_up_position_4 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('Move to reach_up position', 'reached'), ('Timer give time for motion to execute', 'done'), ('say text', 'done')]),
										('failed', [('Move to reach_up position', 'planning_failed')]),
										('failed', [('Move to reach_up position', 'control_failed')]),
										('failed', [('Move to reach_up position', 'param_error')]),
										('failed', [('say text', 'failed')])
										])

		with _sm_move_to_reach_up_position_4:
			# x:30 y:40
			OperatableStateMachine.add('Move to reach_up position',
										SrdfStateToMoveit(config_name="reach_up", move_group="robot", action_topic='/move_group', robot_name=""),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:246 y:38
			OperatableStateMachine.add('Timer give time for motion to execute',
										WaitState(wait_time=16.3),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:562 y:44
			OperatableStateMachine.add('say text',
										TTSBulgarian(ttsbg_text="Сега ще придвижа ръката нагоре и напред"),
										transitions={'failed': 'failed', 'done': 'finished'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Off})


		# x:825 y:119, x:130 y:365, x:230 y:365, x:330 y:365, x:430 y:365, x:615 y:337, x:630 y:378
		_sm_move_to_transport_position_5 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('Timer give time for motion to execute', 'done'), ('Move to transport_position', 'reached'), ('Say text in Bulgarian', 'done')]),
										('failed', [('Move to transport_position', 'param_error')]),
										('failed', [('Move to transport_position', 'control_failed')]),
										('failed', [('Move to transport_position', 'planning_failed')]),
										('failed', [('Say text in Bulgarian', 'failed')])
										])

		with _sm_move_to_transport_position_5:
			# x:37 y:92
			OperatableStateMachine.add('Move to transport_position',
										SrdfStateToMoveit(config_name="transport_position", move_group="robot", action_topic='/move_group', robot_name=""),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:294 y:38
			OperatableStateMachine.add('Timer give time for motion to execute',
										WaitState(wait_time=10),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:387 y:156
			OperatableStateMachine.add('Say text in Bulgarian',
										TTSBulgarian(ttsbg_text="Сега ще Ви демонстрирам някои движения на ръката си."),
										transitions={'failed': 'failed', 'done': 'finished'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Off})



		with _state_machine:
			# x:32 y:34
			OperatableStateMachine.add('Vstapitelno slovo',
										_sm_vstapitelno_slovo_0,
										transitions={'finished': 'Move to transport position', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:248 y:156
			OperatableStateMachine.add('Move to reach_up position',
										_sm_move_to_reach_up_position_4,
										transitions={'finished': 'Move to place_on_tall_table', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:263 y:253
			OperatableStateMachine.add('Move to place_on_tall_table',
										_sm_move_to_place_on_tall_table_3,
										transitions={'finished': 'Move to pick_from_small_table', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:651 y:612
			OperatableStateMachine.add('Move back to transport_position',
										_sm_move_back_to_transport_position_2,
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:637 y:272
			OperatableStateMachine.add('Move to pick_from_small_table',
										_sm_move_to_pick_from_small_table_1,
										transitions={'finished': 'Move back to transport_position', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:252 y:63
			OperatableStateMachine.add('Move to transport position',
										_sm_move_to_transport_position_5,
										transitions={'finished': 'Move to reach_up position', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
