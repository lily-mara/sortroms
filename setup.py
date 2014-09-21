from setuptools import setup
setup(
	name='sortroms',
	version='0.0.4',
	description='Python package for sorting emulator ROM files',
	url='http://github.com/natemara/sortroms',
	author='Nate Mara',
	author_email='natemara@gmail.com',
	license='MIT',
	packages=['sortrom'],
	package_data={'sortrom': ['sortrom/*.json']},
	zip_safe=False
)
