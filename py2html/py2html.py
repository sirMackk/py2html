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
p_sisr = '<span class="ifdef">)</span>'
p_sisl = '<span class="ifdef">(</span>'
definition = '<span class="ifdef">def </span>'
lb = '<br />'

end_span = '</span>'
flow_control = ['class', 'if', 'elif', 'else', 'while', 'for', 'return', 'from', 'import', 'print']
blue_words = ['and', 'or', 'in', 'is', 'import']
#TODO: Later on, check if whitespace is parsed properly by browser, if not, than add &nbsp

def build_header():
    '''This function builds the html header'''
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
            first_word = white_rest[2].split(' ', 1)
            #different case if the word is def
            if first_word[0].lower() == 'def':
                product.append(first_word_def(first_word[1]))
            else:
                product.append(first_word(first_word[0]))
                #analyzes rest of line, appends a string
                product.append(rest_of_line(first_word[1]))

    elif len(white_rest) == 1:
        #if white_rest is a single entry, means it can only have blue parenthesis
        #or grey strings or orange ints
        product.append(find_ints(find_strings(white_rest)))
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
        return '%s%s%s%s' % (comment, line, end_span, lb)
    else:
        return '%s%s%s%s' % (doc, line, end_span, lb)

def first_word_def(rest):
    '''This function returns an html formatted string if the first word
    is "def". It makes the name of the function a different color.'''
    
    return definition + defi + rest[:rest.index('(')] + end_span + p_sisl + rest[(rest.index('(')+1):rest.index(')')] + p_sisr + rest[-1] + lb
    


def first_word(word):

    '''This function uses string concatation to produce and return a flow control
    instruction enclosed in the right html tags or returns initial word if it's not 
    a flow control instruction'''
  
    if word in flow_control:
        return ifdef + word + ' ' + end_span
    else:           
        return word


#work on this next
def rest_of_line(words):
    #It seems the best course of action would be to create two more functions:
    #find_strings and find_ints, that would cycle over a string and insert tags 
    #in the right places. After that, rest_of_line would split the string and look for 
    #blue words, tag them and return ''.join them
    i = 0
    work = words.split()
   # main loop to skip over list of words, modify i sometimes
    while i < range(len(work)):
        pass

def find_strings(words):
    list_1 = [i for i, a in enumerate(words) if a == '\'']
    i = 0
    words_out = ''
    #this will iterate over list_1, so i is it's index
    while i < len(list_1):
        words_out += words[:list_1[i]] + comment
        j = 1
        while j < len(list_1)-1:
            print i, j
            if list_1[i]+j == list_1[(i+j)]:
                j += 1
            else:
                #this will close the tag
                words_out += words[list_1[i]:list_1[(i+j)]] + end_span 
                i += j
                break
        



    return words_out
    
    
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
