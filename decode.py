#!/usr/bin/python

# A Reconsidered Sign, anagram of Ian Ingress Decoder

# Python include
import sys

# Module include
import algorithms.core as core
from algorithms.cipher import *

# Dynamic input processing
text = sys.argv[1]
if len(sys.argv) == 3:
	p2 = sys.argv[2]

# Input parser for every module
## Caesar
try:
	var_caesar = [text,p2]
except:
	var_caesar = [text]



core.first_analysis(text)

caesar.decode(var_caesar)