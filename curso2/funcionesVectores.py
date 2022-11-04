numeros=[4,2,-5,6,324,23]
numeros.sort()  #con la funcion sort ordenas los de menor a mayor, se puede hacer tambien en string
print(numeros)
nombres=['carla','jazmin','zala','aaaaaaaaaaaaaaaaaaaaaaaa','colalal']
nombres.sort()#ordena por orden alfabetico, sin importar la cantidad de caracteres
print(nombres)
frase=input("Escribe una frase: ")
frase=frase.split()#convierte la frase en un vector
#con palabras como si fuesen cada uno una variable
print(len(frase))
print(frase[0])

for i in frase: #este es un for de lo mas comun
    print(i)
#en el split() lo que pongas dentro de los parentesis va a definir
#cuando corta las palabras, si no pones nada simboliza un espacio pero podes
#poner por ej: split(:) entonces cunado vea esa va a separar la palabra
