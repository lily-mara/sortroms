from __future__ import division, print_function, absolute_import
import argparse

from .organizer import main

def command_line_entrypoint():
	parser = argparse.ArgumentParser(
		description='Sort emulator ROM files',
		prog='sortroms'
	)

	parser.add_argument(
		'folders',
		metavar='DIR',
		nargs='*',
		help='The ROM folders to sort (absolute)'
	)

	args = parser.parse_args()
	main(args)
