#!/usr/bin/python
#
# Cmdify
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Imports #
import sys
from cmdify import Cmdify

#
# Public: Simply passes the command argument vector to the cmdify function
#
def main(argv=None):
    if argv is None:
        argv = sys.argv

	commander = Cmdify()
	commander.broadcast(argv)
	

#
# Public: Simply calls to the `main` function using the sys.exit wrapper
#
if __name__ == "__main__":
	sys.exit( main() )