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

if __name__ == '__main__':
	unittest.main()
