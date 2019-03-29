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
from robco_flexbe_states.speak_via_sound_play_no_input_key_state import SpeechOutputEnglishParamTextState
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

		# x:844 y:69, x:334 y:366, x:873 y:630, x:16 y:367, x:128 y:365, x:225 y:367, x:857 y:563
		_sm_move_to_pick_from_small_table_0 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('speak while executing trajectory', 'done'), ('Move to pick_from_small_table', 'reached'), ('timer give time for motion to execute', 'done')]),
										('failed', [('speak while executing trajectory', 'failed')]),
										('failed', [('Move to pick_from_small_table', 'param_error')]),
										('failed', [('Move to pick_from_small_table', 'planning_failed')]),
										('failed', [('Move to pick_from_small_table', 'control_failed')])
										])

		with _sm_move_to_pick_from_small_table_0:
			# x:71 y:40
			OperatableStateMachine.add('Move to pick_from_small_table',
										SrdfStateToMoveit(config_name="pick_from_small_table", move_group="robot", action_topic='/move_group', robot_name=""),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:505 y:216
			OperatableStateMachine.add('speak while executing trajectory',
										SpeechOutputEnglishParamTextState(text_to_speak="Now I am going to move as I am placing something low to the right"),
										transitions={'done': 'finished', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})

			# x:312 y:116
			OperatableStateMachine.add('timer give time for motion to execute',
										WaitState(wait_time=12),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		# x:851 y:66, x:381 y:360, x:857 y:622, x:277 y:369, x:179 y:364, x:17 y:363, x:630 y:365
		_sm_move_back_to_transport_position_1 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('wait', 'done'), ('speak', 'done'), ('move to transport_position', 'reached')]),
										('failed', [('speak', 'failed')]),
										('failed', [('move to transport_position', 'planning_failed')]),
										('failed', [('move to transport_position', 'control_failed')]),
										('failed', [('move to transport_position', 'param_error')])
										])

		with _sm_move_back_to_transport_position_1:
			# x:118 y:45
			OperatableStateMachine.add('move to transport_position',
										SrdfStateToMoveit(config_name="transport_position", move_group="robot", action_topic='/move_group', robot_name=""),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:310 y:128
			OperatableStateMachine.add('wait',
										WaitState(wait_time=15),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:508 y:151
			OperatableStateMachine.add('speak',
										SpeechOutputEnglishParamTextState(text_to_speak="Going back to transport position"),
										transitions={'done': 'finished', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})


		# x:614 y:41, x:130 y:365, x:781 y:468, x:330 y:365, x:430 y:365, x:530 y:365, x:630 y:365
		_sm_move_to_place_on_tall_table_2 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('Move to place_on_tall_table', 'reached'), ('wait', 'done'), ('speak', 'done')]),
										('failed', [('Move to place_on_tall_table', 'planning_failed')]),
										('failed', [('Move to place_on_tall_table', 'control_failed')]),
										('failed', [('Move to place_on_tall_table', 'param_error')]),
										('failed', [('speak', 'failed')])
										])

		with _sm_move_to_place_on_tall_table_2:
			# x:30 y:40
			OperatableStateMachine.add('Move to place_on_tall_table',
										SrdfStateToMoveit(config_name="place_on_tall_table", move_group="robot", action_topic='/move_group', robot_name=""),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:380 y:129
			OperatableStateMachine.add('speak',
										SpeechOutputEnglishParamTextState(text_to_speak="Now I will move to the left as I am going to place something on the table on the left"),
										transitions={'done': 'finished', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})

			# x:277 y:66
			OperatableStateMachine.add('wait',
										WaitState(wait_time=14),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		# x:296 y:148, x:130 y:365, x:230 y:365, x:330 y:365, x:430 y:365, x:530 y:365, x:630 y:365
		_sm_move_to_reach_up_position_3 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('Move to reach_up position', 'reached'), ('wait', 'done'), ('speak', 'done')]),
										('failed', [('Move to reach_up position', 'planning_failed')]),
										('failed', [('Move to reach_up position', 'control_failed')]),
										('failed', [('Move to reach_up position', 'param_error')]),
										('failed', [('speak', 'failed')])
										])

		with _sm_move_to_reach_up_position_3:
			# x:30 y:40
			OperatableStateMachine.add('Move to reach_up position',
										SrdfStateToMoveit(config_name="reach_up", move_group="robot", action_topic='/move_group', robot_name=""),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:246 y:38
			OperatableStateMachine.add('wait',
										WaitState(wait_time=16.3),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:391 y:50
			OperatableStateMachine.add('speak',
										SpeechOutputEnglishParamTextState(text_to_speak="Sega shte pridija ramoto nagore i napred"),
										transitions={'done': 'finished', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})


		# x:825 y:119, x:130 y:365, x:230 y:365, x:330 y:365, x:430 y:365, x:530 y:365, x:630 y:365
		_sm_move_to_transport_position_4 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('say intro', 'done'), ('wait', 'done'), ('Move to transport_position', 'reached')]),
										('failed', [('Move to transport_position', 'param_error')]),
										('failed', [('Move to transport_position', 'control_failed')]),
										('failed', [('Move to transport_position', 'planning_failed')]),
										('failed', [('say intro', 'failed')])
										])

		with _sm_move_to_transport_position_4:
			# x:37 y:92
			OperatableStateMachine.add('Move to transport_position',
										SrdfStateToMoveit(config_name="transport_position", move_group="robot", action_topic='/move_group', robot_name=""),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:294 y:38
			OperatableStateMachine.add('wait',
										WaitState(wait_time=17),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:603 y:196
			OperatableStateMachine.add('say intro',
										SpeechOutputEnglishParamTextState(text_to_speak="While moving in circle, I will make a shor demo moving my arm simultaneously."),
										transitions={'done': 'finished', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})



		with _state_machine:
			# x:148 y:20
			OperatableStateMachine.add('Move to transport position',
										_sm_move_to_transport_position_4,
										transitions={'finished': 'Move to reach_up position', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:229 y:107
			OperatableStateMachine.add('Move to reach_up position',
										_sm_move_to_reach_up_position_3,
										transitions={'finished': 'Move to place_on_tall_table', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:273 y:188
			OperatableStateMachine.add('Move to place_on_tall_table',
										_sm_move_to_place_on_tall_table_2,
										transitions={'finished': 'Move to pick_from_small_table', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:651 y:612
			OperatableStateMachine.add('Move back to transport_position',
										_sm_move_back_to_transport_position_1,
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:637 y:272
			OperatableStateMachine.add('Move to pick_from_small_table',
										_sm_move_to_pick_from_small_table_0,
										transitions={'finished': 'Move back to transport_position', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
