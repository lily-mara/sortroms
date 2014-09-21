from os.path import join, dirname, realpath


def get_datafile(filename):
	path = join(dirname(realpath(__file__)), 'data', filename)

	with open(path, 'r') as fileobj:
		return fileobj.read()
