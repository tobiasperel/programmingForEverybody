archivo=input("Enter file name: ")
archivo= open(archivo)

mayor=list()
grande=list()
for line in archivo:
          line=line.rstrip()
          if len(line)>1 and line.startswith("From "):
              wds=line.split()
              correos[wds[1]]=correos.get(wds[1],0)+1
              #print(wds[1])
              if len(mayor)==0:
                  mayor.append(correos[wds[1]])
              elif correos[wds[1]]>mayor[len(mayor)-1]:
                  mayor.append(correos[wds[1]])
                  grande.append(wds[1])

#print(correos.keys())
#print(correos.values())
print(grande[len(grande)-1],mayor[len(mayor)-1])
