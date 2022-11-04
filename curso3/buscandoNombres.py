import urllib.request,urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/known_by_Oluwaferanmi.html"


for i in range(7):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    contador=1
    for tag in tags:
        if(contador<=18):
            url = tag.get("href",None)
            contador+=1
    print(url)

separacion = url.split("_")
nombres = separacion[2].split(".")
print(nombres[0])



