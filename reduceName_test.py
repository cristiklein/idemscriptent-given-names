# -*- coding: utf-8 -*-

from reduceName import reduceName

import unittest

class TestReduceName(unittest.TestCase):
	def test_pawel(self):
		self.assertEquals(reduceName(u'Paweł'), reduceName(u'Pawel'))
		self.assertEquals(reduceName(u'Paweł'), reduceName(u'Pavel'))

	def test_noah(self):
		self.assertEquals(reduceName(u'Noah'), reduceName(u'Noa'))

	def test_christian(self):
		self.assertEquals(reduceName(u'Cristian'), reduceName(u'Christian'))
		self.assertEquals(reduceName(u'Cristian'), reduceName(u'Krystian'))

	def test_stefan(self):
		self.assertEquals(reduceName(u'Stefan'), reduceName(u'Stephan'))
		self.assertEquals(reduceName(u'Stefan'), reduceName(u'Ștefan'))

	def test_leo(self):
		self.assertNotEquals(reduceName(u'Leo'), reduceName(u'Leon'))

	def test_anna(self):
		self.assertEquals(reduceName(u'Anna'), reduceName(u'Ana'))

	def test_different(self):
		self.assertNotEquals(reduceName(u'Barbara'), reduceName(u'Cristian'))

if __name__ == '__main__':
	unittest.main()
