'This module contains the WikipediaKnowledgeBase class'

import logging
import requests
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

	ARTICLE_URL_TEMPLATE='https://en.wikipedia.org/w/api.php?action=parse&format=json&redirects=1&page={0}'
	START_ARTICLE='List of most popular given names'

	DEFAULT_LANGUAGES = 'de en fr pl ro sv'.split()
	GENDERS = 'male female'.split()

	def __init__(self, languages = DEFAULT_LANGUAGES):
		self.languages = languages
		self.session = requests.session()

		self.namesCache = None

	@logStartAndEnd
	def getNamesCache(self):
		if self.namesCache:
			return self.namesCache

		namesCache = { 'male': [ ], 'female': [ ], 'unknown': [ ] }
		givenNamesPage = self.session.get(self.ARTICLE_URL_TEMPLATE.format(self.START_ARTICLE)).json()
		for link in givenNamesPage['parse']['links']:
			possibleGivenNameArticle = link['*']
			self.checkArticleForGivenName(possibleGivenNameArticle, namesCache)

		# Ensures atomicity
		self.namesCache = namesCache
		return self.namesCache

	@logStartAndEnd
	def checkArticleForGivenName(self, possibleGivenNameArticle, namesCache):
		# TODO: URL safe
		givenNamePage = self.session.get(self.ARTICLE_URL_TEMPLATE.format(possibleGivenNameArticle)).json()
		if 'error' in givenNamePage:
			logger.debug('Got error page for %s', possibleGivenNameArticle)
			return
		title = givenNamePage['parse']['title']
		text = givenNamePage['parse']['text']['*']
		lowerCaseText = text.lower()

		if 'given name' in title or 'given name' in text:
			givenName = title.partition(' ')[0]
			whereMasculine = lowerCaseText.find('masculine')
			whereFeminine = lowerCaseText.find('feminine')
			if whereMasculine == -1:
				whereMasculine = lowerCaseText.find(' male') # avoid matching 'fe*male*'
				if whereMasculine == -1:
					whereMasculine = len(text)
			if whereFeminine == -1:
				whereFeminine = lowerCaseText.find('female')
				if whereFeminine == -1:
					whereFeminine = len(text)

			if whereMasculine < whereFeminine:
				logger.debug('Found male given name %s', givenName)
				namesCache['male'].append(givenName)
			elif whereFeminine < whereMasculine:
				logger.debug('Found female given name %s', givenName)
				namesCache['female'].append(givenName)
			else:
				logger.debug('Found unknown given name %s', givenName)
				namesCache['unknown'].append(givenName)

	@logStartAndEnd
	def retrieveGivenNames(self, gender):
		'''
		Returns all given names for the specified gender in the configured
		languages.

			:param gender 'male' or 'female'
		'''

		if gender in [ 'male', 'female' ]:
			return self.getNamesCache()[gender]
		else:
			raise ValueError('Gender must be male or female')

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

class WikipediaKnowledgeBaseTest(unittest.TestCase):
	def setUp(self):
		self.kb = WikipediaKnowledgeBase()

	def testRetrieveMaleGivenNames(self):
		self.assertIn('Cristian', self.kb.retrieveGivenNames('male'))
		self.assertIn('Radu', self.kb.retrieveGivenNames('male'))

	def testRetrieveFemaleGivenNames(self):
		self.assertIn('Fatima', self.kb.retrieveGivenNames('female'))
		self.assertIn('Linda', self.kb.retrieveGivenNames('female'))

	def testRetrieveInvalidGender(self):
		self.assertRaises(ValueError, self.kb.retrieveGivenNames('hermaphrodite'))

	def testRetrieveMaleAlternateSpellings(self):
		self.assertEqual(self.kb.retrieveAlternateSpellings('Bogdan'), [ ])
		self.assertEqual(self.kb.retrieveAlternateSpellings('Cristian'),
			'Christian Cristian Krystian'.split())

	def testRetrieveFemaleAlternateSpellings(self):
		self.assertEqual(self.kb.retrieveAlternateSpellings('Barbara'), [ ])
		self.assertEqual(set(self.kb.retrieveAlternateSpellings('Judit')),
			'Judit Judith Judyta')
		self.assertEqual(set(self.kb.retrieveAlternateSpellings('Linda')),
			set())

if __name__ == '__main__':
	unittest.main()
