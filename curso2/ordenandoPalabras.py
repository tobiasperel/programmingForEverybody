archivo=input("Enter file name: ")
archivo=open(archivo)
nombres=list()

for line in archivo:
    line=line.rstrip()
    palabra=line.split()
    for i in range(len(palabra)):
        if palabra[i] in nombres:
            continue
        nombres.append(palabra[i])


#print(nombres)
nombres.sort()
print(nombres)
