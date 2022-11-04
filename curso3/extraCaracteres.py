#Se debe importar la libreria
import re

archivo=input("Enter file name: ")
archivo=open(archivo)

for line in archivo:
    line=line.rstrip()             #lo que hace este for es buscar si hay alguna linea que EMPIECE con from
    if re.search("^From: ", line):  # lo primero qu le mandas es lo que buscas(string),despues la linea
        print(line)

# ^hola.*: #Esto quiere decir que tiene que empezar con hola, debe seguir con caracter y el * simboliza que debe ser de 0-inf
# ^hola\S+: #Esto quiere decir que tiene que empezar con hola, debe no tener espacios despues y el mas significa una o mas veces

line="La verda de 100 paises de los 5 continentes"
y= re.findall("[0-9]+",line) #busca si hay algun numero en el archivo
print(y)
y=re.findall("[AEIOU]+",line)#busca si aparece si alguna mayuscula vocal
print(y)

#supongamos que ahora tenemos esta frase:
line="From: Using the: " # y yo quiero buscar la palabra From
y= re.findall("^F.+: ",line) # aca me va a devolver desde la f hasta los : pero va a imprimir lo maximo posible
print(y) # que en este caso seria "From:"

#si yo quisiese que me imprima lo mas chico posible:
line="From: Using the: " # y yo quiero buscar la palabra From
y= re.findall("^F.+?: ",line) # aca me va a devolver desde la f hasta los : pero va a imprimir lo minimo posible
print(y) # que en este caso seria "From"

#si yo quisiese que me imprima el mail:
line="From: pereltobias@gmail.com sun sep 20 18:06:24 2020"
y= re.findall("\s+@\s+",line) # el \s+ significa minimo un espacio porque el mas de 1-inf lo mismo despues
print(y) # imprime el mail


line="From: pereltobias@gmail.com sun sep 20 18:06:24 2020"
y= re.findall("^From (\s+@\s+)",line) # con los parentesis le indico que quiero que no me guarde el from
print(y) # imprime el mail
