import re
archivo=input("Enter file name: ")
archivo=open(archivo)
suma=0
contador=0
for line in archivo:
    line=line.rstrip()
    num=re.findall("[0-9]+",line)
    if len(num)>0:
        contador=0
        for numero in num:
            numero=numero.rstrip()
            nume=int(num[contador])
            suma+=nume
            contador+=1
print(suma)
