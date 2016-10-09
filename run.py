import xml.etree.ElementTree as ET
import requests
import os
import sys
import time

word = sys.argv[1].strip()
print(word)
url = 'http://www.dictionaryapi.com/api/v1/references/collegiate/xml/' + word + '?key=' + os.environ['MERRIAM_WEBSTER_API_KEY']
r = requests.get(url)
root = ET.fromstring(r.content)
# root = ET.parse('sample.xml').getroot()

output = ''
for definition in root.findall('.//entry[1]//*/dt'):
    output += ET.tostring(definition) + '\n'

print(output)

if not os.path.exists('output'):
    os.makedirs('output')
f = open('output/' + word + '.html', 'w')
f.write(output)
f.close()

time.sleep(2)
