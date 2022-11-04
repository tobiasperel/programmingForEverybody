archivo = open("archivo4.txt")
nombres = dict()
for line in archivo:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    nombres[email] = nombres.get(email,0)+1

ordenado=sorted(nombres.values())
print(ordenado)
#for k,v in ordenado:
#    print((k,v))