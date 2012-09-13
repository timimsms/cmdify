#!/usr/bin/python
#
# Cmdify
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Imports #
from subprocess import call


#
# Public: Cmdify will take a single argument as input and create a 
# customizable Growl notification via the `growlnotify` 
#
class Cmdify:
	#
	# Public: Should be used to set configurable application constants 
	#
	def __init__(self):
		pass
	
	
	#
	# TODO: Define this for real (just using sample alert for now)
	#
	def parse_args(self, argv):
		result = {}
		result["message"]= "Sample Alert"
	
		return result
	
	def create_arg_string(self, arg_dict):
		# Instantiate the args string 
		args = ""
		
		# Add the message
		args += "--message='"
		args += arg_dict["message"]
		args += "' "
		
		return args
		
	#
	# Public: Simply broadcasts a given message via growlnotify
	#
	def broadcast(self, argv):
		# Build the argument vector
		arguments = self.parse_args(argv)
	
		# Convert to a flat string 
		argument_str = self.create_arg_string(arguments)
	
		# Notify
		self.notify(argument_str)
		
		return True
		
	#
	#
	#
	def notify(self, args):
		# TODO: Throw a custom exception when `growlnotify` can't be found
		call(["growlnotify", args])		

		return True
