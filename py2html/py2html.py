# PythonParse

from sys import argv
from tokenize import generate_tokens
from token import tok_name
from keyword import iskeyword
from cgi import escape



#example header, later must add modifieable colors




class PythonParse(object):

#TODO: Make colors global vars, easier to modify
#TODO: Fix __docs__

    def __init__(self, input):  
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
<div id="main_container"><pre>'''

        self.trailer = '''</pre></div></body>
                </html>'''

        self.indent = ''
        self._input = open(input)
        self._output = open('%s.html' % input[:-3], 'w')
        self._output.write(header)
        self.analyze()
        self._input.close()
        self._output.close()
        
    def analyze(self):
        '''This method will accept a list of token pairs from get_tokens
        and it's gonna analyze it, add the appropriate html tags, and add it to 
        the _output object'''
        function = False
        tokens = generate_tokens(self._input.readline)
        for toknum, tokval, (srow, scol), (erow, ecol), line in tokens:
            out = ''
            space = ''

            if ecol <= len(line)-2:
                if line[ecol] == ' ':
                    space = ' '

            tokname = tok_name[toknum]
            if tokname == 'NEWLINE' or tokname == 'NL':
                self._output.write('\n%s' % self.indent)
            elif tokname == 'INDENT':
                self._output.write('    ')
                self.indent += '    '
                
            elif tokname == 'DEDENT':
                
                self._output.seek(-4, 1)
                self.indent = self.indent[:-4]

            elif iskeyword(tokval) or tokval == '(' or tokval == ')':
                if tokval.lower() == 'def':
                    function = True
                out = '<span class="%s"><b>%s</b></span>' % ('ifdef', tokval)

            elif tokname == 'NAME' or tokname == 'OP':
                if function == True:
                    out = '<span class="%s"><b>%s</b></span>' % ('def', tokval)
                    function = False
                else:
                    out = tokval
                                     
            elif tokname == 'NUMBER':
                out = '<span class="%s"><b>%s</b></span>' % ('int', tokval)

            elif tokname == 'STRING':
                if tokval[:3] == '\'\'\'':
                    out = '<span class="%s"><b>%s</b></span>' % ('int', escape(tokval))
                else:
                    out = '<span class="%s">%s</span>' % ('str', escape(tokval))
              
            elif tokname == 'COMMENT':
                out = '<span class="%s"><b>%s</b></span>' % ('comm', escape(tokval))

            else:
                self._output.write(out)
                self._output.write(self.trailer)

            self._output.write('%s%s' % (out, space))

     
script, name = argv
#length check for argv later

PythonParse(name)
