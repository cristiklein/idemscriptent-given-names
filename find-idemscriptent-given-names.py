#!/usr/bin/env python

from collections import defaultdict
from glob import glob
import logging

from reduceName import reduceName

if __name__ == '__main__':
	logging.basicConfig(
		level = logging.DEBUG,
		format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	)

	names = { 'm': [], 'f': [] }
	for fileName in glob('names-*.txt'):
		fileNameWithoutExt, _ = fileName.split('.')
		_, gender, language = fileNameWithoutExt.split('-')

		with open(fileName) as f:
			for line in f.readlines():
				for name in line.split('/'):
					name = name.strip().capitalize()
					names[gender].append(name)

	reductionToNames = {
		'm': defaultdict(set),
		'f': defaultdict(set),
	}
	for gender in names:
		for name in names[gender]:
			reductionToNames[gender][reduceName(name)].add(name)

	for gender in names:
		uniqueNames = []
		for similarSound, similarNames in reductionToNames[gender].items():
			if len(similarNames) == 1:
				uniqueNames.append(similarNames.pop())

		for name in sorted(uniqueNames):
			print name
		print
			
