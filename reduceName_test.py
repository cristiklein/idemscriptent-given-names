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
		self.assertEquals(reduceName(u'Leo'), reduceName(u'Léo'))

	def test_anna(self):
		self.assertEquals(reduceName(u'Anna'), reduceName(u'Ana'))

	def test_mina(self):
		self.assertEquals(reduceName(u'Minna'), reduceName(u'Mina'))

	def test_lili(self):
		self.assertEquals(reduceName(u'Lily'), reduceName(u'Lilly'))
		self.assertEquals(reduceName(u'Lily'), reduceName(u'Lili'))

	def test_eric(self):
		self.assertEquals(reduceName(u'Eric'), reduceName(u'Erik'))

	def test_sara(self):
		self.assertEquals(reduceName(u'Sara'), reduceName(u'Sarah'))

	def test_felix(self):
		self.assertEquals(reduceName(u'Felix'), reduceName(u'Feliks'))

	def test_adrian(self):
		self.assertEquals(reduceName(u'Adrien'), reduceName(u'Adrian'))

	def test_jacob(self):
		self.assertEquals(reduceName(u'Jacob'), reduceName(u'Jakub'))

	def test_agata(self):
		self.assertEquals(reduceName(u'Agata'), reduceName(u'Agatha'))

	def test_different(self):
		self.assertNotEquals(reduceName(u'Barbara'), reduceName(u'Cristian'))
		self.assertNotEquals(reduceName(u'Nora'), reduceName(u'Lara'))
		self.assertNotEquals(reduceName(u'Bastian'), reduceName(u'Sebastian'))
		self.assertNotEquals(reduceName(u'Mina'), reduceName(u'Lina'))
		self.assertNotEquals(reduceName(u'Marta'), reduceName(u'Mara'))
		self.assertNotEquals(reduceName(u'Katarina'), reduceName(u'Sabina'))

if __name__ == '__main__':
	unittest.main()
