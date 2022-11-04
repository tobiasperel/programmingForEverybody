archivo=input("Enter file name: ")
archivo=open(archivo)
horas=dict()

for line in archivo:
    line=line.rstrip()
    if len(line)>5 and line.startswith("From "):
        wds=line.split()
        hora=wds[5].split(":")
        horas[hora[0]]=horas.get(hora[0],0)+1
print(horas)
ordenado=sorted(horas.items())
for k,v in ordenado:
    print(k,v) #los segundos parentesis son para que los imprima como (a,b) y no a,b
