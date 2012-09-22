#!/usr/bin/python

from sys import argv
import tokenize
import token
import keyword



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
'''

trailer = '''</body>
</html>'''


        
#string.expandtabs()

#NEW PLAN:

#Use the method below to read the .py file into memory using file.readline. Tokenize it (try/except?), return a list of tokens, then use the keyword module to color words blue, numbers orange etc.  Allow the program to read in .inf/.conf file for easy color adjustments.
#Easy, right?



class PythonParse(object):


    def __init__(self, input):
        #TODO: check whitespace when putting string back together
        self._scan = {
        'NAME' : self.check_kywrd,
        'OP': self.check_op,
        'STRING': self.str_fmt,
        'COMMENT': self.cmt_fmt,
        'NEWLINE': self.new_line,
        #error here, dict cannot contain string values
        'INDENT': '',
        'NL': self.new_line,
        'DEDENT': '',
        'ENDMARKER': '',
        }
        self._input = open(input)
        self._output = open('%s.html' % input, 'w')  
        self._tokens = []
        self.get_tokens()
        self._input.close()
        self._output.write(header)
        self.analyze()
        self._output.write(trailer)
        self._output.close()
        
        
        
        #gonna call get_tokens and analyze here, perfect place
    
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
        
        for item in self._tokens:
            
            self._output.write(self._scan[item[0]](item[1]))       
        
        
    def check_kywrd(self, word):
        if keyword.iskeyword(word):
            return '<span class="ifdef"> ' + word + ' </span>'
        else:
            return ' ' + word
            
    def check_op(self, op):
        if op == '(' or op == ')':
            return '<span class="ifdef">' + op + '</span>'
        else:
            return op
            
    def str_fmt(self, str):
        return '<span class="str"> ' + str + '</span>'
     
    def cmt_fmt(self, cmt):
        return '<span class="comm"> ' + cmt + '</span>'
    
    def new_line(self, nl):
        return '<br />\n'
        
script, name = argv
#length check for argv later

PythonParse(name)
