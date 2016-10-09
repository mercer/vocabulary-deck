from os import walk
import os
import re
(_, _, filenames) = walk('output').next()

f = open('deck.txt', 'w')
eol_removal = re.compile('[\n\r]')
for filename in filenames:
    with open('output/' + filename, 'r') as content_file:
        question = os.path.splitext(filename)[0]
        answer = eol_removal.sub('', content_file.read())
        f.write(question + '\t' + answer + '\n')

f.close()
