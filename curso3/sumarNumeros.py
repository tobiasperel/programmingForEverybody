import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/comments_901128.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("span")
contador=0
suma=0

for tag in tags:
    palabras=str(tag)
    numero= re.findall("[0-9]+",palabras)
    suma=suma+int(numero[0])
    contador+=1

print(suma)
print(contador)