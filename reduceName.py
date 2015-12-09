# -*- coding: utf-8 -*-

try:
	import fuzzy
except ImportError:
	print('Please install the fuzzy library: https://pypi.python.org/pypi/Fuzzy')
	print('pip install fuzzy')
	raise SystemExit(1)

from unidecode import unidecode

def reduceName(name):
	"""
	Similar to soundex, reduce the name to a string that loosely represents how
	it sounds. Names that may be confused should be reduced to the same value.
	"""
	# Convert diacritics to normal letter, e.g., ș -> s
	if type(name) == unicode:
		name = unidecode(name)

	# Double metaphone quirks
	name = name.replace('Ch', 'K')
	name = name.replace('th', 't')
	name = name.replace('C', 'K') # Romanian never uses K
	name = name.replace('c', 'k') # Romanian never uses K
	name = name.replace('w', 'v') # Polish does not have v
	name = name.replace('W', 'V') # Polish does not have v
	name = name.replace('j', 'i') # Confusing in Polish
	name = name.replace('en', 'an') # Confusing in French

	dmeta = fuzzy.DMetaphone()
	return dmeta(name)[0]
