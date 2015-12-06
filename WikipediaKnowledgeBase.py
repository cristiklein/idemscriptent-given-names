'This module contains the WikipediaKnowledgeBase class'

import logging

logger = logging.getLogger(__name__)

class WikipediaKnowledgeBase:
	'Taps into Wikipedia to retrieve trivia about given names.'

	DEFAULT_LANGUAGES = 'de en fr pl ro sv'.split()
	GENDERS = 'male female'.split()

	def __init__(self, languages = DEFAULT_LANGUAGES):
		self.languages = languages

	def retrieveGivenNames(self, gender):
		'''
		Returns all given names for the specified gender in the configured
		languages.

			:param gender 'male' or 'female'
		'''

		# TODO
		if gender == 'male':
			return [ 'Ahmed', 'Mohammed', 'Mahamad', 'David', 'Davit' ]
		elif gender == 'female':
			return [ 'Fatima', 'Fatime', 'Linda' ]
		else:
			raise NotImplemented('Unknown gender {0}'.format(gender))

	def retrieveAlternateSpellings(self, name):
		'''
		Returns all alternative spellings for a name, not including the name
		itself, in the configured languages.

			:param name: the name to retrieve alternative spellings for
		'''

		# TODO
		examples = {
			'Ahmed': [ ],
			'David': [ 'Davit' ],
			'Davit': [ 'David' ],
			'Fatima': 'Fatime',
			'Fatime': 'Fatima',
			'Linda': [ ],
			'Mahamad': [ 'Mohammed' ],
			'Mohammed': [ 'Mohammed' ],
		}

		return examples[name]
