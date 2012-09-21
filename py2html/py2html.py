#!/usr/bin/python

from sys import argv
from re import search, split
from cStringIO import StringIO
import tokenize
import token
import keyword

html = {'ifdef': '<span class="ifdef">', 
        'number': '<span class="int">',
        'definition': '<span class="def">'
        'string': '<span class="str">',
        'comment:' '<span class="comm">',
        'lb' = '<br />'
        'end_span' = '<br />'}
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
.comment {
color:#008000;
}

</style>
</head>
<body>'''

trailer = '''</body>
</html>'''


        
#string.expandtabs()

#NEW PLAN:

#Use the method below to read the .py file into memory using file.readline. Tokenize it (try/except?), return a list of tokens, then use the keyword module to color words blue, numbers orange etc.  Allow the program to read in .inf/.conf file for easy color adjustments.
#Easy, right?

#TODO: Later on, check if whitespace is parsed properly by browser, if not, than add &nbsp

#THIS SOLUTION WAS SUGGESTED ON STACKOVERFLOW,
# import tokenize
# import token
# import io

# text = '''
# x = 'hello there'  
# if x == 'example "quotes" inside quotes' and y == 'another example': pass
# '''


# tokens = tokenize.generate_tokens(io.BytesIO(text).readline)
# for toknum, tokval, (srow, scol), (erow, ecol), line in tokens:
    # tokname = token.tok_name[toknum]
    # print(tokname, tokval)

class PythonParse(object):

    def __init__(self, input, output):
        #input and output will be file objects?
        self._input = input
        self._output = output  
        self._tokens = []
        
        #gonna call get_tokens and analyze here, perfect place
    
    def get_tokens(self):
        '''This function will tokenize self._input and append self._tokens with a list of tuples'''
        tokens = tokenize.generate_tokens(self._input.realine)
        for toknum, tokval, (srow, scol), (erow, ecol), line in tokens:
            tokname = token.tok_name[toknum]
            self._tokens.append((tokname, tokval))
            
        
    def analyze(self):
        '''This method will accept a list of token pairs from get_tokens
        and it's gonna analyze it, add the appropriate html tags, and add it to 
        the _output object'''
        #single loop to go over token types, decide on type what to do
        for item in _self.tokens:
            if item[0] == 'NAME':
                #call check name func
                pass
            elif item[0] == 'OP' and item[1] == '(' or item[1] == ')':
                #call parenthesis color func
                pass
            elif item[0] == 'NUMBER':
                self.output.write('%sitem[1]%s' % (html['number'], html['end_span']))
            #continue this for rest of token types
            
       
        
    def get_html(self):
        pass