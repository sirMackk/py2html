#!/usr/bin/python

from sys import argv
from re import search, split
#html tag vars, will make this work better later
ifdef = '<span class="ifdef">'
integer = '<span class="int">'
defi = '<span class="def">'
stri = '<span class="str">'
comment = '<span class="comm">'
doc = '<span class="doc">'

end_span = '</span>'
flow_control = ['class', 'if', 'elif', 'else', 'while', 'for', 'return', 'from', 'import']
blue_words = ['and', 'or', 'in', 'is', 'import']
#four_spaces = '&nbsp&nbsp&nbsp&nbsp'
   
    #re.split(r'(\s+)', stri, 1)
    #this seems to be a good way to get leading whitespace from strings to avoid using a loop
    #use ''.join(y) to join stuff back afterwards

def build_header():
    '''This function build the html header'''
    pass
 
        
def analyze(line):
    '''This function accepts a line of python code and returns the line
    after formatting it with html tags'''
    product = []
    #splits a line into whitespace [1] and rest of line
    white_rest = re.split(r'(\s+)', line, 1)

    #white_rest[0] == '' when there is indent
    if white_rest[0] == '':
        #append white space to beginning of line
        product.append(white_rest[1])
        #split string, get the first word, go through first_word function, append it
        #check if line is a comment, mark it green, else continue analysis
        if white_rest[2][0] == '#' or white_rest[2][0:3] == '\'\'\'' or white_rest[2][-3:]:
            product.append(is_comment_or_doc(white_rest[2]))
        else:
            #gets first word of the line, appends string
            #update, if first word is def, it's gonna call different function
            #to color func name pink
            first_word = white_rest[2].split(' ', 1)
            if first_word[0].lower() == 'def':
                #under construction
                product.append(first_word_def(first_word[1]))
            else:
                product.append(first_word(white_rest[2].split(' ', 1)[0]))
            #analyzes rest of line, appends a string
            product.append(rest_of_line(white_rest[2].split(' ', 1)[1]))
    #line != '', meaning no whitespace, so can take first word, analyze it
    #then take rest of line and analyze it
    #UPDATE: gonna update this part of the function after I get most of stuff working
    #because this is similar to the above flow block, except with different indices
    else:
        if white_rest[0] == '#' or white_rest[0:3] == '\'\'\'' or white_rest[2][-3:]:
            #appends a string, joins white_rest to feed is_comment with string
            product.append(is_comment_or_doc(''.join(white_rest)))
        else:
            #analyze first word
            if white_rest[0].lower() == 'def':
                pass
            product.append(first_word(white_rest[0]))
            #analyze rest of line
            product.append(rest_of_line(white_rest[2]))    

    #this func returns a string of join list items prepared by previous functions
    return ''.join(product)
def is_comment_or_doc(line):
    '''This function takes in a string and appends comment <span> tags to it
    or if it's a __doc__ then it adds orange <span> tags'''
    if line[0] == '#':
        return '%s%s%s' % (comment, line, end_span)
    else:
        return '%s%s%s' % (doc, line, end_span)
#REWRITE THIS FUNCTION USING REGEX SUB or REPLACE, MUCH EASIER, NICER AND MAYBE FASTER
def first_word_def(rest):
    first = '%s%s%s' % (ifdef, 'def ', end_span)
    left = rest[1].split('(', 1)
    first += '%s%s%s%s(%s%s)%s:' % (defi, left, end_span, ifdef, end_span, left[1].split(')', 1), ifdef, end_span)
    return first
    


def first_word(word):

    '''This function uses string concatation to produce and return a flow control
    instruction enclosed in the right html tags or returns initial word if it's not 
    a flow control instruction'''
    #first check if word is a comment
    #then check for flow control words
    flow = ''
    ##one way to do this job
    # for i in flow_control:
        # if word == i.lower():
            # flow += ifdef
            # flow += word
            # flow += end_span
    #another way of doing this job:

    #first gotta check if line ain't a comment
    
    if word in flow_control:
        pass
        
        
    return word


#commented these out so nose can run
# def rest_of_line(words):
    # i = 0
    # work = words.split()
   ## main loop to skip over list of words, modify i sometimes
    # while i < range(len(work)):

    
    
############
#MAIN LOOP
############  
#do input verification here dude    
# script, filename = argv

#opens file in memory
# input = open('%s.py' % filename)
# output = open('%s.html' % filename, 'w')
#should write the header of the html file to the file
#only after the main loop is done should it add the footer
#file = input.readlines()
# for i in file:
    # output.write(first(i))
#closes file
# input.close()
# output.close()
