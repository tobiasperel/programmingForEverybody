import urllib.request,urllib.parse,urllib.error
import json

url = "http://py4e-data.dr-chuck.net/comments_901131.json"

connection = urllib.request.urlopen(url)
data = connection.read().decode()

print(type(data))

js = json.loads(data) # hago que sea un diccionario
suma=0
print(type(js))
for i in js['comments']:
    suma+=i['count']
print(suma)