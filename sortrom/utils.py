from os.path import join, dirname, realpath


def get_data_file(file_name):
	return join(dirname(realpath(__file__)), file_name)
