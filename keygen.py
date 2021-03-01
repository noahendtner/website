#!/usr/bin/python
from random import choice

letters = "ABCDEFGHIJKLMOPQRTUVWXYZ"
prefix = "SN"


def genKey(_prefix, prefix, letters):
	TEMPLATE = "pAAAAAAAAAAAA"
	new = []
	if _prefix not in prefix:
		return 0
	elif _prefix in letters:
		return 0
	else:
		for char in TEMPLATE:
			if char == "A":
				char = choice(letters)
			elif char == "p":
				char = _prefix
			new.append(char)

		return "".join(new)

print(genKey("S", prefix, letters))