import os
import json
import glob
import shutil

from .utils import get_datafile

cd = os.chdir
pwd = os.getcwd


def main(args):
	tags = get_tags()
	folders = args.folders

	for folder in folders:
		input('Press ENTER to org "{}"...'.format(folder))
		cd(folder)
		org_by_tags(tags)

	return 0


def filter_games(filter_by, folder_name=None):
	'''
	Finds all files matching filter_by, and moves them into a folder
	called folder_name. Returns the number of files moved. If no files
	match pattern, no folder is created.
	'''

	games = glob.glob(filter_by)
	if len(games) == 0:
		return 0
	if folder_name is None:
		folder_name = filter_by
	if not os.path.exists(folder_name):
		os.mkdir(folder_name)
	for game in games:
		shutil.move(game, folder_name)
	return len(games)


def build_country(country, country_code):
	'''
	Takes one country and one country code as arguments, moves all
	files with tags in the format "*(%)*" where "%" is the country
	code to the folder with the given name of the country. Also
	creates an "official" subfolder containing all official releases.
	'''

	official = '{0} Official'.format(country)

	official_games = 0
	games = filter_games('*({0})*'.format(country_code), country)

	if games != 0:
		cd(country)
		official_games = filter_games('*[!]*', official)
		official_games += filter_games('*({0}).nes'.format(country_code), official)
		cd('..')

	return {'games': games, 'official': official_games}


def get_tags():
	'''
	Returns a dict object holding all of the country names and tags in
	the format.

	{
		'Country Code': 'Country', ...
	}

	'''

	tag_string = get_datafile('tags.json')
	return json.loads(tag_string)


def org_by_tags(tags):
	'''
	For every country and country code in the given list of tags, put
	the files matching the code into a folder called country. Prints
	information about the number of files moved.
	'''

	for tag, country in tags.items():
		country_stats = build_country(country, tag)
		games = country_stats['games']
		official = country_stats['official']
		if games != 0:
			print('Built {0}... {1} games... {2} official.'.format(country, games, official))


if __name__ == '__main__':
	main()
