from sortroms import main
import argparse

parser = argparse.ArgumentParser(
	description='Sort emulator ROM files',
	prog='sortroms'
)

parser.add_argument(
	'folders',
	metavar='DIR',
	type=str,
	nargs='*',
	help='The ROM folders to sort (absolute)'
)

if __name__ == '__main__':
	args = parser.parse_args()
	main(args)
