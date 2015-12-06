'This module contains the WikipediaKnowledgeBase class'

import logging
import time

logger = logging.getLogger(__name__)

def logStartAndEnd(method):
	'Annotation to log when a method is entered or exited.'
	def loggedMethod(*args, **kwargs):
		# Produce a friendly string with all arguments
		argsAsString = [ str(arg) for arg in args ] + \
			[ str(k) + '=' + str(v) for k,v in kwargs.items() ]
		argsAsString = ','.join(argsAsString)

		logger.debug('Entering %s(%s)', method.__name__, argsAsString)
		startTime = time.time()
		try:
			ret = method(*args, **kwargs)
		except Exception as e:
			endTime = time.time()
			logger.debug('Exiting  %s(%s) threw %s after %dms', method.__name__,
				argsAsString, str(e), (endTime - startTime) * 1000)
			raise
		endTime = time.time()
		logger.debug('Exiting  %s(%s) -> %s in %dms', method.__name__,
			argsAsString, ret, (endTime - startTime) * 1000)
		return ret
	return loggedMethod

class WikipediaKnowledgeBase:
	'Taps into Wikipedia to retrieve trivia about given names.'

	DEFAULT_LANGUAGES = 'de en fr pl ro sv'.split()
	GENDERS = 'male female'.split()

	def __init__(self, languages = DEFAULT_LANGUAGES):
		self.languages = languages

	@logStartAndEnd
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

	@logStartAndEnd
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
