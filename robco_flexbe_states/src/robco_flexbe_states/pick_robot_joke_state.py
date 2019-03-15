#!/usr/bin/env python
import rospy
import random

from flexbe_core import EventState, Logger

    #################################
    # SRG Stefan: Modified by SRG 11.3.2019
    # From: https://github.com/FlexBE/flexbe_strands/blob/master/strands_flexbe_states/src/strands_flexbe_states/pick_joke_state.py
    #################################

class PickRobotJokeState(EventState):
	'''
	Select a joke or pick a random one.
	#> robot_joke_OUT 		string 	Provides the selected joke.
	<= done 			Joke has been selected.
	'''

	RANDOM = 0

	def __init__(self):
		super(PickRobotJokeState, self).__init__(outcomes = ['done'],
											output_keys = ['robot_joke_OUT'])

		
		self._robot_joke_OUT = None
		self._joke_selection = 0
		self._jokes = [	'How many robots does it take to screw in a light bulb? Three - one to hold the bulb, and two to turn the ladder!',
'What is a robots favorite type of music? Heavy metal!',
'What do you get when you cross a robot and a tractor? A trans-farmer!',
'Why did the robot get angry so often? People kept pushing its buttons.',
'Why did the robot go to the doctor? Because it had a virus! ',
'What happens when a robot falls in muddy water? It gets wet and muddy.',
'A robot walks into a bar, orders a drink, and lays down some cash. Bartender says: Hey, we dont serve robots. And the robot says: Oh, but someday you will.',
'Why are robots shy? Because they have hardware and software but no underware.'
]



	def execute(self, userdata):
		userdata.robot_joke_OUT = self._jokes[self._joke_selection - 1]
		# Logger.loginfo('The joke selected is:  \n%s' % userdata.robot_joke_OUT)
		# Logger.logwarn('Failed to send the speech command:\n%s' % str(userdata.robot_joke_OUT))
		Logger.logwarn('PickRobotJokeState on_execute')
		return 'done'
		

	def on_enter(self, userdata):
		if self._joke_selection == 0:
			self._joke_selection = random.randint(1, len(self._jokes))
			Logger.logwarn('PickRobotJokeState on_enter')
		