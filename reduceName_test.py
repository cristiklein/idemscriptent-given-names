from reduceName import reduceName

import unittest

class TestReduceName(unittest.TestCase):
	def test_pawel(self):
		self.assertEquals(reduceName('Paweł'), reduceName('Pawel'))
		self.assertEquals(reduceName('Paweł'), reduceName('Pavel'))

	def test_noah(self):
		self.assertEquals(reduceName('Noah'), reduceName('Noa'))

	def test_christian(self):
		self.assertEquals(reduceName('Cristian'), reduceName('Christian'))
		self.assertEquals(reduceName('Cristian'), reduceName('Krystian'))

	def test_stefan(self):
		self.assertEquals(reduceName('Stefan'), reduceName('Stephan'))
		self.assertEquals(reduceName('Stefan'), reduceName('Ștefan'))

	def test_leo(self):
		self.assertEquals(reduceName('Leo'), reduceName('Leon'))

	def test_anna(self):
		self.assertEquals(reduceName('Anna'), reduceName('Ana'))

	def test_different(self):
		self.assertNotEquals(reduceName('Barbara'), reduceName('Cristian'))

if __name__ == '__main__':
	unittest.main()
