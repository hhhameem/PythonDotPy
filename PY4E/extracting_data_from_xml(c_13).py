# -*- coding: utf-8 -*-
"""Extracting Data from XML(C-13).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AGB6LmzjN-nyBWJ47SqtHxRc0Cq5yaJx
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')

print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
# comment = data.decode()
tree = ET.fromstring(data)

counts = tree.findall('comments/comment')

print(len(counts))

count_values = list()

for result in counts:
    count_values.append(result.find('count').text)

print(count_values)
sum=0
for count in count_values:
    sum = sum + int(count)

print('sum:', sum)