#!/usr/bin/env python
from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyActionClient
import roslib; roslib.load_manifest('sound_play')

# from mary_tts.msg import maryttsAction, maryttsGoal
from sound_play.msg import SoundRequest, SoundRequestAction, SoundRequestGoal

"""
#     #################################
#     # SRG Stefan: 
#     # Created by Stefan SRG 15.3.2019, based on:	
#     # https://github.com/FlexBE/flexbe_strands/blob/master/strands_flexbe_states/src/strands_flexbe_states/speech_output_state.py
#     # and https://github.com/ros-drivers/audio_common/blob/master/sound_play/scripts/test_actionlib_client.py
#     #################################
"""

class SpeechOutputEnglishParamTextState(EventState):
		'''
		Lets the robot speak the string, set in Behaviour Parameters 
        variable or inplace in the state GUI.

        -- text_to_speak          string    The text to be spoken. 

		<= done 			Speaking has finished.
		<= failed 			Failed to execute speaking.
		'''
		def __init__(self, text_to_speak="Hello World!"):
			super(SpeechOutputEnglishParamTextState, self).__init__(outcomes=['done', 'failed'])

			self._topic = '/sound_play'
			self._text_to_speak = text_to_speak
			self._client = ProxyActionClient({self._topic: SoundRequestAction})

			self._error = False


		def execute(self, userdata):
			if self._error:
				return 'failed'

			if self._client.has_result(self._topic):
				return 'done'

		def on_enter(self, userdata):
			Logger.loginfo('Speech output, talking')
			goal = SoundRequestGoal()
			goal.sound_request.arg = self._text_to_speak
			goal.sound_request.command = SoundRequest.PLAY_ONCE
			goal.sound_request.sound = SoundRequest.SAY
			goal.sound_request.volume = 1.0 

			self._error = False
			try:
				self._client.send_goal(self._topic, goal)
				# Logger.logwarn('V try')
			except Exception as e:
				Logger.logwarn('Failed to send the Speech command:\n%s' % str(e))
				self._error = True


		def on_exit(self, userdata):
			if not self._client.has_result(self._topic):
				self._client.cancel(self._topic)
				Logger.loginfo('Cancelled active action goal.')


		
