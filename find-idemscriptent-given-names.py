#!/usr/bin/env python3

def readNameList(fileName):
	"""
	Read a list of names from a file, one by line. Ignores comments
	that start with '#' and empty lines.
	"""
	with open(fileName) as f:
		lines = f.readlines()

	names = [ ]
	for line in lines:
		name = line[:line.rfind('#')].strip()
		if name:
			names.append(name)

	return names

if __name__ == '__main__':
	print(readNameList('male-given-names.list'))
