from nose.tools import *
from py2html.py2html import first_word_def

def test_def_1():
    test_def = '__init__(self):'
    equal_def = '<span class="ifdef">def </span><span class="defi">__init__</span><span class="ifdef">(</span>self<span class="ifdef">)</span>:'
    
    assert_equal(first_word_def(test_def), equal_def)

