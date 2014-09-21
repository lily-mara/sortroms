from setuptools import setup
setup(
	name='sortroms',
	version='1.0.0',
	description='Python package for sorting emulator ROM files',
	url='http://github.com/natemara/sortroms',
	author='Nate Mara',
	author_email='natemara@gmail.com',
	license='MIT',
	packages=['sortroms'],
	package_dir={'sortroms': 'sortroms'},
	package_data={'sortroms': ['sortroms/*.json']},
	zip_safe=False
)
