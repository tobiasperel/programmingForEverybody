(0,1,2)>(1,2,3) #se fija primero el primer numero,despue el segundo y asi pero el mas importante es el primrero 199<200
d=dict()
d={"a":15,"b":20,"c":-15}
d=sorted( d.items() )# me los ordena por la key
print(d)
#--------------------------------------------
#para ordenanrlos por values hay que hacer esto
r={"a":15,"b":20,"c":-15}
l=list()
for k,v in r.items():
    l.append((v,k))
l=sorted(l)
print(l)
l.sort(reverse=True)#asi doy vuelta una lista
print(l )
#---------------------------------------------------
#guarda un diccionario con las key y values
x={"javier":1,"gonzalo":2,"manaos":3}
y=x.items()
print(y)
