from setuptools import setup
setup(
	name='sortroms',
	version='1.1.1',
	description='Python package for sorting emulator ROM files',
	url='http://github.com/natemara/sortroms',
	author='Nate Mara',
	author_email='natemara@gmail.com',
	license='MIT',
	packages=['sortroms'],
	package_data={'sortroms.data': ['*.json']},
	include_package_data=True,
	entry_points={
		"console_scripts": [
			"sortroms=sortroms:main"
		],
	},
	zip_safe=False
)
