import json

data = '''{
    "name":"Tobias",
    "phone":{
        "type" : "intil",
        "number" : "+54911454543"
    },
    "email" : {
        "hide" : "yes"
    }      
}'''

info = json.loads(data)# esto nos devuelve in diccionario!!
print(info)
print("Name:",info["name"])#lo manejas como diccionario
print("Hide:",info["email"]["hide"])#dentro de email toma que hay otro diccionario,
# asi se accede
print("number:",info["phone"]["number"])

# tambien podemos hacer listas de diccionarios:

data2 = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "Chuck"
    } ,
     {"id" : "1232",
      "x" : "fd2",
      "name" : "Tobias"
    }
]'''

info2 = json.loads(data2)
print(len(info2))#aca se puede ver que son dos elementos en la lista

for item in info2:
    print("Name:",item["name"])
    print("ID:", item["id"])
