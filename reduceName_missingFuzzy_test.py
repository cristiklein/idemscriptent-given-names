import unittest
import sys

class TestReduceNameLibraries(unittest.TestCase):
	def test_missing_fuzzy(self):
		# Clear PYTHONPATH to emulate fuzzy missing
		sys.path = sys.path[:1]
		def importReduceName():
			from reduceName import reduceName
		self.assertRaises(SystemExit, importReduceName)

if __name__ == '__main__':
	unittest.main()
