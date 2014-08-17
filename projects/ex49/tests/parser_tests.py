from nose.tools import *

from ex49 import parser
from ex49.parser import ParserError

import sys, os
sys.path.insert(0,os.path.abspath(__file__ + "/../../../ex48"))
from ex48 import lexicon

def test_peek():
	# check peeking on empty word list, list with 1 item, list with many items
	assert_equal(parser.peek([]), None)
	assert_equal(parser.peek(lexicon.scan("north")), "direction")
	assert_equal(parser.peek(lexicon.scan("go north now")), "verb")

def test_match():
	# matching with a list with 0 items
	assert_equal(parser.match([], "verb"), None)

	# matching with a list with 1 item (items are poped when match found 
	# -> list need to be reconstructed)
	word_list = lexicon.scan("north")
	assert_equal(parser.match(word_list, "direction"), ("direction", "north"))
	word_list = lexicon.scan("north")
	assert_equal(parser.match(word_list, "noun"), None)

	# matching with a list with many items
	word_list = lexicon.scan("haha go up quickly")
	assert_equal(parser.match(word_list, "error"), ("error", "haha"))
	word_list = lexicon.scan("haha go up quickly")
	assert_equal(parser.match(word_list, "verb"), None)

def test_skip():
	# skiping with an empty list
	word_list = []
	parser.skip(word_list, "noun")
	assert_equal(word_list, [])

	# skipping with a list with 1 item
	word_list = lexicon.scan("in")
	parser.skip(word_list, "noun")
	assert_equal(word_list, [("stop", "in")])
	parser.skip(word_list, "stop")
	assert_equal(word_list, [])

	# skipping with lists with many items
	word_list = lexicon.scan("in of from")
	parser.skip(word_list, "stop")
	assert_equal(word_list, [])

	word_list = lexicon.scan("Go up or down")
	parser.skip(word_list, "verb")
	assert_equal(word_list, [("direction", "up"),
							 ("error", "or"),
							 ("direction", "down")])

def test_parse_verb():
	# parsing with an empty word list
	word_list = []
	assert_raises(ParserError, parser.parse_verb, word_list)

	# parsing correct word lists
	word_list = lexicon.scan("Of the in go")
	assert_equal(parser.parse_verb(word_list), ("verb", "go"))

	word_list = lexicon.scan("go")
	assert_equal(parser.parse_verb(word_list), ("verb", "go"))

	# parsing incorrect word lists
	word_list = lexicon.scan("Of the in jsjhjhj")
	assert_raises(ParserError, parser.parse_verb, word_list)

	word_list = lexicon.scan("jsjhjhj")
	assert_raises(ParserError, parser.parse_verb, word_list)

def test_parse_object():
	# parsing with empty word list
	word_list = []
	assert_raises(ParserError, parser.parse_object, word_list)

	# parsing correct word lists
	word_list = lexicon.scan("Of in the princess")
	assert_equal(parser.parse_object(word_list), ("noun", "princess"))

	word_list = lexicon.scan("bear")
	assert_equal(parser.parse_object(word_list), ("noun", "bear"))


	word_list = lexicon.scan("from at in the south")
	assert_equal(parser.parse_object(word_list), ("direction", "south"))

	word_list = lexicon.scan("down")
	assert_equal(parser.parse_object(word_list), ("direction", "down"))

	# parsing incorrect word lists
	word_list = lexicon.scan("go")
	assert_raises(ParserError, parser.parse_object, word_list)

	word_list = lexicon.scan("from at in the 98")
	assert_raises(ParserError, parser.parse_object, word_list)



def test_parse_subject():
	# parse word lists with no verb after initial stops
	word_list = lexicon.scan("After from south")
	assert_raises(ParserError, parser.parse_subject, word_list, ("", ""))

	word_list = lexicon.scan("After from")
	assert_raises(ParserError, parser.parse_subject, word_list, ("", ""))

	word_list = lexicon.scan("bear After from")
	assert_raises(ParserError, parser.parse_subject, word_list, ("", ""))

	# parse word lists with no obj after: initial stops, verb and further stops 
	word_list = lexicon.scan("After at go")
	assert_raises(ParserError, parser.parse_subject, word_list, ("", ""))

	word_list = lexicon.scan("After at go at")
	assert_raises(ParserError, parser.parse_subject, word_list, ("", ""))

	word_list = lexicon.scan("After at go at 191919")
	assert_raises(ParserError, parser.parse_subject, word_list, ("", ""))

	# parse a correct word list and a subject
	word_list = lexicon.scan("at kill from bear")
	sentence = parser.parse_subject(word_list, ("noun", "Player"))
	assert_equal(sentence.subject, "Player")
	assert_equal(sentence.object, "bear")
	assert_equal(sentence.verb, "kill")

def test_parse_sentence():
	# parse an empty word list
	word_list = []
	assert_raises(ParserError, parser.parse_sentence, word_list)

	# parse other wrong word lists
	word_list = lexicon.scan("999 go bear")
	assert_raises(ParserError, parser.parse_sentence, word_list)

	word_list = lexicon.scan("go kill bear")
	assert_raises(ParserError, parser.parse_sentence, word_list)

	word_list = lexicon.scan("stop")
	assert_raises(ParserError, parser.parse_sentence, word_list)

	word_list = lexicon.scan("bear")
	assert_raises(ParserError, parser.parse_sentence, word_list)

	word_list = lexicon.scan("Princess go")
	assert_raises(ParserError, parser.parse_sentence, word_list)

	word_list = lexicon.scan("Princess bear")
	assert_raises(ParserError, parser.parse_sentence, word_list)

	word_list = lexicon.scan("Princess jjkjkj ")
	assert_raises(ParserError, parser.parse_sentence, word_list)

	word_list = lexicon.scan("Princess go kill bear")
	assert_raises(ParserError, parser.parse_sentence, word_list)

	word_list = lexicon.scan("Princess go now")
	assert_raises(ParserError, parser.parse_sentence, word_list)

	# parse correct word lists
	word_list = lexicon.scan("PrinceSS go from bear")
	sentence = parser.parse_sentence(word_list)
	assert_equal(sentence.subject, "PrinceSS")
	assert_equal(sentence.object, "bear")
	assert_equal(sentence.verb, "go")

	word_list = lexicon.scan("stop at the door")
	sentence = parser.parse_sentence(word_list)
	assert_equal(sentence.subject, "player")
	assert_equal(sentence.object, "door")
	assert_equal(sentence.verb, "stop")















