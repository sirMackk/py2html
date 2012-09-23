#!/usr/bin/python

from sys import argv
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
<div id="main_container"><pre>
'''

trailer = '''</pre></div></body>
</html>'''




class PythonParse(object):
#TODO: Fix white space between words
#TODO: Make colors global vars, easier to modify
#TODO: Fix __docs__

    def __init__(self, input):
        #This dict might be handy
        #self._ops = ['=', '+', '-', '*', '//', '%',
               # '**', '////', '==', '+=', '-=', '*=', '//=',
                #'%=', '**=', '////=', '!=', '<>', '>', '<',
                #'>=', '<=']
        

        self.indent = ''
        self._input = open(input)
        self._output = open('%s.html' % input[:-3], 'w')
        self._output.write(header)
        self.analyze()


    
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
        tokens = tokenize.generate_tokens(self._input.readline)
        for toknum, tokval, (srow, scol), (erow, ecol), line in tokens:
            tokname = token.tok_name[toknum]
            if tokname == 'NEWLINE' or tokname == 'NL':
                self._output.write('\n%s' % self.indent)
            elif tokname == 'INDENT':
                self._output.write('    ')
                self.indent += '    '
                
            elif tokname == 'DEDENT':
                
                self._output.seek(-4, 1)
                self.indent = self.indent[:-4]

            elif keyword.iskeyword(tokval) or tokval == '(' or tokval == ')':
                self._output.write('<span class="%s">%s</span>' % ('ifdef', tokval))

           # '<span class"%s">%s</span>' % (colors[tokname], tokval)
               

            elif tokname == 'NAME' or tokname == 'OP':

                self._output.write(tokval)
                            
            
            elif tokname == 'NUMBER':
                self._output.write('<span class="%s">%s</span>' % ('int', tokval))

            elif tokname == 'STRING':
                self._output.write('<span class="%s">%s</span>' % ('str', cgi.escape(tokval)))                

            elif tokname == 'COMMENT':
                self._output.write('<span class="%s">%s</span>' % ('comm', tokval))  
            #tokname == endmarker case
            else:
                self._output.write(trailer)
                self._input.close()
                self._output.close()
     
script, name = argv
#length check for argv later

PythonParse(name)
