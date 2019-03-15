#!/usr/bin/env python

from flexbe_core import EventState, Logger

'''
Created on 09.12.2013

@author: Philipp Schillinger
'''

class LogInputKeyMessage(EventState):
	'''
	A state that can log a predefined message to precisely inform the operator about what happened to the behavior.
	
	># text_IN 	string 	Text to output.

	<= done				Indicates that the message has been logged.
	
	'''
	
	def __init__(self):
		'''Constructor'''
		super(LogInputKeyMessage, self).__init__(outcomes = ['done'], input_keys = ['robot_joke_OUT'])

		
	def execute(self, userdata):
		'''Execute this state'''
		
		# Already logged. No need to wait for anything.
		return 'done'

	
	def on_enter(self, userdata):
		'''Log upon entering the state.'''

		Logger.log("userdata.text_IN", Logger.REPORT_HINT)
