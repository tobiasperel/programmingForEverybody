#Primero es necesario importar esto:

import urllib.request,urllib.parse, urllib.error
from bs4 import BeautifulSoup

#luego a continuacion viene tres lineas claves de codigo:

#la primera que consiste en el link de la paginal
url = "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox/FMfcgxwJZJSxnDTvVGPJBgPrCVDbbXGX"
html = urllib.request.urlopen(url).read() # aca lo leemos
codigo = BeautifulSoup(html, "html.parser")# Finalmete aca lo que hacemos es ordenarlo como html

print(type(codigo)) #<class 'bs4.BeautifulSoup'>

tags = codigo("a") #aca lo que hacemos es que tags simpoblice cada vexzz
print(tags)# me imprime todos los links

for tag in tags:
    url = tag.get("href",None)
    print(url)
print(type(url)) # consideremos que el url es un string por ende se le atribuyen las funciones de tal
