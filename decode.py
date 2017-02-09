#!/usr/bin/python

# A Reconsidered Sign, anagram of Ian Ingress Decoder

# Python include
import sys

# Module include
import algorithms.core as core
from algorithms.cipher import *

text = sys.argv[1]
p2 = sys.argv[2]

print 

core.first_analysis(text)
caesar.decode(text,p2)