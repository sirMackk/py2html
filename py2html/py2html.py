#!/usr/bin/python

from sys import argv
from re import search, split
#gets file name from command line
ifdef = '<span class="ifdef">'
integer = '<span class="int">'
defi = '<span class="def">'
stri = '<span class="str">'

end_span = '</span>'
flow_control = ['class', 'def', 'if', 'elif', 'else', 'while', 'for', 'return', 'from', 'import']
blue_words = ['and', 'or', 'in', 'is']
#four_spaces = '&nbsp&nbsp&nbsp&nbsp'
   
    #re.split(r'(\s+)', stri, 1)
    #this seems to be a good way to get leading whitespace from strings to avoid using a loop
    #use ''.join(y) to join stuff back afterwards
    
#TODO:
#Think of a way of parsing function calls like this:
#product.append(white_rest[1]) for example. They at least need the integers colored
  
 
        
def analyze(line):
    '''This function accepts a line of python code and returns the line
    after formatting it with html tags'''
    product = []
    #splits a line into whitespace [1] and rest of line
    white_rest = re.split(r'(\s+)', line, 1)
    product.append(white_rest[1])
    #this function will take the rest of line [2] and match the first word
    #to flow control
    #it splits the first word from the rest, this word [0] will be compared to flow control list
    #then rest of line will be sent to next function
    first = white_rest[2].split(' ', 1)
    #YOU GOTTA SEE IF ITS A DEF, IF YES, GOTTA COLOR THE DEF NAME PINK
    #flo function will decide on first word of line and return a formatted html string
    product.append(flo(first[0]))
    #rest function will take care of the rest of the line, after the first word
    product.append(rest(first[1]))
    #place for leading word comparison function

    #this func returns a string of join list items prepared by previous functions
    return ''.join(product)
def flo(word):
    '''This function uses string concatation to produce and return a flow control
    instruction enclosed in the right html tags or returns initial word if it's not 
    a flow control instruction'''
    flow = ''
    ##one way to do this job
    # for i in flow_control:
        # if word == i.lower():
            # flow += ifdef
            # flow += word
            # flow += end_span
    #another way of doing this job:
    if word in flow_control:
        flow += ifdef
        flow += word
        flow += end_span
        
    return word
    
def rest(words):
    '''This function will loop over every word left in search of and/or/in/other
    and mark them blue. It will also check every word's first character for an " or ', if 
    if finds it, it will call a string coloring function and insert the right
    coloring into the list preceeding the string and then after it. It should also
    color integers'''
    #TODO : make sure that the insertion indices are correct, use !!!NOSE!!!
    
    #Ok, so the way this while loop works is that it loops through the items
    #of a list of words. First it tries an item if it's an int - if True, 
    #it inserts the html tags before and after the item (see: TODO).
    
    while i < range(len(words)):
    #archaic for loop:
    #for i in range(len(words)):
        try:
            int(words[i])
            words.insert(i, integer)
            words.insert((i+2), span_end)
        #if it's not an integer, program will skip here.
        #here, the program checks for quotes. If it finds a quote
        #it places and html tag before it and goes into an inner loop to find 
        #the end of the quote to place the closing tag, after which it adds length 
        #of the string to the WHILE LOOP accumulator i so that i continues color-coding
        #after the end of the string.
        #TODO: Next, if its not an int or quote, it should look for a bunch of instructions
        #like and/or/in/is and such and color them blue.
        except ValueError:
            #these ifs and for look for quotations
            if words[i][0] == '\'' or words[i][0] == '"':
            #this should place a span tag before every string
                words.insert((i), stri)
                #inner loop that looks for the end of a quote
                for j in range(len(words)):
                    if words[j][len((words[j]-1))] == '\'':
                        words.insert((j+1), end_span)
                        i += j
                        break
                    elif words[j][len((words[j]-1))] == '\"':
                        words.insert((j+1), end_span)
                        i += j
                        break
            #this else looks for blue instructions           
            else:
                if words[i] in blue_words:
                    #add color tags to list of words
                
         i += 1   
                
               # closeString(words[i:len(words)])
        #when the tag-enchanced list is ready, return it for joining
        return words
    
            
    
def closeString(stringy):
    for i in range(len(stringy)):
            if stringy[i][len((stringy[i]-1))] == '\'' or stringy[i][len((stringy[i]-1))] == '\"':
            #this should find end of all strings and place ending html tag
                stringy.insert((i+1), end_span)        
    
    
    
    
############
#MAIN LOOP
############  
#do input verification here dude    
script, filename = argv

#opens file in memory
input = open('%s.py' % filename)
output = open('%s.html' % filename, 'w')
#should write the header of the html file to the file
#only after the main loop is done should it add the footer
#file = input.readlines()
for i in file:
    output.write(first(i))



#closes file
input.close()
output.close()
