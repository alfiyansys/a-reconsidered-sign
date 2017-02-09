import string
from .. import core

def caesar(text, shift):
	trans = ''
	for char in text:
		if char.isalpha():
			ascii = ord(char)
			ascii += shift
			if ascii - shift == 32:
				continue

			if ascii > 90:
				ascii -= 26
			elif ascii < 65:
				ascii += 26

			trans += chr(ascii)
		else:
			trans += char
	return trans

def decode(text, shift=None):
	core.separator()
	print "CAESAR CIPHER"
	text = str.upper(text)
	print "Converting to uppercase...", text

	length = len(text)
	#text = list(text)
	if shift==None:
		print "Using all possible shift..."
		for i in range(1,26):
			print caesar(text,i)
	else:
		print "Using",shift,"shift"
		print caesar(text,int(shift))