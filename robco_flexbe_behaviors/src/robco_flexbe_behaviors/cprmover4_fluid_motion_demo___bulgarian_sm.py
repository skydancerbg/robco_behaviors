#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robco_flexbe_behaviors.move_group_test_sm import move_grouptestSM
from robco_flexbe_behaviors.cprmover4_arm_demo___tts_sound_play_sm import CPRmover4armDEMOTTSsound_playSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Mar 15 2019
@author: Stefan
'''
class CPRmover4fluidmotionDEMOBulgarianSM(Behavior):
	'''
	CPRmover4 arm demo with english speech, trough sound_play.
Do not forget to 
rosrun sound_play soundplay_node.py
before starting the DEMO
	'''


	def __init__(self):
		super(CPRmover4fluidmotionDEMOBulgarianSM, self).__init__()
		self.name = 'CPRmover4 fluid motion DEMO - Bulgarian'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(move_grouptestSM, 'Container/move_group test')
		self.add_behavior(CPRmover4armDEMOTTSsound_playSM, 'Container/CPRmover4 arm DEMO - TTS sound_play')

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

		# x:761 y:285, x:882 y:290, x:230 y:365, x:330 y:365, x:430 y:365
		_sm_container_0 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('finished', [('move_group test', 'finished'), ('CPRmover4 arm DEMO - TTS sound_play', 'finished')]),
										('failed', [('move_group test', 'failed')]),
										('failed', [('CPRmover4 arm DEMO - TTS sound_play', 'failed')])
										])

		with _sm_container_0:
			# x:30 y:40
			OperatableStateMachine.add('move_group test',
										self.use_behavior(move_grouptestSM, 'Container/move_group test'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:289 y:38
			OperatableStateMachine.add('CPRmover4 arm DEMO - TTS sound_play',
										self.use_behavior(CPRmover4armDEMOTTSsound_playSM, 'Container/CPRmover4 arm DEMO - TTS sound_play'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})



		with _state_machine:
			# x:437 y:88
			OperatableStateMachine.add('Container',
										_sm_container_0,
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
