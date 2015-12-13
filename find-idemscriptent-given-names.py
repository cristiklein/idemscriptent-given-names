#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from unidecode import unidecode
from glob import glob
import logging

from reduceName import reduceName

if __name__ == '__main__':
	logging.basicConfig(
		level = logging.DEBUG,
		format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	)

	genderToNameToLanguages = { 'm': defaultdict(list), 'f': defaultdict(list) }
	for fileName in glob('names-*.txt'):
		fileNameWithoutExt, _ = fileName.split('.')
		_, gender, language = fileNameWithoutExt.split('-')

		with open(fileName) as f:
			for line in f.readlines():
				for name in line.split('/'):
					name = name.decode('utf8').strip().capitalize()
					# eliminate diacritic marks, e.g., é becomes e
					name = unidecode(name)
					genderToNameToLanguages[gender][name].append(language)

	for gender in genderToNameToLanguages:
		print '===', gender, '==='
		for name, languages in sorted(genderToNameToLanguages[gender].iteritems(),
			key = lambda nameLanguage: -len(nameLanguage[1])):

			languages = sorted(languages)
			if len(languages) > 2:
				print "{0}: {1}".format(name, ' '.join(languages))
