from sortroms import main
import argparse

parser = argparse.ArgumentParser(
	description='Sort emulator ROM files',
	prog='sortroms'
)

parser.add_argument(
	'folder',
	metavar='DIR',
	type=str,
	nargs='?',
	help='The ROM folder to sort.'
)

if __name__ == '__main__':
	args = parser.parse_args()
	main(args)
