try:
	import fuzzy
except ImportError:
	print('Please install the fuzzy library: https://pypi.python.org/pypi/Fuzzy')
	print('pip install fuzzy')
	raise SystemExit(1)

def reduceName(name):
	"""
	Similar to soundex, reduce the name to a string that loosely represents how
	it sounds. Names that may be confused should be reduced to the same value.
	"""
	dmeta = fuzzy.DMetaphone()
	return dmeta('fuzzy')[0]
