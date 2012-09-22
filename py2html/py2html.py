#!/usr/bin/python

from sys import argv
from string import expandtabs
import tokenize
import token
import keyword
import cgi



#example header, later must add modifieable colors
header = '''<!DOCTYPE html>
<html>
<head>
<style type="text/css">
body {
background-color:#228B22;
color:#000000;
}
/*style for main container*/
#main_container {
background-color:#FFFFFF;
width:95%;
height:auto;
padding:25px;
font-family:courier new;
 }
/*style for code containing divs*/
.code {
background-color:#FFFFFF;
width:95%;
height:auto;
padding-left:25px;
font-family:courier new;
 }
/*styles for code colors, using span*/
/*test colors temporarily*/
.ifdef {
color:#0000CD;
}

.def {
color:#FF00FF;
}
.int {
color:#FF8C00;
}
.str {
color:#A9A9A9;
}
.comm {
color:#008000;
}

</style>
</head>
<body>
<div id="main_container">
'''

trailer = '''</div></body>
</html>'''




class PythonParse(object):


    def __init__(self, input):
        #TODO: whitespace isn't good. Idea: change tokens so they include the whole line, take white space before line and .write it to file, then second loop to handle tokens build rest of line, when \n, outer loop incs by one. This might work, plus it will reduce the number of functions, I can use an if-elif-else block instead.
        self._scan = {
        'NAME' : self.check_kywrd,
        'OP': self.check_op,
        'NUMBER': self.number,
        'STRING': self.str_fmt,
        'COMMENT': self.cmt_fmt,
        'NEWLINE': self.new_line,
        'INDENT': self.indent,
        'NL': self.new_line,
        'DEDENT': self.deindent,
        'ENDMARKER': self.deindent,
        }
        self._ops = ['=', '+', '-', '*', '//', '%',
                '**', '////', '==', '+=', '-=', '*=', '//=',
                '%=', '**=', '////=', '!=', '<>', '>', '<',
                '>=', '<=']

        self.indent = ''
        self._input = open(input)
        self._output = open('%s.html' % input, 'w')
        self._tokens = []
        self.get_tokens()
        self._input.close()
        self._output.write(header)
        self.analyze()
        self._output.write(trailer)
        self._output.close()

    
    def get_tokens(self):
        '''This function will tokenize self._input and append self._tokens with a list of tuples'''
        tokens = tokenize.generate_tokens(self._input.readline)
        for toknum, tokval, (srow, scol), (erow, ecol), line in tokens:
            tokname = token.tok_name[toknum]
            #print (tokname, tokval)
            self._tokens.append((tokname, tokval))
            
        
    def analyze(self):
        '''This method will accept a list of token pairs from get_tokens
        and it's gonna analyze it, add the appropriate html tags, and add it to 
        the _output object'''
        
        for i in xrange(len(self._tokens)):

            self._output.write(self._scan[self._tokens[i][0]](self._tokens[i][1]))
        
        
    def check_kywrd(self, word):
        if keyword.iskeyword(word):
            return '<span class="ifdef"> ' + word + ' </span>'
        else:
            return word
            
    def check_op(self, op):
        if op == '(' or op == ')':
            return '<span class="ifdef">' + op + '</span>'
        elif op == ',':
            return op + ' '
        elif op in self._ops:
            return ' ' + op + ' '
        else:
            return op
            
    def str_fmt(self, str):
        return '<span class="str"> ' + cgi.escape(str) + '</span>'
     
    def cmt_fmt(self, cmt):
        return '<span class="comm">' + cmt + '</span>'
    
    def new_line(self, nl):
        return '<br />\n' + self.indent

    def indent(self, ind):
        self.indent += ('&nbsp' * len(ind.expandtabs(4)))
        return ''

    def deindent(self, ind):
        self.indent = ''
        return ''

    def number(self, num):
        return '<span class="int">' + num + '</span>'

        
script, name = argv
#length check for argv later

PythonParse(name)
