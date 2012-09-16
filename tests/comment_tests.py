from nose.tools import *
from py2html.py2html import is_comment_or_doc


#test out comments
def test_comment_1():
    test_comment_line = '#test test test'
    assert_equal(is_comment_or_doc(test_comment_line), '<span class="comm">%s</span><br />' % test_comment_line)



def test_comment_4():
    test_comment_space = '# test test test'
    assert_equal(is_comment_or_doc(test_comment_space), '<span class="comm">%s</span><br />' % test_comment_space)

#test out __doc__

def test_comment_doc1():
    test_comment_doc1 = '\'\'\'test test test\'\'\''
    assert_equal(is_comment_or_doc(test_comment_doc1), '<span class="doc">%s</span><br />' % test_comment_doc1)

def test_comment_doc2():
    test_comment_doc2 = '\'\'\' test test test\'\'\''
    assert_equal(is_comment_or_doc(test_comment_doc2), '<span class="doc">%s</span><br />' % test_comment_doc2)

def test_comment_doc3():
    test_doc = '\'\'\'Beginning od doc test'
    assert_equal(is_comment_or_doc(test_doc), '<span class="doc">%s</span><br />' % test_doc)

def test_comment_doc4():
    test_doc2 = 'Beginning od doc test\'\'\''
    assert_equal(is_comment_or_doc(test_doc2), '<span class="doc">%s</span><br />' % test_doc2)