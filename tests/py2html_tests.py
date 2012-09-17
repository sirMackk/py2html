from nose.tools import *
from py2html.py2html import *

def test_def_1():
    test_def = '__init__(self):'
    equal_def = '<span class="ifdef">def </span><span class="def">__init__</span><span class="ifdef">(</span>self<span class="ifdef">)</span>:<br />'
    
    assert_equal(first_word_def(test_def), equal_def)

def test_def_2():
    test_def2 = 'function(self):'
    equal_def2 = '<span class="ifdef">def </span><span class="def">function</span><span class="ifdef">(</span>self<span class="ifdef">)</span>:<br />'
    
    assert_equal(first_word_def(test_def2), equal_def2)

def test_def_3():
    test_def3 = 'function():'
    equal_def3 = '<span class="ifdef">def </span><span class="def">function</span><span class="ifdef">(</span><span class="ifdef">)</span>:<br />'
    
    assert_equal(first_word_def(test_def3), equal_def3)

def test_first_word():
    flow_control = ['class', 'if', 'elif', 'else', 'while', 'for', 'return', 'from', 'import', 'print']

    for i in flow_control:

        word_equal = '<span class="ifdef">%s </span>' % i
        assert_equal(first_word(i), word_equal)

def test_first_word2():
    other_words = ['output', 'x', 'player']

    for i in other_words:

        word_equal = '%s' % i
        assert_equal(first_word(i), word_equal)


def test_find_strings1():
    string_test = "if x == 'yes':"
    string_test_equal = 'if x == <span class="comm">\'yes\'</span>:'
    
    assert_equal(find_strings(string_test), string_test_equal)

def test_find_strings2():
    string_test = "if x == 'yes' or y == 'no':"
    string_test_equal = 'if x == <span class="comm">\'yes\'</span> or y == <span class="comm">\'no\'</span>:'
    
    assert_equal(find_strings(string_test), string_test_equal)

   

