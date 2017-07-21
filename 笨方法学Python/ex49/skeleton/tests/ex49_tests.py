# -- coding: utf-8 --
from nose.tools import *
from ex49.ex49 import *


def test_Sentence():
  sentence = Sentence(('noue', 'pencil'), ('verb', 'hit'), ('direction', 'north'))
  assert_equal(sentence.subject, 'pencil')

def test_peek():
  peek1 = [('noue', 'pencil'), ('verb', 'hit'), ('direction', 'north')]
  peek2 = ([('direction', 'north')])
  peek3 = ([])
  assert_equal(peek1, 'noun')
  assert_equal(peek2, 'direction')
  assert_equal(peek3, None)

def test_match():
  match = match([('verb', 'hit'), ('noun', 'pencil')], 'verb')
  assert_equal(match, ('verb', 'pencil'))

def test_parse_subject():
  last_sentence = Sentence(('', ''), ('', ''), ('', ''))
  last_sentence = parse_subject([('verb', 'hit'), ('direction', 'north')], ('noun', 'pencil')) 
  assert_equal(last_sentence, 'hit')