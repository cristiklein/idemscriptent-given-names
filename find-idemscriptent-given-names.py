#!/usr/bin/env python3

from collections import defaultdict
from unidecode import unidecode
from glob import glob

def sortByNumLanguagesDescThenByNameAsc(nameLanguageTuple):
	'''
	This function returns a key that is suitable for sorting by the number of
	languages a particular name appears in, descending, then by name
	alphabetically, ascending.
	'''
	return ( -len(nameLanguageTuple[1]), nameLanguageTuple[0] )

if __name__ == '__main__':
	genderToNameToLanguages = { 'm': defaultdict(list), 'f': defaultdict(list) }
	for fileName in glob('names-*.txt'):
		fileNameWithoutExt, _ = fileName.split('.')
		_, gender, language = fileNameWithoutExt.split('-')

		with open(fileName) as f:
			for line in f.readlines():
				for name in line.split('/'):
					name = name.strip().capitalize()
					# eliminate diacritic marks, e.g., é becomes e
					name = unidecode(name)
					genderToNameToLanguages[gender][name].append(language)

	for gender in sorted(genderToNameToLanguages):
		print('Names for', gender)
		print('===========')
		for name, languages in sorted(genderToNameToLanguages[gender].items(),
			key = sortByNumLanguagesDescThenByNameAsc):

			if len(languages) > 2:
				print("{0:10}: {1}".format(name, ' '.join(sorted(languages))))
		print()
