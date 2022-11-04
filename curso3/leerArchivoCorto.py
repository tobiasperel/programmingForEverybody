import urllib.request, urllib.parse, urllib.error

archivo = urllib.request.urlopen("http://data.pr4e.org/intro-short.txt") # entre los parentesis va el link
for line in archivo:
    print(line.decode().strip())