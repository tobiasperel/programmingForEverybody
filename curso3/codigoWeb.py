import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input("Enter-") #http://www.dr-chuck.com/
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")


tags = soup("a")  # lo que hago es imprimir desde el <a hasta el a> que son todos los hiperfvinculos
for tag in tags:
    print(tag.get("href",None))

