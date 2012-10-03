py2html

What is it?

This python 2.7 program reads a python .py source file and outputs it in a color-coded and nicely formatted html file.

Why?

To practice some file I/O and regex

Who?

sirMackk on github.com


The way it works:
Use it as you would use a CLI utility ie. type in "py2html.py name_of_source_file.py" and the script will output an html file of the same name as the input filename. 

Debriefing for version 0.1:

I learned a lot. Started out experimenting with regex, shelx and .split(), but none of those methods gave any results. I would have to do a lot of work with them to get some nice output. I finally turned to the tokenize module as suggested on StackOverflow and this saved me days or weeks of work.

File I/O was the easiest part of this project, although I did learn a good deal about it. The main obstacle was working with a token generator and getting it to preserve the whitespace structure of a python file. I decided on a pretty large if-else structure instead of seperate function calls to make the code more readable and a bit shorter. There are a few nasty lines of code in there, but I haven't gone down to thinking about making them prettier since they work fine for now and they are able to handle most python source file in a matter of seconds, which is acceptable. Learned a great deal about generators, too.

I was not able to write any tests, since the class only uses one constructor function and one general function, which doesn't even return a value. I believe this is also acceptable for such a small ~140 line project. 

Debriefing for version 0.2:

Th project grew by about 70 lines. This includes giving the class the possibility to return the tagged code without any headers, ideal for embedding in web pages. This might come in mighty handy in a few months. However, I have not had the chance to test this functionality in the wild.

I still have to research how to make my code easier to read and a bit more about best practices, although I see a big improvement since my previous project. There is still more learning to be done.