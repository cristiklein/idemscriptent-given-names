'This module contains the WikipediaKnowledgeBase class'

import logging
import time
import unittest

logger = logging.getLogger(__name__)

def prettyInterval(intervalInSeconds):
	'Returns a string representing a time interval in a human-friendly format.'

	# To reduce overhead, start with the smaller intervals
	if intervalInSeconds < 0.002:
		return str(int(intervalInSeconds * 1000000)) + 'µs'
	elif intervalInSeconds < 2:
		return str(int(intervalInSeconds * 1000)) + 'ms'
	elif intervalInSeconds < 120:
		return str(int(intervalInSeconds)) + 's'
	else:
		return str(int(intervalInSeconds / 60)) + 'm'

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
			logger.debug('Exiting  %s(%s) threw %s after %s', method.__name__,
				argsAsString, str(e), prettyInterval(endTime - startTime))
			raise
		endTime = time.time()
		logger.debug('Exiting  %s(%s) -> %s in %s', method.__name__,
			argsAsString, ret, prettyInterval(endTime - startTime))
		return ret
	return loggedMethod

class LoggingTest(unittest.TestCase):
	def testPrettyInterval(self):
		self.assertEqual(prettyInterval(120), '2m');
		self.assertEqual(prettyInterval(60), '60s');
		self.assertEqual(prettyInterval(59.5), '59s');
		self.assertEqual(prettyInterval(1), '1000ms');
		self.assertEqual(prettyInterval(0.999), '999ms');
		self.assertEqual(prettyInterval(0.001), '1000µs');
		self.assertEqual(prettyInterval(0.0001), '100µs');

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

if __name__ == '__main__':
	unittest.main()
