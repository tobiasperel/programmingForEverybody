import urllib.request,urllib.parse,urllib.error
import json

serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?%27"

while True:
    address = input("Enter location: " ) #Ann Arbor, Mi
    if len(address)<1:
        break
    url = serviceurl + urllib.parse.urlencode({"address":address})#esto lo que hace es sumar el address
    #y convertirlo como lo lee google: Ann Arbor, Mi ---> Ann+Arbor%2C+Mi

    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrived",len(data),"characters")

    try:
        js = json.loads(data) # aca lo convertimos en un diccionario
    except:
        js = None

    if not js or "status" not in js or js["status"] != "ok" : #practicamente si el archivo esta vacio
        print("=== Failure to Retrive ")
        print(data)
        continue

    print(json.dumps(js,indent=4))#printea el archivo creo

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat" , lat , "lng" , lng)
    location = js ["result"][0]["formatted address"]
    print(location)





