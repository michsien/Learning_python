from nose.tools import *

from ex49 import parser

import sys, os
sys.path.insert(0,os.path.abspath(__file__ + "/../../../ex48"))
print (sys.path)
from ex48 import lexicon

def test_peek():
	parser.peek([])