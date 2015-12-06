#!/usr/bin/env python3

import logging

from WikipediaKnowledgeBase import WikipediaKnowledgeBase

if __name__ == '__main__':
	logging.basicConfig(
		level = logging.DEBUG,
		format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	)

	kb = WikipediaKnowledgeBase()

	for gender in kb.GENDERS:
		givenNames = kb.retrieveGivenNames(gender)
		for givenName in givenNames:
			alternateSpellings = kb.retrieveAlternateSpellings(givenName)
			if not alternateSpellings:
				print(givenName)
