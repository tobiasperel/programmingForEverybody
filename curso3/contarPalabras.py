import urllib.request, urllib.parse, urllib.error

archivo=urllib.request.urlopen("http://data.pr4e.org/intro-short.txt")

counts=dict()
for line in archivo:
    line=line.decode().split()
    for word in line:
        counts[word]=counts.get(word,0)+1
print(counts)
