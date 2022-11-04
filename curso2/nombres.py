#te dice la cantidad de veces que salio cada nombre
counts=dict()
names=["bob","stuart","camila","bob","bob","stuart","camila","bob","glen"]

for i in names:
    if i not in counts:
        counts[i]=1
    else:
        counts[i]+=1

print(counts)

# una mejor forma de hacerlo es asi:
counts=dict()
names=["bob","stuart","camila","bob","bob","stuart","camila","bob","glen"]
for i in names:
    counts[i]=counts.get(i,0)+1
# lo que hace la funcion get es fijarse si en ya existe ese nombre,
# si es asi le suma uno, pero si no existe el valor por defaulf es 0
print(counts)
#esto es igual a counts.get(i,0)

if i in counts:
    x=counts[i]
else:
    x=0
