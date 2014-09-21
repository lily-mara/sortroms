import os
import json
import glob
import shutil

cd = os.chdir
pwd = os.getcwd


def main():
	tags = get_tags()
	folders = get_folders()

	for folder in folders:
		input('Press ENTER to org "{}"...'.format(folder))
		cd(folder)
		org_by_tags(tags)

	return 0


def filter_games(filter_by, folder_name=None):
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
	with open('tags.json', 'r') as jsonfile:
		return json.load(jsonfile)


def get_folders():
	with open('folders.json', 'r') as jsonfile:
		return json.load(jsonfile)


def org_by_tags(tags):
	for tag, country in tags.items():
		country_stats = build_country(country, tag)
		games = country_stats['games']
		official = country_stats['official']
		if games != 0:
			print('Built {0}... {1} games... {2} official.'.format(country, games, official))


if __name__ == '__main__':
	main()
