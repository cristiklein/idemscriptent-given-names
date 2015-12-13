#!/usr/bin/env python3

from collections import defaultdict
from unidecode import unidecode
from glob import glob

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

	for gender in genderToNameToLanguages:
		print('===', gender, '===')
		for name, languages in sorted(genderToNameToLanguages[gender].items(),
			key = lambda nameLanguage: -len(nameLanguage[1])):

			if len(languages) > 2:
				print("{0}: {1}".format(name, ' '.join(sorted(languages))))
