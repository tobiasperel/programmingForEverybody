import xml.etree.ElementTree as ET
import urllib.request,urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = "http://py4e-data.dr-chuck.net/comments_901130.xml"
xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml)
counts = tree.findall('.//count')
suma = 0
for count in counts:
    texto = count.text
    num = int(texto)
    suma+=num
print(suma)


